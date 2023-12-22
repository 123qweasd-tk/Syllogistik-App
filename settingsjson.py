import json

settings_json = json.dumps([
    {'type': 'bool',
     'title': 'Switch to completed Syllogistic',
     'desc': 'Completed Syllogisitc contains also ã-, ë-, ï- and õ-judges',
     'section': 'trainer',
     'key': 'completedsyllogistic'},
    {'type': 'bool',
     'title': 'Switch to more than one particular premis possible',
     'desc': '25% more of the conclusions will result in no relevant judge',
     'section': 'trainer',
     'key': 'particularpremis'}])
