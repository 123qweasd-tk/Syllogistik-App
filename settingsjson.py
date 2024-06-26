import json

settings_json = json.dumps([
    {'type': 'bool',
     'title': 'Wechsle zu vollständiger Syllogistik',
     'desc': 'Vollständige Syllogistik beinhaltet auch ã-, ë-, ï- and õ-Urteile',
     'section': 'trainer',
     'key': 'completedsyllogistic'},
    {'type': 'bool',
     'title': 'Wechsle zu: Mehr als eine partikuläre Prämisse möglich',
     'desc': '25% mehr der Konklusionen werden in keinem relevanten Urteil resultieren',
     'section': 'trainer',
     'key': 'particularpremis'}])
