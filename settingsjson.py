import json

settings_json = json.dumps([
    {'type': 'bool',
     'title': 'Wechsle zwischen Üben und Ausrechnen',
     'desc': 'Entweder das Programm rechnet für dich oder dir werden die Prämissen als Geltungswertformeln angezeigt',
     'section': 'trainer',
     'key': 'calculate_exercise'},
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
