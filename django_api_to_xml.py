# -*- coding: utf-8 -*-

# initialize Django API

import os, sys, codecs
os.environ.setdefault ('DJANGO_SETTINGS_MODULE', 'trimco.settings')

import django
django.setup ()

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach()) # for printing; parasol server for some curious reason uses latin-1 locale

# import some models

from info.models import Speaker
from corpora.models import Recording

import xml.etree.cElementTree as ET

fields = ('id', 'string_id', 'sex', 'year_of_birth', 'language', 'education', 'location')  # fields we want to include in an XML file


if __name__ == '__main__':

    speakers = Speaker.objects.all ()   # get all speakers

    meta = ET.Element ("meta")

    for speaker in speakers:

        person = ET.SubElement (meta, "person")

        from info.models import LanguageRelation
        language = LanguageRelation.objects.get (to_speaker_id = speaker.id) #get id of language
        language_id = language.to_language_id

        from morphology.models import Language
        language_name = Language.objects.get(id=language_id) #get name of language

        from info.models import EducationType
        education = EducationType.objects.get (id = speaker.education_id) #get education

        from info.models import LocationRelation
        location = LocationRelation.objects.get (to_speaker_id = speaker.id) #get id of location
        location_id = location.to_location_id

        from info.models import Location
        location_name = Location.objects.get(id=location_id) #get name of location
        
        gps = location_name.position
        gps_longitude = gps.longitude
        gps_latitude = gps.latitude
        location_data = [str(gps_longitude), str(gps_latitude)]

        speaker_data = [str(speaker.id), speaker.string_id, speaker.sex, str(speaker.year_of_birth), language_name.name, education.name, location_name.name]
        print (' '.join (speaker_data))

#write to xml

        gps = ET.SubElement (person, "gps")
        i = 0
        for sd in speaker_data:
            ET.SubElement(person, fields [i]).text = sd
            i += 1
        ET.SubElement(gps,  "longitude").text = str(gps_longitude)
        ET.SubElement(gps,  "latitude").text = str(gps_latitude)

    tree = ET.ElementTree (meta)
    tree.write ("metadata_export.xml", encoding = 'utf-8', xml_declaration = True)

#    for speaker in speakers:
#        speaker_data = [getattr (speaker, field) for field in fields] # or this way
#        print (' '.join ([str (dt) for dt in speaker_data]))
