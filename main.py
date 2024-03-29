from kivy.app import App
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty, ConfigParserProperty, ObjectProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color
from kivy.base import runTouchApp
from kivy.vector import Vector
from kivy.uix.scrollview import ScrollView

from kivy.config import Config
from kivy.config import ConfigParser


from settingsjson import settings_json
import webbrowser
import random

Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        space: dp(10)
        Label:
            text: 'Menu'
            font_size: dp(40)
            color: 0,1,0.5
        Button:
            text: 'General'
            font_size: dp(25)
            on_press: root.manager.current = 'general'
            background_normal: ''
            background_color: 1, .3, .4, .85
        Button:
            text: 'Conclusions (M•P, S•M -> S•P)'
            font_size: dp(25)
            on_press: root.manager.current = 'menu_conclusions'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Total-formulas (M•P, S•M, S•P <-> S•M•P)'
            font_size: dp(25)
            on_press: root.manager.current = 'menu-total-formulas'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Transformations (S•P <-> S•P)'
            font_size: dp(25)
            on_press: root.manager.current = 'menu_transformations'
            background_normal: ''
            background_color: 1, .2, .4, .3
        Button:
            text: 'Conditional-Statements (^c)'
            font_size: dp(25)
            on_press: root.manager.current = 'conditional-statements'
            background_normal: ''
            background_color: 1, .2, .4, .3
        Button:
            text: 'Ressources'
            font_size: dp(25)
            on_press: root.manager.current = 'ressources'
            background_normal: ''
            background_color: 1, .3, .4, .85
        Button:
            text: 'Quit'
            font_size: dp(25)
            on_press: app.stop()

<GeneralScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Introduction'
            font_size: dp(25)
            on_press: root.manager.current = 'menu_introduction'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Quiz'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
    Button:
        text: "Menu"
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

<Menu_introductionScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'The logical Principles'
            on_press: root.manager.current = 'menu_introduction_1'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Direct Inferences/Indirect Inferences'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Pure vs. Applied Logic'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Structure of the app'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
    Button:
        text: "Menu"
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

<Menu_introductionScreen_1>
    ScrollView:
        do_scroll_y: True
        do_scroll_x: False
        Label:
            text: root.label_Menu_introductionScreen_1_text
            size_hint_y: None
            text_size: self.width, None
            height: self.texture_size[1]
            Button:
                text: "Menu"
                on_press: root.manager.current = 'menu'
                size_hint: "0.1", "0.1"
                pos_hint: {"x":0.9,"y":0.9}

<Menu_conclusionsScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Introduction'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Playground'
            font_size: dp(25)
            on_press: root.manager.current = 'conclusions'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Quiz'
            font_size: dp(25)
            on_press:
                root.manager.current = 'training'
            background_normal: ''
            background_color: 1, 0, .5, .3
    Button:
        text: 'Menu'
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

<ConclusionsScreen>:
    Button:
        text: 'Menu'
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

<TrainingScreen>:
    Button:
        text: 'Menu'
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}
    Button:
        id: 'settings_button'
        text: 'Settings'
        on_release: app.open_settings()
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.7}

<Menu_total_formulas_Screen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Introduction'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Playground'
            font_size: dp(25)
            on_press: root.manager.current = 'total-formulas-quiz'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Quiz'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, 0, .5, .3

<Total_formulas_QuizScreen>:
    Button:
        text: 'Menu'
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

<Menu_TransformationsScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Introduction'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Playground'
            font_size: dp(25)
            on_press: root.manager.current = 'transformations'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Quiz'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, 0, .5, .3

<TransformationsScreen>:
    Button:
        text: 'Menu'
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

<Conditional_StatementsScreen>
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Introduction'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Playground'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Quiz'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, 0, .5, .3
    Button:
        text: 'Menu'
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

<RessourcesScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Ressources"
            font_size: dp(30)
        Button:
            text: 'P vs. NP-Problem'
            font_size: dp(25)
            on_press:
                import webbrowser
                webbrowser.open('https://en.wikiversity.org/w/index.php?title=User:123qweasd-tk/Proof_for_NP_unequal_P_by_Thomas_K%C3%A4fer&oldid=2614943')
        Button:
            text: 'SAT'
            font_size: dp(25)
            background_normal: ''
            background_color: 1, 0, .5, .3
        Button:
            text: 'Pure Strict syllogistic, Version from 16:44, 15 January 2024'
            font_size: dp(25)
            on_press:
                import webbrowser
                webbrowser.open('https://en.wikipedia.org/w/index.php?oldid=1195852979#Pure_Strict_syllogistic')
    Button:
        text: "Menu"
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

""")

class MenuScreen(Screen):
    pass

class GeneralScreen(Screen):
    pass

class Menu_introductionScreen(Screen):
    pass

class Menu_introductionScreen_1(Screen):
    label_Menu_introductionScreen_1_text = StringProperty('Die logischen Prinzipien: \n\nAm Anfang des logischen Denkens ist alles eins (AiAi): \n  B   ~B \n---------\n Ai | Ai \n\n1. Die erste Stufe: \nDer Unterschied der durch gleichzeitige Anwendung der beiden logischen Prinzipien (das Prinzip der Identität und das Prinzip der Limitation) definiert wird, teilt das Eins in Zwei. Es entstehen vier Möglichkeiten, die sich alle ausschließen. Zudem entstehen Kollektiv-Kennzeichnungen (Au und uN bzw. Nu und uA (unmittelbare Schlüsse)): \n B | ~B \n------------------------------\n A |  u | AiAi | \n u |  N |          | AiAi \n N |  u | AiAi | \n u |  A |          | \n\n Unmittelbare Schlüsse (auf derselben Stufe): \nAN -> Au \nNN -> uN \nusw. \n\n2. Die zweite Stufe: \nDer Unterschied der durch gleichzeitige Anwendung der beiden logischen Prinzipien definiert wird, teilt das Zwei in Vier. Es entstehen 16 Möglichkeiten, die sich alle ausschließen. Es entstehen mittelbare Schlüsse zwischen Stufen: \n\nMittelbare Schlüsse zwischen Stufen: \n\n   a) Ganzformel -> Teilformeln: \nANNA -> auau \n            -> aauu \n\n   b) Teilformeln -> Ganzformel: \nuaua und \nuuaa und \n nunu und \nnnuu        -> NNNA \n\n3. Die dritte Stufe: \nDer Unterschied der durch gleichzeitige Anwendung der beiden logischen Prinzipien definiert wird, teilt das Vier in Acht. Es entstehen 256 Möglichkeiten, die sich alle ausschließen. Es entstehen mittelbare Schlüsse innerhalb einer Stufe (z. B. die traditionelle (und die vollständige traditionelle) Syllogistik): \n\nMittelbare Schlüsse innerhalb einer Stufe (über Mittelbegriff): \n   c) Teilformeln -> Teilformel: \naauunnaa und \naunaauna           -> auaunana \n\n\n\n\n')
    
    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        

    
class TrainingScreen(Screen):
    global foo_1
    foo_1 = []
    k = ConfigParser.get_configparser('app')
    premisissentences_ = ConfigParserProperty(1, 'trainer', 'premisissentences', k, val_type=int)
    print('llll', premisissentences_)
    
    #print(premisissentences_)
        #premisissentences_2 = get(premisissentences_)
        #print(premisissentences_2)
    print('hhhhhhhhh')


    def syllogism_example_function(self, premis_one, premis_two, solution):
        if premis_one == "MaP" and premis_two == "SaM": # example-sentences - traditional syllogistic
            return ("Wenn alle Reptilien Wirbeltiere sind \nund alle Saurier Reptilien sind, \nso sind alle Saurier Wirbeltiere.")
        elif premis_one == "MeP" and premis_two == "SaM":
            return ("Wenn kein Mitglied der ural-altaischen Gruppe Indogermane ist \nund alle Ungarn zur ural-altaischen Gruppe gehören, \nist kein Ungar Indogermane.")
        elif premis_one == "MeP" and premis_two == "SiM":
            return ("Wenn kein Raucher gesund lebt \nund einige Jugendliche Raucher sind, \nso leben einige Jugendliche nicht gesund.")
        elif premis_one == "MaP" and premis_two == "SaM":
            return ("Wenn alle Unternehmer zur Gewerbesteuer veranlagt werden \nund alle Gastwirte Unternehmer sind, \nso werden einige Gastwirte zur Gewerbesteuer veranlagt.")
        elif premis_one == "MeP" and premis_two == "SaM":
            return ("Wenn kein Vogel ein Säugetier ist \nund alle Adler Vögel sind, \nso sind einige Adler keine Säugetiere.")
        elif premis_one == "PeM" and premis_two == "SaM":
            return ("Wenn kein rechtwinkeliges Rechteck gleichwinkelig ist \nund alle gleichseitigen Dreiecke gleichwinkelig sind, \nso ist kein gleichseitiges Dreieck rechtwinkelig.")
        elif premis_one == "PaM" and premis_two == "SeM":
            return ("Wenn kein Säugetier gefiedert ist \nund alle Nachtigallen gefiedert sind, \nso ist keine Nachtigall ein Säugetier.")
        elif premis_one == "PeM" and premis_two == "SiM":
            return ("Wenn kein Autofahrer blind ist \nund einige Raucher blind sind, \nso sind einige Raucher keine Autofahrer.")
        elif premis_one == "PaM" and premis_two == "SoM":
            return ("Wenn alle Letten Indogermanen sind \nund einige Balten keine Indogermanen sind, \nso sind einige Balten keine Letten.")
        elif premis_one == "PeM" and premis_two == "SaM":
            return ("Wenn kein Knollenblätterpilz essbar ist \nund alle Steinpilze essbar sind, \nso sind einige Steinpilze keine Knollenblätterpilze.")
        elif premis_one == "MaP" and premis_two == "MiS":
            return ("Wenn für alle Dreiecke gilt, \ndass sich ein Kreis so um sie beschreiben lässt, \ndass die Eckpunkte auf dem Kreis liegen \nund wenn für alle Dreiecke gilt, \ndass sich in sie ein Kreis so beschreiben lässt, \ndass er alle drei Seiten berührt, \nso lässt sich bei einigen Figuren, \nin die sich ein Kreis beschreiben lässt, \nauch ein Kreis um diese Figur beschreiben.")
        elif premis_one == "MiP" and premis_two == "MaS":
            return ("Wenn einige Koniferen Weimutskiefern sind \nund alle Koniferen Nadelgehölze, \nso sind einige Nadelgehölze Weimutskiefern.")
        elif premis_one == "MeP" and premis_two == "MiS":
            return ("Wenn kein Indogermane Eskimo ist \nund einige Indogermanen Grönländer sind, \nso sind einige Grönländer keine Eskimos.")
        elif premis_one == "MoP" and premis_two == "MaS":
            return ("Wenn einige Philosophen keine Dichter sind \nund alle Philosophen Denker sind, \nso sind einige Denker keine Dichter.")
        elif premis_one == "MeP" and premis_two == "MaS":
            return ("Wenn kein amtierender Staatsanwalt wegen Mordes verurteilt wurde, \nund alle amtierenden Staatsanwälte Beamte sind, \nso wurden einige Beamte nicht wegen Mordes verurteilt.")
        elif premis_one == "MaP" and premis_two == "MaS":
            return ("Wenn alle Getreidearten einjährig sind \nund alle Getreidearten Körner als Samen haben, \nso haben einige einjährige Pflanzen Körner als Samen.")
        elif premis_one == "PaM" and premis_two == "MeS":
            return ("Wenn alle Trinker ungesund leben \nund keiner, der ungesund lebt, Leistungssportler ist, \nso  ist kein Leistungssportler Trinker.")
        elif premis_one == "PiM" and premis_two == "MaS":
            return ("Wenn einige Professoren Physiker sind \nund alle Physiker Naturwissenschaftler sind, \nso sind einige Naturwissenschaftler Professoren.")
        elif premis_one == "PeM" and premis_two == "MiS":
            return ("Wenn kein anorganischer Stoff belebt ist \nund einiges belebte Bewusstsein hat, \nso ist einiges mit Bewusstsein kein anorganischer Stoff.")
        elif premis_one == "PaM" and premis_two == "MeS":
            return ("Wenn alle Autos Kraftfahrzeuge sind \nund kein Kraftfahrzeug ohne Bremse ist, \nso sind einige Fahrzeuge ohne Bremsen keine Autos.")
        elif premis_one == "PeM" and premis_two == "MaS":
            return ("Wenn keine Pflanze Bewusstsein hat \nund alles mit Bewusstsein ein Lebewesen ist, \nso sind einige Lebewesen keine Pflanzen.")
        elif premis_one == "PaM" and premis_two == "MaS":
            return ("Wenn alle Quadrate Rechtecke sind \nund alle Rechtecke Trapeze sind, \nso sind einige Trapeze Quadrate.")
        elif premis_one == "MëP" and premis_two == "SeM":  # example-sentences - completed syllogistic (page 127 - Einführung in die formale Logik)
            return ("Wenn alle Nicht-Mitglieder doppelten EIntritt bezahlen und \keine Frau Mitglied ist, \so bezahlen alle Frauen doppelten Eintritt.")
        elif premis_one == "MaP" and premis_two == "SëM":
            return ("Wenn alle weniger Krebsgefährdeten eine längere Lebenserwartung haben \nund alle Nichtraucher weniger Krebsgefährdete sind, \nso haben alle Nichtraucher eine längere Lebenserwartung.")
        elif premis_one == "MãP" and premis_two == "SeM":
            return ("Wenn alle ungeraden Zahlen keine vollkommenen Zahlen sind \nund keine Potenz von drei gerade ist, \nso ist keine Potenz von drei eine vollkommene Zahl.")
        elif premis_one == "MãP" and premis_two == "SãM":
            return ("Wenn kein Nicht-Mitglied Vorsitzender werden kann \nund kein Nicht-Schwimmer Mitglied ist, \nso kann kein Nicht-Schwimmer Vorsitzender werden.")
        elif premis_one == "MëP" and premis_two == "SãM":
            return ("Wenn alle Nicht-Akademiker schlechtere Beförderungschancen haben \nund alle, die keine höhere Schule besuchten, keine Akademiker sind, \nso haben alle, die keine höhere Schule besuchten, \nschlechtere Beförderungsaussichten.")
        elif premis_one == "MeP" and premis_two == "SëM":
            return ("Wenn alle Primzahlen keine Quadratzahlen sind \nund nicht teilbare Zahlen Primzahlen sind, \nso sind nicht teilbare Zahlen keine Quadratzahlen.")
        elif premis_one == "MeP" and premis_two == "SeM":
            return ("Wenn kein Dreieck ein Viereck ist, \nso sind einige Nicht-Quadrate keine Vierecke.")
        else:
            return ("Kein Beispielsatz vorhanden.")

    def first_formula_values(self, first_formula):
        if first_formula == "MaP": # traditionelle Syllogistik
            first_formula = "auna"
        elif first_formula == "MeP":
            first_formula = "naau"
        elif first_formula == "MiP":
            first_formula = "auuu"
        elif first_formula == "MoP":
            first_formula = "uuau"
        elif first_formula == "PaM":
            first_formula = "anua"
        elif first_formula == "PeM":
            first_formula = "naau"
        elif first_formula == "PiM":
            first_formula = "auuu"
        elif first_formula == "PoM":
            first_formula = "uauu"
        elif first_formula == "MãP": # vervollständigte Syllogistik
            first_formula = "anua"
        elif first_formula == "MëP":
            first_formula = "uaan"
        elif first_formula == "MïP":
            first_formula = "uuua"
        elif first_formula == "MõP":
            first_formula = "uauu"
        elif first_formula == "PãM":
            first_formula = "auna"
        elif first_formula == "PëM":
            first_formula = "uaan"
        elif first_formula == "PïM":
            first_formula = "uuua"
        elif first_formula == "PõM":
            first_formula = "uuau"
        return (first_formula)

    def second_formula_values(self, second_formula):
        if second_formula == "SaM": # traditionelle Syllogistik
            second_formula = "auna"
        elif second_formula == "SeM":
            second_formula = "naau"
        elif second_formula == "SiM":
            second_formula = "auuu"
        elif second_formula == "SoM":
            second_formula = "uuau"
        elif second_formula == "MaS":
            second_formula = "anua"
        elif second_formula == "MeS":
            second_formula = "naau"
        elif second_formula == "MiS":
            second_formula = "auuu"
        elif second_formula == "MoS":
            second_formula = "uauu"
        elif second_formula == "SãM": # vervollständigte Syllogistik
            second_formula = "anua"
        elif second_formula == "SëM":
            second_formula = "uaan"
        elif second_formula == "SïM":
            second_formula = "uuua"
        elif second_formula == "SõM":
            second_formula = "uauu"
        elif second_formula == "MãS":
            second_formula = "auna"
        elif second_formula == "MëS":
            second_formula = "uaan"
        elif second_formula == "MïS":
            second_formula = "uuua"
        elif second_formula == "MõS":
            second_formula = "uuau"
        return (second_formula)

    def syllogism_deduction_first_value_n(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of first value
            return ("n")
        elif second_formula[0] == "n" and first_formula[1] == "n":
            return ("n")
        elif first_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        else:  # calculates potential "u"-values of first value
            return ("u")

    def syllogism_deduction_first_value_a(self, first_formula, second_formula):
        if first_formula[0] == "a" and second_formula[1] == "n" and second_formula[
            0] == "n":  # calculates potential "a"-values of first value
            return ("a")
        elif second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
            return ("a")
        else:  # calculates potential "u"-values of first value
            return ("u")

    def syllogism_deduction_second_value_n(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of second value
            return ("n")
        elif second_formula[1] == "n" and first_formula[1] == "n":
            return ("n")
        elif first_formula[0] == "n" and second_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            return ("n")
        else:  # calculates potential "u"-values of second value
            return ("u")

    def syllogism_deduction_second_value_a(self, first_formula, second_formula):
        if first_formula[0] == "a" and second_formula[0] == "n" and second_formula[
            1] == "n":  # calculates potential "a"-values of second value
            return ("a")
        elif second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
            return ("a")
        else:  # calculates potential "u"-values of second value
            return ("u")

    def syllogism_deduction_third_value_n(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            return ("n")
        elif second_formula[0] == "n" and first_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "n" and second_formula[2] == "n":
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        else:
            return ("u")

    def syllogism_deduction_third_value_a(self, first_formula, second_formula):
        if first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] == "n":
            return ("a")
        elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
            return ("a")
        else:
            return ("u")

    def syllogism_deduction_fourth_value_n(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and first_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "n" and second_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            return ("n")
        else:
            return ("u")

    def syllogism_deduction_fourth_value_a(self, first_formula, second_formula):
        if first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] == "n":
            return ("a")
        elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
            return ("a")
        else:
            return ("u")

    def syllogism_contradiction_test(self, first_formula, second_formula):
        conclusion = [0, 0, 0, 0, 0, 0, 0, 0]
        conclusion[0] = self.syllogism_deduction_first_value_n(first_formula, second_formula)
        conclusion[1] = self.syllogism_deduction_first_value_a(first_formula, second_formula)
        if conclusion[0] == 'n' and conclusion[1] == 'a':
            print('first error at 0')
            return (1)
        conclusion[2] = self.syllogism_deduction_second_value_n(first_formula, second_formula)
        conclusion[3] = self.syllogism_deduction_second_value_a(first_formula, second_formula)
        if conclusion[2] == 'n' and conclusion[3] == 'a':
            print('first error at 1')
            return (1)
        conclusion[4] = self.syllogism_deduction_third_value_n(first_formula, second_formula)
        conclusion[5] = self.syllogism_deduction_third_value_a(first_formula, second_formula)
        if conclusion[4] == 'n' and conclusion[5] == 'a':
            print('first error at 2')
            return (1)
        conclusion[6] = self.syllogism_deduction_fourth_value_n(first_formula, second_formula)
        conclusion[7] = self.syllogism_deduction_fourth_value_a(first_formula, second_formula)
        if conclusion[6] == 'n' and conclusion[7] == 'a':
            print('first error at 3')
            return (1)
        else:
            return (0)

    def syllogism_deduction_first_value(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of first value
            return ("n")
        elif second_formula[0] == "n" and first_formula[1] == "n":
            return ("n")
        elif first_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        elif first_formula[0] == "a" and second_formula[1] == "n" and second_formula[
            0] != "n":  # calculates potential "a"-values of first value
            return ("a")
        elif second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] != "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] != "n":
            return ("a")
        else:  # calculates potential "u"-values of first value
            return ("u")

    def syllogism_deduction_second_value(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of second value
            return ("n")
        elif second_formula[1] == "n" and first_formula[1] == "n":
            return ("n")
        elif first_formula[0] == "n" and second_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            return ("n")
        elif first_formula[0] == "a" and second_formula[0] == "n" and second_formula[
            1] != "n":  # calculates potential "a"-values of second value
            return ("a")
        elif second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] != "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] != "n":
            return ("a")
        else:  # calculates potential "u"-values of second value
            return ("u")

    def syllogism_deduction_third_value(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            return ("n")
        elif second_formula[0] == "n" and first_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "n" and second_formula[2] == "n":
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        elif first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] != "n":
            return ("a")
        elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
            return ("a")
        else:
            return ("u")

    def syllogism_deduction_fourth_value(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and first_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "n" and second_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] != "n":
            return ("a")
        elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
            return ("a")
        else:
            return ("u")

    def syllogism_solution(self,first_formula, second_formula):
        conclusion = [0, 0, 0, 0]
        conclusion[0] = self.syllogism_deduction_first_value(first_formula, second_formula)
        conclusion[1] = self.syllogism_deduction_second_value(first_formula, second_formula)
        conclusion[2] = self.syllogism_deduction_third_value(first_formula, second_formula)
        conclusion[3] = self.syllogism_deduction_fourth_value(first_formula, second_formula)
        return (conclusion)

    def output(self, solution):
    
        completedsyllogistic = self.function_completed_syllogistic_settings()#looks for setting
        
        if solution == ["a", "u", "n", "a"]: # traditionelle Syllogistik
            return "All S are P,\nalso known as SaP"
        elif solution == ["a", "u", "u", "u"]:
            return "Some S are P,\nalso known as SiP"
        elif solution == ["n", "a", "a", "u"]:
            return "No S is P,\nalso known as SeP"
        elif solution == ["u", "u", "a", "u"]:
            return "Some S are no P,\nalso known as SoP"
        elif (completedsyllogistic == 0) and (self.advice_premis_1 == "anua") and (self.advice_premis_2 == "anua"): #traditionelle Syllogistik: wegen des (abgeschwächten) Schlusses "Darapti"
            return "Some S are P,\nalso known as SiP"
        elif (completedsyllogistic == 1) and (solution == ["a", "n", "u", "a"]): # vervollständigte Syllogistik
            return "All P are S,\nalso known as SãP"
        elif (completedsyllogistic == 1) and (solution == ["u", "a", "a", "n"]):
            return "No P is S,\nalso known as SëP"
        elif (completedsyllogistic == 1) and (solution == ["u", "u", "u", "a"]):
            return "Some ~S are ~P,\nalso known as SïP"
        elif (completedsyllogistic == 1) and (solution == ["u", "a", "u", "u"]):
            return "Some P are no S,\nalso known as SõP"
        else:
            return ("No (allowed) \njudge possible!")

    def output2(self, my_text, my_text2):
        first_formula = my_text
        second_formula = my_text2
        self.advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_1 = self.first_formula_values(first_formula)
        self.advice_premis_2 = self.second_formula_values(second_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        solution = self.syllogism_solution(advice_premis_1, advice_premis_2)
        output_ = self.output(solution)
        result_contradiction_test = self.syllogism_contradiction_test(advice_premis_1, advice_premis_2)
        return [output_, advice_premis_1, advice_premis_2, solution, result_contradiction_test]


    def append_function(self, button):
        print(button)
        if foo_1 == []:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_1_p1.text ='n'
                self.btn_1_p1.background_color=(1, 0, 0, .7)
                self.btn_2_p1.text ='n'
                self.btn_2_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_1_p1.text ='a'
                self.btn_1_p1.background_color=(0, 1, 0, .7)
                self.btn_2_p1.text ='a'
                self.btn_2_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_1_p1.text ='u'
                self.btn_1_p1.background_color=(1, 1, 1, .7)
                self.btn_2_p1.text ='u'
                self.btn_2_p1.background_color=(1, 1, 1, .7)
        elif len(foo_1) == 1:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_3_p1.text ='n'
                self.btn_3_p1.background_color=(1, 0, 0, .7)
                self.btn_4_p1.text ='n'
                self.btn_4_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_3_p1.text ='a'
                self.btn_3_p1.background_color=(0, 1, 0, .7)
                self.btn_4_p1.text ='a'
                self.btn_4_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_3_p1.text ='u'
                self.btn_3_p1.background_color=(1, 1, 1, .7)
                self.btn_4_p1.text ='u'
                self.btn_4_p1.background_color=(1, 1, 1, .7)
        elif len(foo_1) == 2:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_5_p1.text ='n'
                self.btn_5_p1.background_color=(1, 0, 0, .7)
                self.btn_6_p1.text ='n'
                self.btn_6_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_5_p1.text ='a'
                self.btn_5_p1.background_color=(0, 1, 0, .7)
                self.btn_6_p1.text ='a'
                self.btn_6_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_5_p1.text ='u'
                self.btn_5_p1.background_color=(1, 1, 1, .7)
                self.btn_6_p1.text ='u'
                self.btn_6_p1.background_color=(1, 1, 1, .7)
        elif len(foo_1) == 3:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_7_p1.text ='n'
                self.btn_7_p1.background_color=(1, 0, 0, .7)
                self.btn_8_p1.text ='n'
                self.btn_8_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_7_p1.text ='a'
                self.btn_7_p1.background_color=(0, 1, 0, .7)
                self.btn_8_p1.text ='a'
                self.btn_8_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_7_p1.text ='u'
                self.btn_7_p1.background_color=(1, 1, 1, .7)
                self.btn_8_p1.text ='u'
                self.btn_8_p1.background_color=(1, 1, 1, .7)
        elif len(foo_1) == 4:
            print('test')
            self.first_formula = foo_1
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_1_p2.text ='n'
                self.btn_1_p2.background_color=(1, 0, 0, .7)
                self.btn_5_p2.text ='n'
                self.btn_5_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_1_p2.text ='a'
                self.btn_1_p2.background_color=(0, 1, 0, .7)
                self.btn_5_p2.text ='a'
                self.btn_5_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_1_p2.text ='u'
                self.btn_1_p2.background_color=(1, 1, 1, .7)
                self.btn_5_p2.text ='u'
                self.btn_5_p2.background_color=(1, 1, 1, .7)
        elif len(foo_1) == 5:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_2_p2.text ='n'
                self.btn_2_p2.background_color=(1, 0, 0, .7)
                self.btn_6_p2.text ='n'
                self.btn_6_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_2_p2.text ='a'
                self.btn_2_p2.background_color=(0, 1, 0, .7)
                self.btn_6_p2.text ='a'
                self.btn_6_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_2_p2.text ='u'
                self.btn_2_p2.background_color=(1, 1, 1, .7)
                self.btn_6_p2.text ='u'
                self.btn_6_p2.background_color=(1, 1, 1, .7)
        elif len(foo_1) == 6:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_3_p2.text ='n'
                self.btn_3_p2.background_color=(1, 0, 0, .7)
                self.btn_7_p2.text ='n'
                self.btn_7_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_3_p2.text ='a'
                self.btn_3_p2.background_color=(0, 1, 0, .7)
                self.btn_7_p2.text ='a'
                self.btn_7_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_3_p2.text ='u'
                self.btn_3_p2.background_color=(1, 1, 1, .7)
                self.btn_7_p2.text ='u'
                self.btn_7_p2.background_color=(1, 1, 1, .7)
        elif len(foo_1) == 7:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_4_p2.text ='n'
                self.btn_4_p2.background_color=(1, 0, 0, .7)
                self.btn_8_p2.text ='n'
                self.btn_8_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_4_p2.text ='a'
                self.btn_4_p2.background_color=(0, 1, 0, .7)
                self.btn_8_p2.text ='a'
                self.btn_8_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_4_p2.text ='u'
                self.btn_4_p2.background_color=(1, 1, 1, .7)
                self.btn_8_p2.text ='u'
                self.btn_8_p2.background_color=(1, 1, 1, .7)
        if len(foo_1) == 8:
            self.second_formula = foo_1[4:8]
            self.btn_n.disabled = True
            self.btn_a.disabled = True
            self.btn_u.disabled = True
            self.click(button)
            foo_1.clear()

    def draw(self):
        self.line.points = [
            self.width*0.1,
            self.height*.7,
            self.width*0.2,
            self.height*.7
        ]

    def right_answer(self, button):
        right_label = Label(text='Right!', font_size= 35, size_hint=(.5, .3), pos_hint={'x': .25, 'y': .35})
        self.add_widget(right_label)

    def wrong_answer(self, button):
        wrong_label = Label(text='Wrong!', font_size=30, size_hint=(.5, .3), pos_hint={'x': .25, 'y': .25})
        self.add_widget(wrong_label)

    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active_advice.text = self.my_text_training_conclusion
        else:
            self.lbl_active_advice.text = "OFF"

    def on_checkbox_Active_2(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active_advice.text = self.advice_premises_and_conclusion
        else:
            self.lbl_active_advice.text = "OFF"

    def on_checkbox_Active_3(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active_example.text = self.syllogism_example_text
        else:
            self.lbl_active_example.text = "OFF"
        
    def on_checkbox_Active_4(self, checkboxInstance, isActive):
        if isActive:
            self.label_first_premis.text = self.premises_to_sentences_function_premis_one(self.my_text)
            self.label_second_premis.text = self.premises_to_sentences_function_premis_two(self.my_text2)
        else:
            self.label_first_premis.text = self.my_text
            self.label_second_premis.text = self.my_text2

    def premises_to_sentences_function_premis_one(self, my_text):
        if my_text == "MaP": # traditionelle Syllogistik
            premis_one_sentence = "All M are P"
        elif my_text == "MeP":
            premis_one_sentence = "No M are P"
        elif my_text == "MiP":
            premis_one_sentence = "Some M are P"
        elif my_text == "MoP":
            premis_one_sentence = "Some M are not P"
        elif my_text == "PaM":
            premis_one_sentence = "All P are M"
        elif my_text == "PeM":
            premis_one_sentence = "No P are M"
        elif my_text == "PiM":
            premis_one_sentence = "Some P are M"
        elif my_text == "PoM":
            premis_one_sentence = "Some P are not M"
        elif my_text == "MãP": # vervollständigte Syllogistik
            premis_one_sentence = "All P are M"
        elif my_text == "MëP":
            premis_one_sentence = "All not-M are P"
        elif my_text == "MïP":
            premis_one_sentence = "Some not-M are not P"
        elif my_text == "MõP":
            premis_one_sentence = "Some not-M are P"
        elif my_text == "PãM":
            premis_one_sentence = "All M are P"
        elif my_text == "PëM":
            premis_one_sentence = "All not-P are M"
        elif my_text == "PïM":
            premis_one_sentence = "Some not-P are not M"
        elif my_text == "PõM":
            premis_one_sentence = "Some not-P are M"
        return (premis_one_sentence)

    def premises_to_sentences_function_premis_two(self, my_text2):
        if my_text2 == "SaM": # traditionelle Syllogistik
            premis_two_sentence = "All S are M"
        elif my_text2 == "SeM":
            premis_two_sentence = "No S are M"
        elif my_text2 == "SiM":
            premis_two_sentence = "Some S are M"
        elif my_text2 == "SoM":
            premis_two_sentence = "Some S are not M"
        elif my_text2 == "MaS":
            premis_two_sentence = "All M are S"
        elif my_text2 == "MeS":
            premis_two_sentence = "No M are S"
        elif my_text2 == "MiS":
            premis_two_sentence = "Some M are S"
        elif my_text2 == "MoS":
            premis_two_sentence = "Some M are not S"
        elif my_text2 == "SãM": # vervollständigte Syllogistik
            premis_two_sentence = "All S are M"
        elif my_text2 == "SëM":
            premis_two_sentence = "All not-M are S"
        elif my_text2 == "SïM":
            premis_two_sentence = "Some not-M are not S"
        elif my_text2 == "SõM":
            premis_two_sentence = "Some not-M are S"
        elif my_text2 == "MãS":
            premis_two_sentence = "All S are M"
        elif my_text2 == "MëS":
            premis_two_sentence = "All not-M are S"
        elif my_text2 == "MïS":
            premis_two_sentence = "Some not-M are not S"
        elif my_text2 == "MõS":
            premis_two_sentence = "Some not-M are S"
        return (premis_two_sentence)

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def open_settings(self, *args):
        App.get_running_app().open_settings()

    def clear_widgets_function(self, *args):
        
        dummy = self.children[:]
        for child in dummy:
            if (child != self.active_4): #Checkbox Sentences remains
                self.remove_widget(child)
        
        foo_1.clear()
        
        self.menu_button = Button(text='Menu', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .9})
        self.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.settings_button = Button(text='Settings', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .7})
        self.add_widget(self.settings_button)
        self.settings_button.bind(on_press=self.open_settings)
        
        completedsyllogistic = self.function_completed_syllogistic_settings()#looks for setting
        particularpremis = self.function_particularpremis_settings()#looks for setting

        if completedsyllogistic == 1:
            a = random.randint(0, 15)
            b = random.randint(0, 15)
            if particularpremis == 0: 
                while (((a == 4) or (a == 5) or (a == 6) or (a == 7) or (a == 12) or (a == 13) or (a == 14) or (a == 15)) and ((b == 4) or (b == 5) or (b == 6) or (b == 7) or (b == 12) or (b == 13) or (b == 14) or (b == 15))):
                    a = random.randint(0, 15)
                    b = random.randint(0, 15)
            self.refresh2_button = Button(text='Generate!', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .8})
            self.add_widget(self.refresh2_button)
            self.refresh2_button.bind(on_press=lambda x:self.refresh_function(a, b))
        else:
            a = random.randint(0, 7)
            b = random.randint(0, 7)
            if particularpremis == 0:
                while (((a == 4) or (a == 5) or (a == 6) or (a == 7)) and ((b == 4) or (b == 5) or (b == 6) or (b == 7))):
                    a = random.randint(0, 7)
                    b = random.randint(0, 7)
            self.refresh2_button = Button(text='Generate!', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .8})
            self.add_widget(self.refresh2_button)
            self.refresh2_button.bind(on_press=lambda x:self.refresh_function(a, b))
        
        self.refresh2_button.bind(on_press=self.clear_widgets_function)
    
    def function_completed_syllogistic_settings(self, *args):
        config = ConfigParser.get_configparser('app')
        value = config.getint('trainer', 'completedsyllogistic')
        return value

    def function_particularpremis_settings(self, *args):
        config = ConfigParser.get_configparser('app')
        value = config.getint('trainer', 'particularpremis')
        return value

    def refresh_function_1(self, *args):
        a = args[0]
        b = args[1]

        self.active_4 = CheckBox(active=False)
        self.add_widget(self.active_4)
        self.active_4.bind(active=self.on_checkbox_Active_4)
        self.refresh_function(a, b)

    def refresh_function(self, *args):
        y = args[0]
        x = args[1]

        judges_premis_one = ["MaP", "MeP", "PaM", "PeM", "MiP", "MoP", "PiM", "PoM",  #traditionelle Syllogistik
                             "MãP", "MëP",  "PãM", "PëM", "MïP", "MõP","PïM", "PõM"]  #vervollständigte Syllogistik
        judges_premis_second = ["SaM", "SeM", "MaS", "MeS", "MiS", "MoS","SiM", "SoM", #traditionelle Syllogistik
                                "SãM", "SëM", "MãS", "MëS", "SïM", "SõM", "MïS", "MõS"] #vervollständigte Syllogistik
        
        second_formula = judges_premis_second[y]
        self.my_text2 = second_formula
        first_formula = judges_premis_one[x]
        self.my_text = first_formula

        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        
        function_output_list = self.output2(self.my_text, self.my_text2)
        #advices:
        self.my_text_training_conclusion = '  1. premis: ' + advice_premis_1[0] + '-' + advice_premis_1[0] + ' ' + \
                                          advice_premis_1[
                                              1] + '-' + advice_premis_1[1] + ' ' + advice_premis_1[2] + '-' + \
                                          advice_premis_1[2] + ' ' + advice_premis_1[
                                              3] + '-' + advice_premis_1[3] + "\n" + '  2. premis: ' + advice_premis_2[
                                              0] + ' ' + \
                                          advice_premis_2[1] + ' ' + advice_premis_2[2] + ' ' + advice_premis_2[3] + ',' + \
                                          advice_premis_2[0] + ' ' + advice_premis_2[1] + ' ' + advice_premis_2[2] + ' ' + \
                                          advice_premis_2[3]
        self.advice_premises_and_conclusion = '  1. premis: ' + advice_premis_1[0] + '-' + advice_premis_1[0] + ' ' + \
                                          advice_premis_1[
                                              1] + '-' + advice_premis_1[1] + ' ' + advice_premis_1[2] + '-' + \
                                          advice_premis_1[2] + ' ' + advice_premis_1[
                                              3] + '-' + advice_premis_1[3] + "\n" + '  2. premis: ' + advice_premis_2[
                                              0] + ' ' + \
                                          advice_premis_2[1] + ' ' + advice_premis_2[2] + ' ' + advice_premis_2[3] + ',' + \
                                          advice_premis_2[0] + ' ' + advice_premis_2[1] + ' ' + advice_premis_2[2] + ' ' + \
                                          advice_premis_2[3] + "\n" + '-------------------------------------------' + "\n" + 'conclusion: ' + function_output_list[3][0] + ' ' + function_output_list[3][1] + ' ' + function_output_list[3][0] + ' ' + function_output_list[3][1] + ' ' + function_output_list[3][2] + ' ' + function_output_list[3][3] + ' ' + function_output_list[3][2] + ' ' + function_output_list[3][3]
        
        syllogism_example_text = self.syllogism_example_function(self.my_text, self.my_text2, function_output_list[3])
        self.syllogism_example_text = syllogism_example_text

        self.label_first_premis = Label(text='', font_size= 30)
        self.label_second_premis = Label(text='', font_size= 30)
        self.label_questionmark = Label(text='?', font_size= 30)

        if self.active_4.active == True:
            self.label_first_premis.text = self.premises_to_sentences_function_premis_one(self.my_text)
            self.label_second_premis.text = self.premises_to_sentences_function_premis_two(self.my_text2)
        else:
            self.label_first_premis.text = self.my_text
            self.label_second_premis.text = self.my_text2        

        vertical = BoxLayout(orientation='vertical')
        self.add_widget(vertical)

        horizontal_up = BoxLayout(orientation='horizontal')
        vertical.add_widget(horizontal_up)

        vertical_left_up = BoxLayout(orientation='vertical')
        horizontal_up.add_widget(vertical_left_up)
        
        vertical_left_up.add_widget(self.label_first_premis)
        vertical_left_up.add_widget(self.label_second_premis)
        vertical_left_up.add_widget(self.label_questionmark)
        
        horizontal_up.add_widget(Label(text='Syllogism-\nTrainer', font_size= 35))
        
        self.boxlayout_up = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.boxlayout_up)

        self.checkboxes_BoxLayout = BoxLayout(orientation='horizontal')
        self.boxlayout_up.add_widget(self.checkboxes_BoxLayout)

        self.boxlayout_Checkbox_1 = BoxLayout(orientation='vertical')
        self.checkboxes_BoxLayout.add_widget(self.boxlayout_Checkbox_1)
        self.boxlayout_Checkbox_2 = BoxLayout(orientation='vertical')
        self.checkboxes_BoxLayout.add_widget(self.boxlayout_Checkbox_2)
        self.boxlayout_Checkbox_3 = BoxLayout(orientation='vertical')
        self.checkboxes_BoxLayout.add_widget(self.boxlayout_Checkbox_3)
        self.boxlayout_Checkbox_4 = BoxLayout(orientation='vertical')
        self.checkboxes_BoxLayout.add_widget(self.boxlayout_Checkbox_4)
        
        self.label_advice_1 = Label(text='Advice 1:', font_size= 25)
        self.label_advice_2 = Label(text='Advice 2:', font_size= 25)
        self.label_example = Label(text='Example:', font_size= 25)
        self.label_sentences = Label(text='Sentences', font_size= 25)
        
        self.active = CheckBox(active=False)
        self.active_2 = CheckBox(active=False)
        self.active_3 = CheckBox(active=False)

        self.checkbox_4_dummy_label = Label(text='', font_size= 25)

        self.boxlayout_Checkbox_1.add_widget(self.label_advice_1)
        self.boxlayout_Checkbox_1.add_widget(self.active)
        self.boxlayout_Checkbox_2.add_widget(self.label_advice_2)
        self.boxlayout_Checkbox_2.add_widget(self.active_2)
        self.boxlayout_Checkbox_3.add_widget(self.label_example)
        self.boxlayout_Checkbox_3.add_widget(self.active_3)
        self.boxlayout_Checkbox_4.add_widget(self.label_sentences)
        self.boxlayout_Checkbox_4.add_widget(self.checkbox_4_dummy_label)
        
        self.active_4.pos_hint = {'x': .825, 'y': .6} # not beautiful code
        self.active_4.size_hint = (.1, .1)
        
        self.active.bind(active=self.on_checkbox_Active)
        self.active_2.bind(active=self.on_checkbox_Active_2)
        self.active_3.bind(active=self.on_checkbox_Active_3)
    
        self.syllogism_box_col_1 = BoxLayout(orientation='vertical')
        vertical.add_widget(self.syllogism_box_col_1)
        
        self.syllogism_box_row_1 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_1)
                
        self.dummy_label_one = Label(text='', size_hint_x = 2.0)
        self.syllogism_box_row_1.add_widget(self.dummy_label_one)

        self.s1 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s1)
        self.s2 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s2)
        self.s3 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s3)
        self.s4 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s4)
        self.s5 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s5)
        self.s6 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s6)
        self.s7 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s7)
        self.s8 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s8)

        self.syllogism_box_row_2 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_2)
        
        self.dummy_label_two = Label(text='', size_hint_x = 2.0)
        self.syllogism_box_row_2.add_widget(self.dummy_label_two)

        self.m1 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m1)
        self.m2 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m2) 
        self.m3 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m3)
        self.m4 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m4)
        self.m5 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m5)
        self.m6 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m6)
        self.m7 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m7)
        self.m8 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m8)

        self.syllogism_box_row_3 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_3)
        
        self.dummy_label_three = Label(text='', size_hint_x = 2.0)
        self.syllogism_box_row_3.add_widget(self.dummy_label_three)

        self.p1 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p1)
        self.p2 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p2)
        self.p3 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p3)
        self.p4 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p4)
        self.p5 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p5)
        self.p6 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p6)
        self.p7 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p7)
        self.p8 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p8)

        self.syllogism_box_row_4 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_4)
        
        self.premis_one_label = Label(text='premis one', size_hint_x = 2.0)
        self.syllogism_box_row_4.add_widget(self.premis_one_label)

        self.btn_1_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_1_p1)
        self.btn_2_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_2_p1)
        self.btn_3_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_3_p1)
        self.btn_4_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_4_p1)
        self.btn_5_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_5_p1)
        self.btn_6_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_6_p1)
        self.btn_7_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_7_p1)
        self.btn_8_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_8_p1)

        self.syllogism_box_row_5 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_5)
        
        self.premis_two_label = Label(text='premis two', size_hint_x = 2.0)
        self.syllogism_box_row_5.add_widget(self.premis_two_label)

        self.btn_1_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_1_p2)
        self.btn_2_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_2_p2)
        self.btn_3_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_3_p2)
        self.btn_4_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_4_p2)
        self.btn_5_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_5_p2)
        self.btn_6_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_6_p2)
        self.btn_7_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_7_p2)
        self.btn_8_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_8_p2)
        
        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.conclusion_label = Label(text='conclusion', size_hint_x = 2.0)
        self.syllogism_box_row_6.add_widget(self.conclusion_label)

        self.btn_1_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_c)
        self.btn_2_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_c)
        self.btn_3_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_c)
        self.btn_4_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_c)
        self.btn_5_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_c)
        self.btn_6_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_c)
        self.btn_7_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_c)
        self.btn_8_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_c)
        
        self.answer_buttons_and_advices = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.answer_buttons_and_advices)

        self.answer_buttons = BoxLayout(orientation='vertical')
        self.answer_buttons_and_advices.add_widget(self.answer_buttons)
        
        self.button1 = Button()
        self.button2 = Button()
        self.button3 = Button()

        self.answer_buttons.add_widget(self.button1)
        self.answer_buttons.add_widget(self.button2)
        self.answer_buttons.add_widget(self.button3)

        self.buttons = [self.button1, self.button2, self.button3]
        correct_answer = random.randrange(len(self.buttons))
        print(correct_answer)

        print(function_output_list[3])
        button_text = function_output_list[0]
        
        completedsyllogistic = self.function_completed_syllogistic_settings()
        
        for i, button in enumerate(self.buttons):
            if i == correct_answer:
                button.text = button_text
                button.bind(on_press=self.right_answer)
            else:
                if completedsyllogistic == 1:
                    conclusion_judges = ["All S are P,\nalso known as SaP", "Some S are P,\nalso known as SiP", "No S is P,\nalso known as SeP", "Some S are no P,\nalso known as SoP", "No (allowed) \njudge possible!", # traditionelle Syllogistik
                                                 "All P are S,\nalso known as SãP", "No P is S,\nalso known as SëP", "Some ~S are ~P,\nalso known as SïP", "Some P are no S,\nalso known as SõP"] # vollständige Syllogistik
                    if button_text == "All S are P,\nalso known as SaP" or button_text == "All P are S,\nalso known as SãP":
                        for i, ele in enumerate(conclusion_judges):
                            if (ele == "Some S are P,\nalso known as SiP") or (ele == "Some ~S are ~P,\nalso known as SïP"):
                                conclusion_judges.pop(i)
                    elif button_text == "No S is P,\nalso known as SeP" or button_text == "No P is S,\nalso known as SëP":
                        for i, ele in enumerate(conclusion_judges):
                            if (ele == "Some S are no P,\nalso known as SoP") or (ele == "Some P are no S,\nalso known as SõP"):
                                conclusion_judges.pop(i)
                else:
                    conclusion_judges = ["All S are P,\nalso known as SaP", "Some S are P,\nalso known as SiP", "No S is P,\nalso known as SeP", "Some S are no P,\nalso known as SoP", "No (allowed) \njudge possible!"] # traditionelle Syllogistik
                    if button_text == "All S are P,\nalso known as SaP":
                        for i, ele in enumerate(conclusion_judges):
                            if (ele == "Some S are P,\nalso known as SiP"):
                                conclusion_judges.pop(i)
                    elif button_text == "No S is P,\nalso known as SeP":
                        for i, ele in enumerate(conclusion_judges):
                            if (ele == "Some S are no P,\nalso known as SoP"):
                                conclusion_judges.pop(i)
                conclusion_judges.remove(button_text)
                m = random.choice(conclusion_judges)
                button.text = m
                button.bind(on_press=self.wrong_answer)

        self.box_advices_and_example_BoxLayout = BoxLayout(orientation='vertical')
        self.answer_buttons_and_advices.add_widget(self.box_advices_and_example_BoxLayout)

        self.lbl_active_advice = Label(text="Advice OFF", font_size= 25)
        self.box_advices_and_example_BoxLayout.add_widget(self.lbl_active_advice)
            
        self.lbl_active_example = Label(text="Example OFF", font_size= 20)
        self.box_advices_and_example_BoxLayout.add_widget(self.lbl_active_example)

        self.box_horizontal_buttons_down = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.box_horizontal_buttons_down)

        self.btn_n = Button(text='n', background_normal='', background_color=(1, 0, 0, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_n)
        variable_btn_n ='n'
        self.btn_n.bind(on_press=self.append_function)

        self.btn_a = Button(text='a', background_normal='', background_color=(0, 1, 0, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_a)
        variable_btn_a ='a'
        self.btn_a.bind(on_press=self.append_function)

        self.btn_u = Button(text='u', background_normal='', background_color=(1, 1, 1, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_u)
        variable_btn_u ='u'
        self.btn_u.bind(on_press=self.append_function)
  
        self.refresh_button.bind(on_press=self.clear_widgets_function)

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def click(self,my_button2):
        my_text = self.first_formula
        first_formula = my_text
        my_text2 = self.second_formula
        second_formula = my_text2
        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        function_output_list = self.output2(my_text, my_text2)

        if function_output_list[4] == 1:
            self.conclusion_label.text = "Contradiction!"
        else:
            self.btn_1_c.text = function_output_list[3][0]
            self.btn_3_c.text = function_output_list[3][0]
            self.btn_2_c.text = function_output_list[3][1]
            self.btn_4_c.text = function_output_list[3][1]
            self.btn_5_c.text = function_output_list[3][2]
            self.btn_7_c.text = function_output_list[3][2]
            self.btn_6_c.text = function_output_list[3][3]
            self.btn_8_c.text = function_output_list[3][3]
            if function_output_list[3][0] == 'n':
                self.btn_1_c.background_color=(1, 0, 0, .7)
                self.btn_3_c.background_color=(1, 0, 0, .7)
            elif function_output_list[3][0] == 'a':
                self.btn_1_c.background_color=(0, 1, 0, .7)
                self.btn_3_c.background_color=(0, 1, 0, .7)
            elif function_output_list[3][0] == 'u':
                self.btn_1_c.background_color=(1, 1, 1, .7)
                self.btn_3_c.background_color=(1, 1, 1, .7)
            if function_output_list[3][1] == 'n':
                self.btn_2_c.background_color=(1, 0, 0, .7)
                self.btn_4_c.background_color=(1, 0, 0, .7)
            elif function_output_list[3][1] == 'a':
                self.btn_2_c.background_color=(0, 1, 0, .7)
                self.btn_4_c.background_color=(0, 1, 0, .7)
            elif function_output_list[3][1] == 'u':
                self.btn_2_c.background_color=(1, 1, 1, .7)
                self.btn_4_c.background_color=(1, 1, 1, .7)
            if function_output_list[3][2] == 'n':
                self.btn_5_c.background_color=(1, 0, 0, .7)
                self.btn_7_c.background_color=(1, 0, 0, .7)
            elif function_output_list[3][2] == 'a':
                self.btn_5_c.background_color=(0, 1, 0, .7)
                self.btn_7_c.background_color=(0, 1, 0, .7)
            elif function_output_list[3][2] == 'u':
                self.btn_5_c.background_color=(1, 1, 1, .7)
                self.btn_7_c.background_color=(1, 1, 1, .7)
            if function_output_list[3][3] == 'n':
                self.btn_6_c.background_color=(1, 0, 0, .7)
                self.btn_8_c.background_color=(1, 0, 0, .7)
            elif function_output_list[3][3] == 'a':
                self.btn_6_c.background_color=(0, 1, 0, .7)
                self.btn_8_c.background_color=(0, 1, 0, .7)
            elif function_output_list[3][3] == 'u':
                self.btn_6_c.background_color=(1, 1, 1, .7)
                self.btn_8_c.background_color=(1, 1, 1, .7)



    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        
        completedsyllogistic = self.function_completed_syllogistic_settings()
        particularpremis = self.function_particularpremis_settings()

        if completedsyllogistic == 1:
            a = random.randint(0, 15)
            b = random.randint(0, 15)
            if particularpremis == 0:
                while (((a == 4) or (a == 5) or (a == 6) or (a == 7) or (a == 12) or (a == 13) or (a == 14) or (a == 15)) and ((b == 4) or (b == 5) or (b == 6) or (b == 7) or (b == 12) or (b == 13) or (b == 14) or (b == 15))):
                    a = random.randint(0, 15)
                    b = random.randint(0, 15)
            self.refresh_button = Button(text='Generate!', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .8})
            self.add_widget(self.refresh_button)
            self.refresh_button.bind(on_press=lambda x:self.refresh_function_1(a, b))
        else:
            a = random.randint(0, 7)
            b = random.randint(0, 7)
            if particularpremis == 0:
                while (((a == 4) or (a == 5) or (a == 6) or (a == 7)) and ((b == 4) or (b == 5) or (b == 6) or (b == 7))):
                    a = random.randint(0, 7)
                    b = random.randint(0, 7)
            self.refresh_button = Button(text='Generate!', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .8})
            self.add_widget(self.refresh_button)
            self.refresh_button.bind(on_press=lambda x:self.refresh_function_1(a, b))

class Menu_conclusionsScreen(Screen):
    pass   

class ConclusionsScreen(Screen):
    global foo
    foo = []

    def syllogism_example_function(self, premis_one, premis_two, solution):
        if premis_one == "MaP" and premis_two == "SaM": # example-sentences - traditional syllogistic
            return ("Wenn alle Reptilien Wirbeltiere sind \nund alle Saurier Reptilien sind, \nso sind alle Saurier Wirbeltiere.")
        elif premis_one == "MeP" and premis_two == "SaM":
            return ("Wenn kein Mitglied der ural-altaischen Gruppe Indogermane ist \nund alle Ungarn zur ural-altaischen Gruppe gehören, \nist kein Ungar Indogermane.")
        elif premis_one == "MeP" and premis_two == "SiM":
            return ("Wenn kein Raucher gesund lebt \nund einige Jugendliche Raucher sind, \nso leben einige Jugendliche nicht gesund.")
        elif premis_one == "MaP" and premis_two == "SaM":
            return ("Wenn alle Unternehmer zur Gewerbesteuer veranlagt werden \nund alle Gastwirte Unternehmer sind, \nso werden einige Gastwirte zur Gewerbesteuer veranlagt.")
        elif premis_one == "MeP" and premis_two == "SaM":
            return ("Wenn kein Vogel ein Säugetier ist \nund alle Adler Vögel sind, \nso sind einige Adler keine Säugetiere.")
        elif premis_one == "PeM" and premis_two == "SaM":
            return ("Wenn kein rechtwinkeliges Rechteck gleichwinkelig ist \nund alle gleichseitigen Dreiecke gleichwinkelig sind, \nso ist kein gleichseitiges Dreieck rechtwinkelig.")
        elif premis_one == "PaM" and premis_two == "SeM":
            return ("Wenn kein Säugetier gefiedert ist \nund alle Nachtigallen gefiedert sind, \nso ist keine Nachtigall ein Säugetier.")
        elif premis_one == "PeM" and premis_two == "SiM":
            return ("Wenn kein Autofahrer blind ist \nund einige Raucher blind sind, \nso sind einige Raucher keine Autofahrer.")
        elif premis_one == "PaM" and premis_two == "SoM":
            return ("Wenn alle Letten Indogermanen sind \nund einige Balten keine Indogermanen sind, \nso sind einige Balten keine Letten.")
        elif premis_one == "PeM" and premis_two == "SaM":
            return ("Wenn kein Knollenblätterpilz essbar ist \nund alle Steinpilze essbar sind, \nso sind einige Steinpilze keine Knollenblätterpilze.")
        elif premis_one == "MaP" and premis_two == "MiS":
            return ("Wenn für alle Dreiecke gilt, \ndass sich ein Kreis so um sie beschreiben lässt, \ndass die Eckpunkte auf dem Kreis liegen \nund wenn für alle Dreiecke gilt, \ndass sich in sie ein Kreis so beschreiben lässt, \ndass er alle drei Seiten berührt, \nso lässt sich bei einigen Figuren, \nin die sich ein Kreis beschreiben lässt, \nauch ein Kreis um diese Figur beschreiben.")
        elif premis_one == "MiP" and premis_two == "MaS":
            return ("Wenn einige Koniferen Weimutskiefern sind \nund alle Koniferen Nadelgehölze, \nso sind einige Nadelgehölze Weimutskiefern.")
        elif premis_one == "MeP" and premis_two == "MiS":
            return ("Wenn kein Indogermane Eskimo ist \nund einige Indogermanen Grönländer sind, \nso sind einige Grönländer keine Eskimos.")
        elif premis_one == "MoP" and premis_two == "MaS":
            return ("Wenn einige Philosophen keine Dichter sind \nund alle Philosophen Denker sind, \nso sind einige Denker keine Dichter.")
        elif premis_one == "MeP" and premis_two == "MaS":
            return ("Wenn kein amtierender Staatsanwalt wegen Mordes verurteilt wurde, \nund alle amtierenden Staatsanwälte Beamte sind, \nso wurden einige Beamte nicht wegen Mordes verurteilt.")
        elif premis_one == "MaP" and premis_two == "MaS":
            return ("Wenn alle Getreidearten einjährig sind \nund alle Getreidearten Körner als Samen haben, \nso haben einige einjährige Pflanzen Körner als Samen.")
        elif premis_one == "PaM" and premis_two == "MeS":
            return ("Wenn alle Trinker ungesund leben \nund keiner, der ungesund lebt, Leistungssportler ist, \nso  ist kein Leistungssportler Trinker.")
        elif premis_one == "PiM" and premis_two == "MaS":
            return ("Wenn einige Professoren Physiker sind \nund alle Physiker Naturwissenschaftler sind, \nso sind einige Naturwissenschaftler Professoren.")
        elif premis_one == "PeM" and premis_two == "MiS":
            return ("Wenn kein anorganischer Stoff belebt ist \nund einiges belebte Bewusstsein hat, \nso ist einiges mit Bewusstsein kein anorganischer Stoff.")
        elif premis_one == "PaM" and premis_two == "MeS":
            return ("Wenn alle Autos Kraftfahrzeuge sind \nund kein Kraftfahrzeug ohne Bremse ist, \nso sind einige Fahrzeuge ohne Bremsen keine Autos.")
        elif premis_one == "PeM" and premis_two == "MaS":
            return ("Wenn keine Pflanze Bewusstsein hat \nund alles mit Bewusstsein ein Lebewesen ist, \nso sind einige Lebewesen keine Pflanzen.")
        elif premis_one == "PaM" and premis_two == "MaS":
            return ("Wenn alle Quadrate Rechtecke sind \nund alle Rechtecke Trapeze sind, \nso sind einige Trapeze Quadrate.")
        elif premis_one == "MëP" and premis_two == "SeM":  # example-sentences - completed syllogistic (page 127 - Einführung in die formale Logik)
            return ("Wenn alle Nicht-Mitglieder doppelten EIntritt bezahlen und \keine Frau Mitglied ist, \so bezahlen alle Frauen doppelten Eintritt.")
        elif premis_one == "MaP" and premis_two == "SëM":
            return ("Wenn alle weniger Krebsgefährdeten eine längere Lebenserwartung haben \nund alle Nichtraucher weniger Krebsgefährdete sind, \nso haben alle Nichtraucher eine längere Lebenserwartung.")
        elif premis_one == "MãP" and premis_two == "SeM":
            return ("Wenn alle ungeraden Zahlen keine vollkommenen Zahlen sind \nund keine Potenz von drei gerade ist, \nso ist keine Potenz von drei eine vollkommene Zahl.")
        elif premis_one == "MãP" and premis_two == "SãM":
            return ("Wenn kein Nicht-Mitglied Vorsitzender werden kann \nund kein Nicht-Schwimmer Mitglied ist, \nso kann kein Nicht-Schwimmer Vorsitzender werden.")
        elif premis_one == "MëP" and premis_two == "SãM":
            return ("Wenn alle Nicht-Akademiker schlechtere Beförderungschancen haben \nund alle, die keine höhere Schule besuchten, keine Akademiker sind, \nso haben alle, die keine höhere Schule besuchten, \nschlechtere Beförderungsaussichten.")
        elif premis_one == "MeP" and premis_two == "SëM":
            return ("Wenn alle Primzahlen keine Quadratzahlen sind \nund nicht teilbare Zahlen Primzahlen sind, \nso sind nicht teilbare Zahlen keine Quadratzahlen.")
        elif premis_one == "MeP" and premis_two == "SeM":
            return ("Wenn kein Dreieck ein Viereck ist, \nso sind einige Nicht-Quadrate keine Vierecke.")
        else:
            return ("Kein kategorisches Urteil! oder kein Beispielsatz...")

    def first_formula_values(self, first_formula):
        if first_formula == "MaP": # traditionelle Syllogistik
            first_formula = "auna"
        elif first_formula == "MeP":
            first_formula = "naau"
        elif first_formula == "MiP":
            first_formula = "auuu"
        elif first_formula == "MoP":
            first_formula = "uuau"
        elif first_formula == "PaM":
            first_formula = "anua"
        elif first_formula == "PeM":
            first_formula = "naau"
        elif first_formula == "PiM":
            first_formula = "auuu"
        elif first_formula == "PoM":
            first_formula = "uauu"
        elif first_formula == "MãP": # vervollständigte Syllogistik
            first_formula = "anua"
        elif first_formula == "MëP":
            first_formula = "uaan"
        elif first_formula == "MïP":
            first_formula = "uuua"
        elif first_formula == "MõP":
            first_formula = "uauu"
        elif first_formula == "PãM":
            first_formula = "auna"
        elif first_formula == "PëM":
            first_formula = "uaan"
        elif first_formula == "PïM":
            first_formula = "uuua"
        elif first_formula == "PõM":
            first_formula = "uuau"
        return (first_formula)

    def second_formula_values(self, second_formula):
        if second_formula == "SaM": # traditionelle Syllogistik
            second_formula = "auna"
        elif second_formula == "SeM":
            second_formula = "naau"
        elif second_formula == "SiM":
            second_formula = "auuu"
        elif second_formula == "SoM":
            second_formula = "uuau"
        elif second_formula == "MaS":
            second_formula = "anua"
        elif second_formula == "MeS":
            second_formula = "naau"
        elif second_formula == "MiS":
            second_formula = "auuu"
        elif second_formula == "MoS":
            second_formula = "uauu"
        elif second_formula == "SãM": # vervollständigte Syllogistik
            second_formula = "anua"
        elif second_formula == "SëM":
            second_formula = "uaan"
        elif second_formula == "SïM":
            second_formula = "uuua"
        elif second_formula == "SõM":
            second_formula = "uauu"
        elif second_formula == "MãS":
            second_formula = "auna"
        elif second_formula == "MëS":
            second_formula = "uaan"
        elif second_formula == "MïS":
            second_formula = "uuua"
        elif second_formula == "MõS":
            second_formula = "uuau"
        return (second_formula)

    def syllogism_deduction_first_value_n(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of first value
            return ("n")
        elif second_formula[0] == "n" and first_formula[1] == "n":
            return ("n")
        elif first_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        else:  # calculates potential "u"-values of first value
            return ("u")

    def syllogism_deduction_first_value_a(self, first_formula, second_formula):
        if first_formula[0] == "a" and second_formula[1] == "n" and second_formula[
            0] == "n":  # calculates potential "a"-values of first value
            return ("a")
        elif second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
            return ("a")
        else:  # calculates potential "u"-values of first value
            return ("u")

    def syllogism_deduction_second_value_n(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of second value
            return ("n")
        elif second_formula[1] == "n" and first_formula[1] == "n":
            return ("n")
        elif first_formula[0] == "n" and second_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            return ("n")
        else:  # calculates potential "u"-values of second value
            return ("u")

    def syllogism_deduction_second_value_a(self, first_formula, second_formula):
        if first_formula[0] == "a" and second_formula[0] == "n" and second_formula[1] == "n":  # calculates potential "a"-values of second value
            return ("a")
        elif second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
            return ("a")
        else:  # calculates potential "u"-values of second value
            return ("u")

    def syllogism_deduction_third_value_n(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            return ("n")
        elif second_formula[0] == "n" and first_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "n" and second_formula[2] == "n":
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        else:
            return ("u")

    def syllogism_deduction_third_value_a(self, first_formula, second_formula):
        if first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] == "n":
            return ("a")
        elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
            return ("a")
        else:
            return ("u")

    def syllogism_deduction_fourth_value_n(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and first_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "n" and second_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            return ("n")
        else:
            return ("u")

    def syllogism_deduction_fourth_value_a(self, first_formula, second_formula):
        if first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] == "n":
            return ("a")
        elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
            return ("a")
        else:
            return ("u")

    def syllogism_contradiction_test(self, first_formula, second_formula):
        conclusion = [0, 0, 0, 0, 0, 0, 0, 0]
        conclusion[0] = self.syllogism_deduction_first_value_n(first_formula, second_formula)
        conclusion[1] = self.syllogism_deduction_first_value_a(first_formula, second_formula)
        if conclusion[0] == 'n' and conclusion[1] == 'a':
            print('first error at 0')
            return (1)
        conclusion[2] = self.syllogism_deduction_second_value_n(first_formula, second_formula)
        conclusion[3] = self.syllogism_deduction_second_value_a(first_formula, second_formula)
        if conclusion[2] == 'n' and conclusion[3] == 'a':
            print('first error at 1')
            return (1)
        conclusion[4] = self.syllogism_deduction_third_value_n(first_formula, second_formula)
        conclusion[5] = self.syllogism_deduction_third_value_a(first_formula, second_formula)
        if conclusion[4] == 'n' and conclusion[5] == 'a':
            print('first error at 2')
            return (1)
        conclusion[6] = self.syllogism_deduction_fourth_value_n(first_formula, second_formula)
        conclusion[7] = self.syllogism_deduction_fourth_value_a(first_formula, second_formula)
        if conclusion[6] == 'n' and conclusion[7] == 'a':
            print('first error at 3')
            return (1)
        else:
            return (0)

    def syllogism_deduction_first_value(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of first value
            return ("n")
        elif second_formula[0] == "n" and first_formula[1] == "n":
            return ("n")
        elif first_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        elif first_formula[0] == "a" and second_formula[1] == "n" and second_formula[
            0] != "n":  # calculates potential "a"-values of first value
            return ("a")
        elif second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] != "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] != "n":
            return ("a")
        else:  # calculates potential "u"-values of first value
            return ("u")

    def syllogism_deduction_second_value(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of second value
            return ("n")
        elif second_formula[1] == "n" and first_formula[1] == "n":
            return ("n")
        elif first_formula[0] == "n" and second_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            return ("n")
        elif first_formula[0] == "a" and second_formula[0] == "n" and second_formula[
            1] != "n":  # calculates potential "a"-values of second value
            return ("a")
        elif second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] != "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] != "n":
            return ("a")
        else:  # calculates potential "u"-values of second value
            return ("u")

    def syllogism_deduction_third_value(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            return ("n")
        elif second_formula[0] == "n" and first_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "n" and second_formula[2] == "n":
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            return ("n")
        elif first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] != "n":
            return ("a")
        elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
            return ("a")
        else:
            return ("u")

    def syllogism_deduction_fourth_value(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and first_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "n" and second_formula[3] == "n":
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            return ("n")
        elif first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] != "n":
            return ("a")
        elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
            return ("a")
        else:
            return ("u")

    def syllogism_solution(self,first_formula, second_formula):
        conclusion = [0, 0, 0, 0]
        conclusion[0] = self.syllogism_deduction_first_value(first_formula, second_formula)
        conclusion[1] = self.syllogism_deduction_second_value(first_formula, second_formula)
        conclusion[2] = self.syllogism_deduction_third_value(first_formula, second_formula)
        conclusion[3] = self.syllogism_deduction_fourth_value(first_formula, second_formula)
        return (conclusion)

    def output(self, solution):
        if solution == ["a", "u", "n", "a"]: # traditionelle Syllogistik
            return "All S are P,\nalso known as SaP"
        elif solution == ["a", "u", "u", "u"]:
            return "Some S are P,\nalso known as SiP"
        elif solution == ["n", "a", "a", "u"]:
            return "No S is P,\nalso known as SeP"
        elif solution == ["u", "u", "a", "u"]:
            return "Some S are no P,\nalso known as SoP"
        elif solution == ["a", "n", "u", "a"]: # vervollständigte Syllogistik
            return "All P are S,\nalso known as SãP"
        elif solution == ["u", "a", "a", "n"]:
            return "No P is S,\nalso known as SëP"
        elif solution == ["u", "u", "u", "a"]:
            return "Some ~S are ~P,\nalso known as SïP"
        elif solution == ["u", "a", "u", "u"]:
            return "Some P are no S,\nalso known as SõP"
        else:
            return ("No traditional\njudge!")

    def output2(self, my_text, my_text2):
        first_formula = my_text
        second_formula = my_text2
        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        solution = self.syllogism_solution(advice_premis_1, advice_premis_2)
        output_ = self.output(solution)
        result_contradiction_test = self.syllogism_contradiction_test(advice_premis_1, advice_premis_2)
        return [output_, advice_premis_1, advice_premis_2, solution, result_contradiction_test]

    def append_function(self, button):
        print(button)
        if foo == []:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_1_p1.text ='n'
                self.btn_1_p1.background_color=(1, 0, 0, .7)
                self.btn_2_p1.text ='n'
                self.btn_2_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_1_p1.text ='a'
                self.btn_1_p1.background_color=(0, 1, 0, .7)
                self.btn_2_p1.text ='a'
                self.btn_2_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_1_p1.text ='u'
                self.btn_1_p1.background_color=(1, 1, 1, .7)
                self.btn_2_p1.text ='u'
                self.btn_2_p1.background_color=(1, 1, 1, .7)
        elif len(foo) == 1:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_3_p1.text ='n'
                self.btn_3_p1.background_color=(1, 0, 0, .7)
                self.btn_4_p1.text ='n'
                self.btn_4_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_3_p1.text ='a'
                self.btn_3_p1.background_color=(0, 1, 0, .7)
                self.btn_4_p1.text ='a'
                self.btn_4_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_3_p1.text ='u'
                self.btn_3_p1.background_color=(1, 1, 1, .7)
                self.btn_4_p1.text ='u'
                self.btn_4_p1.background_color=(1, 1, 1, .7)
        elif len(foo) == 2:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_5_p1.text ='n'
                self.btn_5_p1.background_color=(1, 0, 0, .7)
                self.btn_6_p1.text ='n'
                self.btn_6_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_5_p1.text ='a'
                self.btn_5_p1.background_color=(0, 1, 0, .7)
                self.btn_6_p1.text ='a'
                self.btn_6_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_5_p1.text ='u'
                self.btn_5_p1.background_color=(1, 1, 1, .7)
                self.btn_6_p1.text ='u'
                self.btn_6_p1.background_color=(1, 1, 1, .7)
        elif len(foo) == 3:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_7_p1.text ='n'
                self.btn_7_p1.background_color=(1, 0, 0, .7)
                self.btn_8_p1.text ='n'
                self.btn_8_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_7_p1.text ='a'
                self.btn_7_p1.background_color=(0, 1, 0, .7)
                self.btn_8_p1.text ='a'
                self.btn_8_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_7_p1.text ='u'
                self.btn_7_p1.background_color=(1, 1, 1, .7)
                self.btn_8_p1.text ='u'
                self.btn_8_p1.background_color=(1, 1, 1, .7)
        elif len(foo) == 4:
            print('test')
            self.first_formula = foo
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_1_p2.text ='n'
                self.btn_1_p2.background_color=(1, 0, 0, .7)
                self.btn_5_p2.text ='n'
                self.btn_5_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_1_p2.text ='a'
                self.btn_1_p2.background_color=(0, 1, 0, .7)
                self.btn_5_p2.text ='a'
                self.btn_5_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_1_p2.text ='u'
                self.btn_1_p2.background_color=(1, 1, 1, .7)
                self.btn_5_p2.text ='u'
                self.btn_5_p2.background_color=(1, 1, 1, .7)
        elif len(foo) == 5:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_2_p2.text ='n'
                self.btn_2_p2.background_color=(1, 0, 0, .7)
                self.btn_6_p2.text ='n'
                self.btn_6_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_2_p2.text ='a'
                self.btn_2_p2.background_color=(0, 1, 0, .7)
                self.btn_6_p2.text ='a'
                self.btn_6_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_2_p2.text ='u'
                self.btn_2_p2.background_color=(1, 1, 1, .7)
                self.btn_6_p2.text ='u'
                self.btn_6_p2.background_color=(1, 1, 1, .7)
        elif len(foo) == 6:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_3_p2.text ='n'
                self.btn_3_p2.background_color=(1, 0, 0, .7)
                self.btn_7_p2.text ='n'
                self.btn_7_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_3_p2.text ='a'
                self.btn_3_p2.background_color=(0, 1, 0, .7)
                self.btn_7_p2.text ='a'
                self.btn_7_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_3_p2.text ='u'
                self.btn_3_p2.background_color=(1, 1, 1, .7)
                self.btn_7_p2.text ='u'
                self.btn_7_p2.background_color=(1, 1, 1, .7)
        elif len(foo) == 7:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_4_p2.text ='n'
                self.btn_4_p2.background_color=(1, 0, 0, .7)
                self.btn_8_p2.text ='n'
                self.btn_8_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_4_p2.text ='a'
                self.btn_4_p2.background_color=(0, 1, 0, .7)
                self.btn_8_p2.text ='a'
                self.btn_8_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_4_p2.text ='u'
                self.btn_4_p2.background_color=(1, 1, 1, .7)
                self.btn_8_p2.text ='u'
                self.btn_8_p2.background_color=(1, 1, 1, .7)
        if len(foo) == 8:
            self.second_formula = foo[4:8]
            self.btn_n.disabled = True
            self.btn_a.disabled = True
            self.btn_u.disabled = True
            self.click(button)
            foo.clear()

    def refresh_function(self, button):
        horizontal = BoxLayout(orientation='horizontal')
        self.add_widget(horizontal)
        
        self.label_1 = Label(font_size= 20, size_hint_x = .5)
        horizontal.add_widget(self.label_1)
        
        vertical = BoxLayout(orientation='vertical')
        horizontal.add_widget(vertical)
        
        self.boxlayout_up = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.boxlayout_up)
    
        self.syllogism_box_col_1 = BoxLayout(orientation='vertical')
        vertical.add_widget(self.syllogism_box_col_1)
        
        self.syllogism_box_row_1 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_1)
        
        self.dummy_label_one = Label(text='', size_hint_x = 2.0)
        self.syllogism_box_row_1.add_widget(self.dummy_label_one)

        self.s1 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s1)
        self.s2 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s2)
        self.s3 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s3)
        self.s4 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s4)
        self.s5 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s5)
        self.s6 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s6)
        self.s7 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s7)
        self.s8 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s8)

        self.syllogism_box_row_2 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_2)
        
        self.dummy_label_two = Label(text='', size_hint_x = 2.0)
        self.syllogism_box_row_2.add_widget(self.dummy_label_two)

        self.m1 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m1)
        self.m2 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m2) 
        self.m3 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m3)
        self.m4 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m4)
        self.m5 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m5)
        self.m6 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m6)
        self.m7 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m7)
        self.m8 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m8)

        self.syllogism_box_row_3 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_3)
        
        self.dummy_label_three = Label(text='', size_hint_x = 2.0)
        self.syllogism_box_row_3.add_widget(self.dummy_label_three)

        self.p1 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p1)
        self.p2 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p2)
        self.p3 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p3)
        self.p4 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p4)
        self.p5 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p5)
        self.p6 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p6)
        self.p7 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p7)
        self.p8 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p8)

        self.syllogism_box_row_4 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_4)
        
        self.premis_one_label = Label(text='premis one', size_hint_x = 2.0)
        self.syllogism_box_row_4.add_widget(self.premis_one_label)

        self.btn_1_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_1_p1)
        self.btn_2_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_2_p1)
        self.btn_3_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_3_p1)
        self.btn_4_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_4_p1)
        self.btn_5_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_5_p1)
        self.btn_6_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_6_p1)
        self.btn_7_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_7_p1)
        self.btn_8_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_8_p1)

        self.syllogism_box_row_5 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_5)
        
        self.premis_two_label = Label(text='premis two', size_hint_x = 2.0)
        self.syllogism_box_row_5.add_widget(self.premis_two_label)

        self.btn_1_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_1_p2)
        self.btn_2_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_2_p2)
        self.btn_3_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_3_p2)
        self.btn_4_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_4_p2)
        self.btn_5_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_5_p2)
        self.btn_6_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_6_p2)
        self.btn_7_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_7_p2)
        self.btn_8_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_8_p2)
        
        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.conclusion_label = Label(text='conclusion', size_hint_x = 2.0)
        self.syllogism_box_row_6.add_widget(self.conclusion_label)

        self.btn_1_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_c)
        self.btn_2_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_c)
        self.btn_3_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_c)
        self.btn_4_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_c)
        self.btn_5_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_c)
        self.btn_6_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_c)
        self.btn_7_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_c)
        self.btn_8_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_c)

        self.syllogism_box_col_2 = BoxLayout(orientation='vertical')
        vertical.add_widget(self.syllogism_box_col_2)

        self.label_5 = Label(font_size= 20)
        vertical.add_widget(self.label_5)

        self.box_horizontal_buttons_down = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.box_horizontal_buttons_down)

        self.btn_n = Button(text='n', background_normal='', background_color=(1, 0, 0, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_n)
        variable_btn_n ='n'
        self.btn_n.bind(on_press=self.append_function)

        self.btn_a = Button(text='a', background_normal='', background_color=(0, 1, 0, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_a)
        variable_btn_a ='a'
        self.btn_a.bind(on_press=self.append_function)

        self.btn_u = Button(text='u', background_normal='', background_color=(1, 1, 1, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_u)
        variable_btn_u ='u'
        self.btn_u.bind(on_press=self.append_function)

        self.label_3 = Label(font_size= 20, size_hint_x = .5)
        horizontal.add_widget(self.label_3)
        


        self.refresh_button.bind(on_press=self.clear_widgets_function)

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def clear_widgets_function(self, *args):
        self.clear_widgets()
        foo.clear()
        
        self.refresh2_button = Button(text='Generate!', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .8})
        self.add_widget(self.refresh2_button)
        
        self.menu_button = Button(text='Menu', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .9})
        self.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.refresh2_button.bind(on_press=self.refresh_function)
        
        self.refresh2_button.bind(on_press=self.clear_widgets_function)

    def __init__(self,**kwargs):
        super (ConclusionsScreen,self).__init__(**kwargs)
        
        self.refresh_button = Button(text='Generate!', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .8})
        self.add_widget(self.refresh_button)
        self.refresh_button.bind(on_press=self.refresh_function)

    def click(self,my_button2):
        my_text = self.first_formula
        first_formula = my_text
        my_text2 = self.second_formula
        second_formula = my_text2
        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        function_output_list = self.output2(my_text, my_text2)
        self.advice_premises_and_conclusion = '  1. premis: ' + advice_premis_1[0] + '-' + advice_premis_1[0] + ' ' + \
                                      advice_premis_1[
                                          1] + '-' + advice_premis_1[1] + ' ' + advice_premis_1[2] + '-' + \
                                      advice_premis_1[2] + ' ' + advice_premis_1[
                                          3] + '-' + advice_premis_1[3] + "\n" + '  2. premis: ' + advice_premis_2[
                                          0] + ' ' + \
                                      advice_premis_2[1] + ' ' + advice_premis_2[2] + ' ' + advice_premis_2[3] + ',' + \
                                      advice_premis_2[0] + ' ' + advice_premis_2[1] + ' ' + advice_premis_2[2] + ' ' + \
                                      advice_premis_2[3] + "\n" + '-------------------------------------------' + "\n" + 'conclusion: ' + function_output_list[3][0] + ' ' + function_output_list[3][1] + ' ' + function_output_list[3][0] + ' ' + function_output_list[3][1] + ' ' + function_output_list[3][2] + ' ' + function_output_list[3][3] + ' ' + function_output_list[3][2] + ' ' + function_output_list[3][3]

        if function_output_list[4] == 1:
            self.conclusion_label.text = "Contradiction!"
        else:
            self.btn_1_c.text = function_output_list[3][0]
            self.btn_3_c.text = function_output_list[3][0]
            self.btn_2_c.text = function_output_list[3][1]
            self.btn_4_c.text = function_output_list[3][1]
            self.btn_5_c.text = function_output_list[3][2]
            self.btn_7_c.text = function_output_list[3][2]
            self.btn_6_c.text = function_output_list[3][3]
            self.btn_8_c.text = function_output_list[3][3]
            if function_output_list[3][0] == 'n':
                self.btn_1_c.background_color=(1, 0, 0, .7)
                self.btn_3_c.background_color=(1, 0, 0, .7)
            elif function_output_list[3][0] == 'a':
                self.btn_1_c.background_color=(0, 1, 0, .7)
                self.btn_3_c.background_color=(0, 1, 0, .7)
            elif function_output_list[3][0] == 'u':
                self.btn_1_c.background_color=(1, 1, 1, .7)
                self.btn_3_c.background_color=(1, 1, 1, .7)
            if function_output_list[3][1] == 'n':
                self.btn_2_c.background_color=(1, 0, 0, .7)
                self.btn_4_c.background_color=(1, 0, 0, .7)
            elif function_output_list[3][1] == 'a':
                self.btn_2_c.background_color=(0, 1, 0, .7)
                self.btn_4_c.background_color=(0, 1, 0, .7)
            elif function_output_list[3][1] == 'u':
                self.btn_2_c.background_color=(1, 1, 1, .7)
                self.btn_4_c.background_color=(1, 1, 1, .7)
            if function_output_list[3][2] == 'n':
                self.btn_5_c.background_color=(1, 0, 0, .7)
                self.btn_7_c.background_color=(1, 0, 0, .7)
            elif function_output_list[3][2] == 'a':
                self.btn_5_c.background_color=(0, 1, 0, .7)
                self.btn_7_c.background_color=(0, 1, 0, .7)
            elif function_output_list[3][2] == 'u':
                self.btn_5_c.background_color=(1, 1, 1, .7)
                self.btn_7_c.background_color=(1, 1, 1, .7)
            if function_output_list[3][3] == 'n':
                self.btn_6_c.background_color=(1, 0, 0, .7)
                self.btn_8_c.background_color=(1, 0, 0, .7)
            elif function_output_list[3][3] == 'a':
                self.btn_6_c.background_color=(0, 1, 0, .7)
                self.btn_8_c.background_color=(0, 1, 0, .7)
            elif function_output_list[3][3] == 'u':
                self.btn_6_c.background_color=(1, 1, 1, .7)
                self.btn_8_c.background_color=(1, 1, 1, .7)

class Menu_total_formulas_Screen(Screen):
    pass

class Total_formulas_QuizScreen(Screen):
    global foo_3
    foo_3 = []
    
    def input_first_formula(self):
        first_formula = input("First logical formula:")
        if first_formula == "MaP":
            first_formula = "auna"
        elif first_formula == "MeP":
            first_formula = "naau"
        elif first_formula == "MiP":
            first_formula = "auuu"
        elif first_formula == "MoP":
            first_formula = "uuau"
        elif first_formula == "PaM":
            first_formula = "anua"
        elif first_formula == "PeM":
            first_formula = "naau"
        elif first_formula == "PiM":
            first_formula = "auuu"
        elif first_formula == "PoM":
            first_formula = "uauu"
        return(first_formula)
        
    def input_second_formula(self):
        second_formula = input("Second logical formula:")
        if second_formula == "SaM":
            second_formula = "auna"
        elif second_formula == "SeM":
            second_formula = "naau"
        elif second_formula == "SiM":
            second_formula = "auuu"
        elif second_formula == "SoM":
            second_formula = "uuau"
        elif second_formula == "MaS":
            second_formula = "anua"
        elif second_formula == "MeS":
            second_formula = "naau"
        elif second_formula == "MiS":
            second_formula = "auuu"
        elif second_formula == "MoS":
            second_formula = "uauu"
        return(second_formula)

    def input_third_formula(self):
        third_formula = input("Third logical formula:")
        if third_formula == "SaP":
            third_formula = "auna"
        elif third_formula == "SeP":
            third_formula = "naau"
        elif third_formula == "SiP":
            third_formula = "auuu"
        elif third_formula == "SoP":
            third_formula = "uuau"
        elif third_formula == "PaS":
            third_formula = "anua"
        elif third_formula == "PeS":
            third_formula = "naau"
        elif third_formula == "PiS":
            third_formula = "auuu"
        elif third_formula == "PoS":
            third_formula = "uauu"
        return(third_formula)


    def total_formula_deduction_first_value_n(self, first_formula,second_formula,third_formula):
        if first_formula[0] == "n":    #caluculates potential "n"-values of first value
            return("n")
        elif second_formula[0] == "n":
            return("n")
        elif third_formula[0] == "n":
            return("n")
        else: #calculates potential "u"-values of first value
            return("u")

    def total_formula_deduction_first_value_a(self, first_formula,second_formula,third_formula):
        if first_formula[0] == "a" and second_formula[1] == "n":    #calculates potential "a"-values of first value
            return("a")
        elif first_formula[0] == "a" and third_formula[1] == "n":
            return("a")
        elif second_formula[0] == "a" and first_formula[2] == "n":
            return("a")
        elif second_formula[0] == "a" and third_formula[2] == "n":
            return("a")
        elif third_formula[0] == "a" and first_formula[1] == "n":
            return("a")
        elif third_formula[0] == "a" and second_formula[2] == "n":
            return("a")
        else: #calculates potential "u"-values of first value
            return("u")

    def total_formula_deduction_second_value_n(self, first_formula,second_formula,third_formula):
        if first_formula[0] == "n":    #caluculates potential "n"-values of second value
            return("n")
        elif second_formula[1] == "n":
            return("n")
        elif third_formula[1] == "n":
            return("n")
        else: #calculates potential "u"-values of second value
            return("u")

    def total_formula_deduction_second_value_a(self, first_formula,second_formula,third_formula):
        if first_formula[0] == "a" and second_formula[0] == "n":    #calculates potential "a"-values of second value
            return("a")
        elif first_formula[0] == "a" and third_formula[0] == "n":
            return("a")
        elif second_formula[1] == "a" and first_formula[2] == "n":
            return("a")
        elif second_formula[1] == "a" and third_formula[3] == "n":
            return("a")
        elif third_formula[1] == "a" and first_formula[1] == "n":
            return("a")
        elif third_formula[1] == "a" and second_formula[3] == "n":
            return("a")
        else: #calculates potential "u"-values of second value
            return("u")

    def total_formula_deduction_third_value_n(self, first_formula,second_formula,third_formula):
        if first_formula[1] == "n":    #caluculates potential "n"-values of third value
            return("n")
        elif second_formula[2] == "n":
            return("n")
        elif third_formula[0] == "n":
            return("n")
        else: #calculates potential "u"-values of third value
            return("u")

    def total_formula_deduction_third_value_a(self, first_formula,second_formula,third_formula):
        if first_formula[1] == "a" and second_formula[3] == "n":    #calculates potential "a"-values of third value
            return("a")
        elif first_formula[1] == "a" and third_formula[1] == "n":
            return("a")
        elif second_formula[2] == "a" and first_formula[3] == "n":
            return("a")
        elif second_formula[2] == "a" and third_formula[2] == "n":
            return("a")
        elif third_formula[0] == "a" and first_formula[0] == "n":
            return("a")
        elif third_formula[0] == "a" and second_formula[0] == "n":
            return("a")
        else: #calculates potential "u"-values of third value
            return("u")

    def total_formula_deduction_fourth_value_n(self, first_formula,second_formula,third_formula):
        if first_formula[1] == "n":    #caluculates potential "n"-values of fourth value
            return("n")
        elif second_formula[3] == "n":
            return("n")
        elif third_formula[1] == "n":
            return("n")
        else: #calculates potential "u"-values of fourth value
            return("u")

    def total_formula_deduction_fourth_value_a(self, first_formula,second_formula,third_formula):
        if first_formula[1] == "a" and second_formula[2] == "n":    #calculates potential "a"-values of fourth value
            return("a")
        elif first_formula[1] == "a" and third_formula[0] == "n":
            return("a")
        elif second_formula[3] == "a" and first_formula[3] == "n":
            return("a")
        elif second_formula[3] == "a" and third_formula[3] == "n":
            return("a")
        elif third_formula[1] == "a" and first_formula[0] == "n":
            return("a")
        elif third_formula[1] == "a" and second_formula[1] == "n":
            return("a")
        else: #calculates potential "u"-values of fourth value
            return("u")

    def total_formula_deduction_fifth_value_n(self, first_formula,second_formula,third_formula):
        if first_formula[2] == "n":    #caluculates potential "n"-values of fifth value
            return("n")
        elif second_formula[0] == "n":
            return("n")
        elif third_formula[2] == "n":
            return("n")
        else: #calculates potential "u"-values of fifth value
            return("u")

    def total_formula_deduction_fifth_value_a(self, first_formula,second_formula,third_formula):
        if first_formula[2] == "a" and second_formula[1] == "n":    #calculates potential "a"-values of fifth value
            return("a")
        elif first_formula[2] == "a" and third_formula[3] == "n":
            return("a")
        elif second_formula[0] == "a" and first_formula[0] == "n":
            return("a")
        elif second_formula[0] == "a" and third_formula[0] == "n":
            return("a")
        elif third_formula[2] == "a" and first_formula[3] == "n":
            return("a")
        elif third_formula[2] == "a" and second_formula[2] == "n":
            return("a")
        else: #calculates potential "u"-values of fifth value
            return("u")

    def total_formula_deduction_sixth_value_n(self, first_formula,second_formula,third_formula):
        if first_formula[2] == "n":    #caluculates potential "n"-values of sixth value
            return("n")
        elif second_formula[1] == "n":
            return("n")
        elif third_formula[3] == "n":
            return("n")
        else: #calculates potential "u"-values of sixth value
            return("u")

    def total_formula_deduction_sixth_value_a(self, first_formula,second_formula,third_formula):
        if first_formula[2] == "a" and second_formula[0] == "n":    #calculates potential "a"-values of sixth value
            return("a")
        elif first_formula[2] == "a" and third_formula[2] == "n":
            return("a")
        elif second_formula[1] == "a" and first_formula[0] == "n":
            return("a")
        elif second_formula[1] == "a" and third_formula[1] == "n":
            return("a")
        elif third_formula[3] == "a" and first_formula[3] == "n":
            return("a")
        elif third_formula[3] == "a" and second_formula[3] == "n":
            return("a")
        else: #calculates potential "u"-values of sixth value
            return("u")

    def total_formula_deduction_seventh_value_n(self, first_formula,second_formula,third_formula):
        if first_formula[3] == "n":    #caluculates potential "n"-values of sixth value
            return("n")
        elif second_formula[2] == "n":
            return("n")
        elif third_formula[2] == "n":
            return("n")
        else: #calculates potential "u"-values of sixth value
            return("u")

    def total_formula_deduction_seventh_value_a(self, first_formula,second_formula,third_formula):
        if first_formula[3] == "a" and second_formula[3] == "n":    #calculates potential "a"-values of sixth value
            return("a")
        elif first_formula[3] == "a" and third_formula[3] == "n":
            return("a")
        elif second_formula[2] == "a" and first_formula[1] == "n":
            return("a")
        elif second_formula[2] == "a" and third_formula[0] == "n":
            return("a")
        elif third_formula[2] == "a" and first_formula[2] == "n":
            return("a")
        elif third_formula[2] == "a" and second_formula[0] == "n":
            return("a")
        else: #calculates potential "u"-values of sixth value
            return("u")

    def total_formula_deduction_eighth_value_n(self, first_formula,second_formula,third_formula):
        if first_formula[3] == "n":    #caluculates potential "n"-values of eighth value
            return("n")
        elif second_formula[3] == "n":
            return("n")
        elif third_formula[3] == "n":
            return("n")
        else: #calculates potential "u"-values of eighth value
            return("u")

    def total_formula_deduction_eighth_value_a(self, first_formula,second_formula,third_formula):
        if first_formula[3] == "a" and second_formula[2] == "n":    #calculates potential "a"-values of eighth value
            return("a")
        elif first_formula[3] == "a" and third_formula[2] == "n":
            return("a")
        elif second_formula[3] == "a" and first_formula[1] == "n":
            return("a")
        elif second_formula[3] == "a" and third_formula[1] == "n":
            return("a")
        elif third_formula[3] == "a" and first_formula[2] == "n":
            return("a")
        elif third_formula[3] == "a" and second_formula[1] == "n":
            return("a")
        else: #calculates potential "u"-values of eighth value
            return("u")

    def syllogism_contradiction_test(self, first_formula, second_formula, third_formula):
        conclusion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        conclusion[0] = self.total_formula_deduction_first_value_n(first_formula, second_formula, third_formula)
        conclusion[1] = self.total_formula_deduction_first_value_a(first_formula, second_formula, third_formula)
        if conclusion[0] == 'n' and conclusion[1] == 'a':
            print('first error at 0')
            return (1)
        conclusion[2] = self.total_formula_deduction_second_value_n(first_formula, second_formula, third_formula)
        conclusion[3] = self.total_formula_deduction_second_value_a(first_formula, second_formula, third_formula)
        if conclusion[2] == 'n' and conclusion[3] == 'a':
            print('first error at 1')
            return (1)
        conclusion[4] = self.total_formula_deduction_third_value_n(first_formula, second_formula, third_formula)
        conclusion[5] = self.total_formula_deduction_third_value_a(first_formula, second_formula, third_formula)
        if conclusion[4] == 'n' and conclusion[5] == 'a':
            print('first error at 2')
            return (1)
        conclusion[6] = self.total_formula_deduction_fourth_value_n(first_formula, second_formula, third_formula)
        conclusion[7] = self.total_formula_deduction_fourth_value_a(first_formula, second_formula, third_formula)
        if conclusion[6] == 'n' and conclusion[7] == 'a':
            print('first error at 3')
            return (1)
        conclusion[8] = self.total_formula_deduction_fifth_value_n(first_formula, second_formula, third_formula)
        conclusion[9] = self.total_formula_deduction_fifth_value_a(first_formula, second_formula, third_formula)
        if conclusion[8] == 'n' and conclusion[9] == 'a':
            print('first error at 4')
            return (1)
        conclusion[10] = self.total_formula_deduction_sixth_value_n(first_formula, second_formula, third_formula)
        conclusion[11] = self.total_formula_deduction_sixth_value_a(first_formula, second_formula, third_formula)
        if conclusion[10] == 'n' and conclusion[11] == 'a':
            print('first error at 5')
            return (1)
        conclusion[12] = self.total_formula_deduction_seventh_value_n(first_formula, second_formula, third_formula)
        conclusion[13] = self.total_formula_deduction_seventh_value_a(first_formula, second_formula, third_formula)
        if conclusion[12] == 'n' and conclusion[13] == 'a':
            print('first error at 6')
            return (1)
        conclusion[14] = self.total_formula_deduction_eighth_value_n(first_formula, second_formula, third_formula)
        conclusion[15] = self.total_formula_deduction_eighth_value_a(first_formula, second_formula, third_formula)
        if conclusion[14] == 'n' and conclusion[15] == 'a':
            print('first error at 7')
            return (1)
        else:
            return (0)

    def total_formula_deduction_first_value(self, first_formula,second_formula,third_formula):
        if first_formula[0] == "n":    #caluculates potential "n"-values of first value
            return("n")
        elif second_formula[0] == "n":
            return("n")
        elif third_formula[0] == "n":
            return("n")
        elif first_formula[0] == "a" and second_formula[1] == "n":    #calculates potential "a"-values of first value
            return("a")
        elif first_formula[0] == "a" and third_formula[1] == "n":
            return("a")
        elif second_formula[0] == "a" and first_formula[2] == "n":
            return("a")
        elif second_formula[0] == "a" and third_formula[2] == "n":
            return("a")
        elif third_formula[0] == "a" and first_formula[1] == "n":
            return("a")
        elif third_formula[0] == "a" and second_formula[2] == "n":
            return("a")
        else: #calculates potential "u"-values of first value
            return("u")

    def total_formula_deduction_second_value(self, first_formula,second_formula,third_formula):
        if first_formula[0] == "n":    #caluculates potential "n"-values of second value
            return("n")
        elif second_formula[1] == "n":
            return("n")
        elif third_formula[1] == "n":
            return("n")
        elif first_formula[0] == "a" and second_formula[0] == "n":    #calculates potential "a"-values of second value
            return("a")
        elif first_formula[0] == "a" and third_formula[0] == "n":
            return("a")
        elif second_formula[1] == "a" and first_formula[2] == "n":
            return("a")
        elif second_formula[1] == "a" and third_formula[3] == "n":
            return("a")
        elif third_formula[1] == "a" and first_formula[1] == "n":
            return("a")
        elif third_formula[1] == "a" and second_formula[3] == "n":
            return("a")
        else: #calculates potential "u"-values of second value
            return("u")

    def total_formula_deduction_third_value(self, first_formula,second_formula,third_formula):
        if first_formula[1] == "n":    #caluculates potential "n"-values of third value
            return("n")
        elif second_formula[2] == "n":
            return("n")
        elif third_formula[0] == "n":
            return("n")
        elif first_formula[1] == "a" and second_formula[3] == "n":    #calculates potential "a"-values of third value
            return("a")
        elif first_formula[1] == "a" and third_formula[1] == "n":
            return("a")
        elif second_formula[2] == "a" and first_formula[3] == "n":
            return("a")
        elif second_formula[2] == "a" and third_formula[2] == "n":
            return("a")
        elif third_formula[0] == "a" and first_formula[0] == "n":
            return("a")
        elif third_formula[0] == "a" and second_formula[0] == "n":
            return("a")
        else: #calculates potential "u"-values of third value
            return("u")

    def total_formula_deduction_fourth_value(self, first_formula,second_formula,third_formula):
        if first_formula[1] == "n":    #caluculates potential "n"-values of fourth value
            return("n")
        elif second_formula[3] == "n":
            return("n")
        elif third_formula[1] == "n":
            return("n")
        elif first_formula[1] == "a" and second_formula[2] == "n":    #calculates potential "a"-values of fourth value
            return("a")
        elif first_formula[1] == "a" and third_formula[0] == "n":
            return("a")
        elif second_formula[3] == "a" and first_formula[3] == "n":
            return("a")
        elif second_formula[3] == "a" and third_formula[3] == "n":
            return("a")
        elif third_formula[1] == "a" and first_formula[0] == "n":
            return("a")
        elif third_formula[1] == "a" and second_formula[1] == "n":
            return("a")
        else: #calculates potential "u"-values of fourth value
            return("u")

    def total_formula_deduction_fifth_value(self, first_formula,second_formula,third_formula):
        if first_formula[2] == "n":    #caluculates potential "n"-values of fifth value
            return("n")
        elif second_formula[0] == "n":
            return("n")
        elif third_formula[2] == "n":
            return("n")
        elif first_formula[2] == "a" and second_formula[1] == "n":    #calculates potential "a"-values of fifth value
            return("a")
        elif first_formula[2] == "a" and third_formula[3] == "n":
            return("a")
        elif second_formula[0] == "a" and first_formula[0] == "n":
            return("a")
        elif second_formula[0] == "a" and third_formula[0] == "n":
            return("a")
        elif third_formula[2] == "a" and first_formula[3] == "n":
            return("a")
        elif third_formula[2] == "a" and second_formula[2] == "n":
            return("a")
        else: #calculates potential "u"-values of fifth value
            return("u")

    def total_formula_deduction_sixth_value(self, first_formula,second_formula,third_formula):
        if first_formula[2] == "n":    #caluculates potential "n"-values of sixth value
            return("n")
        elif second_formula[1] == "n":
            return("n")
        elif third_formula[3] == "n":
            return("n")
        elif first_formula[2] == "a" and second_formula[0] == "n":    #calculates potential "a"-values of sixth value
            return("a")
        elif first_formula[2] == "a" and third_formula[2] == "n":
            return("a")
        elif second_formula[1] == "a" and first_formula[0] == "n":
            return("a")
        elif second_formula[1] == "a" and third_formula[1] == "n":
            return("a")
        elif third_formula[3] == "a" and first_formula[3] == "n":
            return("a")
        elif third_formula[3] == "a" and second_formula[3] == "n":
            return("a")
        else: #calculates potential "u"-values of sixth value
            return("u")

    def total_formula_deduction_seventh_value(self, first_formula,second_formula,third_formula):
        if first_formula[3] == "n":    #caluculates potential "n"-values of sixth value
            return("n")
        elif second_formula[2] == "n":
            return("n")
        elif third_formula[2] == "n":
            return("n")
        elif first_formula[3] == "a" and second_formula[3] == "n":    #calculates potential "a"-values of sixth value
            return("a")
        elif first_formula[3] == "a" and third_formula[3] == "n":
            return("a")
        elif second_formula[2] == "a" and first_formula[1] == "n":
            return("a")
        elif second_formula[2] == "a" and third_formula[0] == "n":
            return("a")
        elif third_formula[2] == "a" and first_formula[2] == "n":
            return("a")
        elif third_formula[2] == "a" and second_formula[0] == "n":
            return("a")
        else: #calculates potential "u"-values of sixth value
            return("u")

    def total_formula_deduction_eighth_value(self, first_formula,second_formula,third_formula):
        if first_formula[3] == "n":    #caluculates potential "n"-values of eighth value
            return("n")
        elif second_formula[3] == "n":
            return("n")
        elif third_formula[3] == "n":
            return("n")
        elif first_formula[3] == "a" and second_formula[2] == "n":    #calculates potential "a"-values of eighth value
            return("a")
        elif first_formula[3] == "a" and third_formula[2] == "n":
            return("a")
        elif second_formula[3] == "a" and first_formula[1] == "n":
            return("a")
        elif second_formula[3] == "a" and third_formula[1] == "n":
            return("a")
        elif third_formula[3] == "a" and first_formula[2] == "n":
            return("a")
        elif third_formula[3] == "a" and second_formula[1] == "n":
            return("a")
        else: #calculates potential "u"-values of eighth value
            return("u")

    def syllogism_solution(self, first_formula,second_formula, third_formula):
        conclusion = [0,0,0,0,0,0,0,0]
        conclusion[0] = self.total_formula_deduction_first_value(first_formula,second_formula, third_formula)
        conclusion[1] = self.total_formula_deduction_second_value(first_formula,second_formula, third_formula)
        conclusion[2] = self.total_formula_deduction_third_value(first_formula,second_formula, third_formula)
        conclusion[3] = self.total_formula_deduction_fourth_value(first_formula,second_formula, third_formula)
        conclusion[4] = self.total_formula_deduction_fifth_value(first_formula,second_formula, third_formula)
        conclusion[5] = self.total_formula_deduction_sixth_value(first_formula,second_formula, third_formula)
        conclusion[6] = self.total_formula_deduction_seventh_value(first_formula,second_formula, third_formula)
        conclusion[7] = self.total_formula_deduction_eighth_value(first_formula,second_formula, third_formula)
        return(conclusion)

    def output2(self, first_formula, second_formula, third_formula):

        result_contradiction_test = self.syllogism_contradiction_test(first_formula, second_formula, third_formula)
        solution = self.syllogism_solution(first_formula, second_formula, third_formula)

        #self.conclusion_label.text = solution
        return [solution, result_contradiction_test]

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def append_function(self, button):
        print(button)
        if foo_3 == []:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_1_p1.text ='n'
                self.btn_1_p1.background_color=(1, 0, 0, .7)
                self.btn_2_p1.text ='n'
                self.btn_2_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_1_p1.text ='a'
                self.btn_1_p1.background_color=(0, 1, 0, .7)
                self.btn_2_p1.text ='a'
                self.btn_2_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_1_p1.text ='u'
                self.btn_1_p1.background_color=(1, 1, 1, .7)
                self.btn_2_p1.text ='u'
                self.btn_2_p1.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 1:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_3_p1.text ='n'
                self.btn_3_p1.background_color=(1, 0, 0, .7)
                self.btn_4_p1.text ='n'
                self.btn_4_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_3_p1.text ='a'
                self.btn_3_p1.background_color=(0, 1, 0, .7)
                self.btn_4_p1.text ='a'
                self.btn_4_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_3_p1.text ='u'
                self.btn_3_p1.background_color=(1, 1, 1, .7)
                self.btn_4_p1.text ='u'
                self.btn_4_p1.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 2:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_5_p1.text ='n'
                self.btn_5_p1.background_color=(1, 0, 0, .7)
                self.btn_6_p1.text ='n'
                self.btn_6_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_5_p1.text ='a'
                self.btn_5_p1.background_color=(0, 1, 0, .7)
                self.btn_6_p1.text ='a'
                self.btn_6_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_5_p1.text ='u'
                self.btn_5_p1.background_color=(1, 1, 1, .7)
                self.btn_6_p1.text ='u'
                self.btn_6_p1.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 3:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_7_p1.text ='n'
                self.btn_7_p1.background_color=(1, 0, 0, .7)
                self.btn_8_p1.text ='n'
                self.btn_8_p1.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_7_p1.text ='a'
                self.btn_7_p1.background_color=(0, 1, 0, .7)
                self.btn_8_p1.text ='a'
                self.btn_8_p1.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_7_p1.text ='u'
                self.btn_7_p1.background_color=(1, 1, 1, .7)
                self.btn_8_p1.text ='u'
                self.btn_8_p1.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 4:
            print('test')
            self.first_formula = foo_3
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_1_p2.text ='n'
                self.btn_1_p2.background_color=(1, 0, 0, .7)
                self.btn_5_p2.text ='n'
                self.btn_5_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_1_p2.text ='a'
                self.btn_1_p2.background_color=(0, 1, 0, .7)
                self.btn_5_p2.text ='a'
                self.btn_5_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_1_p2.text ='u'
                self.btn_1_p2.background_color=(1, 1, 1, .7)
                self.btn_5_p2.text ='u'
                self.btn_5_p2.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 5:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_2_p2.text ='n'
                self.btn_2_p2.background_color=(1, 0, 0, .7)
                self.btn_6_p2.text ='n'
                self.btn_6_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_2_p2.text ='a'
                self.btn_2_p2.background_color=(0, 1, 0, .7)
                self.btn_6_p2.text ='a'
                self.btn_6_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_2_p2.text ='u'
                self.btn_2_p2.background_color=(1, 1, 1, .7)
                self.btn_6_p2.text ='u'
                self.btn_6_p2.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 6:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_3_p2.text ='n'
                self.btn_3_p2.background_color=(1, 0, 0, .7)
                self.btn_7_p2.text ='n'
                self.btn_7_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_3_p2.text ='a'
                self.btn_3_p2.background_color=(0, 1, 0, .7)
                self.btn_7_p2.text ='a'
                self.btn_7_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_3_p2.text ='u'
                self.btn_3_p2.background_color=(1, 1, 1, .7)
                self.btn_7_p2.text ='u'
                self.btn_7_p2.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 7:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_4_p2.text ='n'
                self.btn_4_p2.background_color=(1, 0, 0, .7)
                self.btn_8_p2.text ='n'
                self.btn_8_p2.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_4_p2.text ='a'
                self.btn_4_p2.background_color=(0, 1, 0, .7)
                self.btn_8_p2.text ='a'
                self.btn_8_p2.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_4_p2.text ='u'
                self.btn_4_p2.background_color=(1, 1, 1, .7)
                self.btn_8_p2.text ='u'
                self.btn_8_p2.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 8:
            print('test')
            self.second_formula = foo_3[4:8]
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_1_p3.text ='n'
                self.btn_1_p3.background_color=(1, 0, 0, .7)
                self.btn_3_p3.text ='n'
                self.btn_3_p3.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_1_p3.text ='a'
                self.btn_1_p3.background_color=(0, 1, 0, .7)
                self.btn_3_p3.text ='a'
                self.btn_3_p3.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_1_p3.text ='u'
                self.btn_1_p3.background_color=(1, 1, 1, .7)
                self.btn_3_p3.text ='u'
                self.btn_3_p3.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 9:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_2_p3.text ='n'
                self.btn_2_p3.background_color=(1, 0, 0, .7)
                self.btn_4_p3.text ='n'
                self.btn_4_p3.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_2_p3.text ='a'
                self.btn_2_p3.background_color=(0, 1, 0, .7)
                self.btn_4_p3.text ='a'
                self.btn_4_p3.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_2_p3.text ='u'
                self.btn_2_p3.background_color=(1, 1, 1, .7)
                self.btn_4_p3.text ='u'
                self.btn_4_p3.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 10:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_5_p3.text ='n'
                self.btn_5_p3.background_color=(1, 0, 0, .7)
                self.btn_7_p3.text ='n'
                self.btn_7_p3.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_5_p3.text ='a'
                self.btn_5_p3.background_color=(0, 1, 0, .7)
                self.btn_7_p3.text ='a'
                self.btn_7_p3.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_5_p3.text ='u'
                self.btn_5_p3.background_color=(1, 1, 1, .7)
                self.btn_7_p3.text ='u'
                self.btn_7_p3.background_color=(1, 1, 1, .7)
        elif len(foo_3) == 11:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_6_p3.text ='n'
                self.btn_6_p3.background_color=(1, 0, 0, .7)
                self.btn_8_p3.text ='n'
                self.btn_8_p3.background_color=(1, 0, 0, .7)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_6_p3.text ='a'
                self.btn_6_p3.background_color=(0, 1, 0, .7)
                self.btn_8_p3.text ='a'
                self.btn_8_p3.background_color=(0, 1, 0, .7)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_6_p3.text ='u'
                self.btn_6_p3.background_color=(1, 1, 1, .7)
                self.btn_8_p3.text ='u'
                self.btn_8_p3.background_color=(1, 1, 1, .7)
        if len(foo_3) == 12:
            self.third_formula = foo_3[8:12]
            self.btn_n.disabled = True
            self.btn_a.disabled = True
            self.btn_u.disabled = True
            self.click(button)
            foo_3.clear()

    def clear_widgets_function(self, *args):
        self.clear_widgets()
        foo_3.clear()
        
        self.refresh2_button = Button(text='Generate!', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .8})
        self.add_widget(self.refresh2_button)
        
        self.menu_button = Button(text='Menu', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .9})
        self.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.refresh2_button.bind(on_press=self.refresh_function)
        
        self.refresh2_button.bind(on_press=self.clear_widgets_function)

    def click(self,my_button2):
        my_text = self.first_formula
        my_text2 = self.second_formula
        my_text3 = self.third_formula
        
        function_output_list = self.output2(my_text, my_text2, my_text3)
        
        if function_output_list[0][0] != 'u':
            function_output_list_upper_value_one = function_output_list[0][0].upper()
        else:
            function_output_list_upper_value_one = function_output_list[0][0]
            
        if function_output_list[0][1] != 'u':
            function_output_list_upper_value_two = function_output_list[0][1].upper()
        else:
            function_output_list_upper_value_two = function_output_list[0][1]
            
        if function_output_list[0][2] != 'u':
            function_output_list_upper_value_three = function_output_list[0][2].upper()
        else:
            function_output_list_upper_value_three = function_output_list[0][2]
            
        if function_output_list[0][3] != 'u':
            function_output_list_upper_value_four = function_output_list[0][3].upper()
        else:
            function_output_list_upper_value_four = function_output_list[0][3]
            
        if function_output_list[0][4] != 'u':
            function_output_list_upper_value_five = function_output_list[0][4].upper()
        else:
            function_output_list_upper_value_five = function_output_list[0][4]
            
        if function_output_list[0][5] != 'u':
            function_output_list_upper_value_six = function_output_list[0][5].upper()
        else:
            function_output_list_upper_value_six = function_output_list[0][5]

        if function_output_list[0][6] != 'u':
            function_output_list_upper_value_seven = function_output_list[0][6].upper()
        else:
            function_output_list_upper_value_seven = function_output_list[0][6]
            
        if function_output_list[0][7] != 'u':
            function_output_list_upper_value_eight = function_output_list[0][7].upper()
        else:
            function_output_list_upper_value_eight = function_output_list[0][7]

        if function_output_list[1] == 1:
            self.conclusion_label.text = "Contradiction!"
        else:
            self.btn_1_c.text = function_output_list_upper_value_one
            self.btn_2_c.text = function_output_list_upper_value_two
            self.btn_3_c.text = function_output_list_upper_value_three
            self.btn_4_c.text = function_output_list_upper_value_four
            self.btn_5_c.text = function_output_list_upper_value_five
            self.btn_6_c.text = function_output_list_upper_value_six
            self.btn_7_c.text = function_output_list_upper_value_seven
            self.btn_8_c.text = function_output_list_upper_value_eight
            if function_output_list[0][0] == 'n':
                self.btn_1_c.background_color=(1, 0, 0, .7)
                self.btn_1_c.background_color=(1, 0, 0, .7)
            elif function_output_list[0][0] == 'a':
                self.btn_1_c.background_color=(0, 1, 0, .7)
                self.btn_1_c.background_color=(0, 1, 0, .7)
            elif function_output_list[0][0] == 'u':
                self.btn_1_c.background_color=(1, 1, 1, .7)
                self.btn_1_c.background_color=(1, 1, 1, .7)
            if function_output_list[0][1] == 'n':
                self.btn_2_c.background_color=(1, 0, 0, .7)
                self.btn_2_c.background_color=(1, 0, 0, .7)
            elif function_output_list[0][1] == 'a':
                self.btn_2_c.background_color=(0, 1, 0, .7)
                self.btn_2_c.background_color=(0, 1, 0, .7)
            elif function_output_list[0][1] == 'u':
                self.btn_2_c.background_color=(1, 1, 1, .7)
                self.btn_2_c.background_color=(1, 1, 1, .7)
            if function_output_list[0][2] == 'n':
                self.btn_3_c.background_color=(1, 0, 0, .7)
                self.btn_3_c.background_color=(1, 0, 0, .7)
            elif function_output_list[0][2] == 'a':
                self.btn_3_c.background_color=(0, 1, 0, .7)
                self.btn_3_c.background_color=(0, 1, 0, .7)
            elif function_output_list[0][2] == 'u':
                self.btn_3_c.background_color=(1, 1, 1, .7)
                self.btn_3_c.background_color=(1, 1, 1, .7)
            if function_output_list[0][3] == 'n':
                self.btn_4_c.background_color=(1, 0, 0, .7)
                self.btn_4_c.background_color=(1, 0, 0, .7)
            elif function_output_list[0][3] == 'a':
                self.btn_4_c.background_color=(0, 1, 0, .7)
                self.btn_4_c.background_color=(0, 1, 0, .7)
            elif function_output_list[0][3] == 'u':
                self.btn_4_c.background_color=(1, 1, 1, .7)
                self.btn_4_c.background_color=(1, 1, 1, .7)
            if function_output_list[0][4] == 'n':
                self.btn_5_c.background_color=(1, 0, 0, .7)
                self.btn_5_c.background_color=(1, 0, 0, .7)
            elif function_output_list[0][4] == 'a':
                self.btn_5_c.background_color=(0, 1, 0, .7)
                self.btn_5_c.background_color=(0, 1, 0, .7)
            elif function_output_list[0][4] == 'u':
                self.btn_5_c.background_color=(1, 1, 1, .7)
                self.btn_5_c.background_color=(1, 1, 1, .7)
            if function_output_list[0][5] == 'n':
                self.btn_6_c.background_color=(1, 0, 0, .7)
                self.btn_6_c.background_color=(1, 0, 0, .7)
            elif function_output_list[0][5] == 'a':
                self.btn_6_c.background_color=(0, 1, 0, .7)
                self.btn_6_c.background_color=(0, 1, 0, .7)
            elif function_output_list[0][5] == 'u':
                self.btn_6_c.background_color=(1, 1, 1, .7)
                self.btn_6_c.background_color=(1, 1, 1, .7)
            if function_output_list[0][6] == 'n':
                self.btn_7_c.background_color=(1, 0, 0, .7)
                self.btn_7_c.background_color=(1, 0, 0, .7)
            elif function_output_list[0][6] == 'a':
                self.btn_7_c.background_color=(0, 1, 0, .7)
                self.btn_7_c.background_color=(0, 1, 0, .7)
            elif function_output_list[0][6] == 'u':
                self.btn_7_c.background_color=(1, 1, 1, .7)
                self.btn_7_c.background_color=(1, 1, 1, .7)
            if function_output_list[0][7] == 'n':
                self.btn_8_c.background_color=(1, 0, 0, .7)
                self.btn_8_c.background_color=(1, 0, 0, .7)
            elif function_output_list[0][7] == 'a':
                self.btn_8_c.background_color=(0, 1, 0, .7)
                self.btn_8_c.background_color=(0, 1, 0, .7)
            elif function_output_list[0][7] == 'u':
                self.btn_8_c.background_color=(1, 1, 1, .7)
                self.btn_8_c.background_color=(1, 1, 1, .7)
                
    def refresh_function(self, button):
        
        horizontal = BoxLayout(orientation='horizontal')
        self.add_widget(horizontal)
        
        self.label_1 = Label(font_size= 20, size_hint_x = .5)
        horizontal.add_widget(self.label_1)
        
        vertical = BoxLayout(orientation='vertical')
        horizontal.add_widget(vertical)
        
        self.boxlayout_up = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.boxlayout_up)
    
        self.syllogism_box_col_1 = BoxLayout(orientation='vertical')
        vertical.add_widget(self.syllogism_box_col_1)
        
        self.syllogism_box_row_1 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_1)
        
        self.dummy_label_one = Label(text='', size_hint_x = 2.5)
        self.syllogism_box_row_1.add_widget(self.dummy_label_one)

        self.s1 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s1)
        self.s2 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s2)
        self.s3 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s3)
        self.s4 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s4)
        self.s5 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s5)
        self.s6 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s6)
        self.s7 = Label(text='S')
        self.syllogism_box_row_1.add_widget(self.s7)
        self.s8 = Label(text='~S')
        self.syllogism_box_row_1.add_widget(self.s8)

        self.syllogism_box_row_2 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_2)
        
        self.dummy_label_two = Label(text='', size_hint_x = 2.5)
        self.syllogism_box_row_2.add_widget(self.dummy_label_two)

        self.m1 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m1)
        self.m2 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m2) 
        self.m3 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m3)
        self.m4 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m4)
        self.m5 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m5)
        self.m6 = Label(text='M')
        self.syllogism_box_row_2.add_widget(self.m6)
        self.m7 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m7)
        self.m8 = Label(text='~M')
        self.syllogism_box_row_2.add_widget(self.m8)

        self.syllogism_box_row_3 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_3)
        
        self.dummy_label_three = Label(text='', size_hint_x = 2.5)
        self.syllogism_box_row_3.add_widget(self.dummy_label_three)

        self.p1 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p1)
        self.p2 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p2)
        self.p3 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p3)
        self.p4 = Label(text='P')
        self.syllogism_box_row_3.add_widget(self.p4)
        self.p5 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p5)
        self.p6 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p6)
        self.p7 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p7)
        self.p8 = Label(text='~P')
        self.syllogism_box_row_3.add_widget(self.p8)

        self.syllogism_box_row_4 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_4)
        
        self.premis_one_label = Label(text='1. Formula', size_hint_x = 2.5)
        self.syllogism_box_row_4.add_widget(self.premis_one_label)

        self.btn_1_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_1_p1)
        self.btn_2_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_2_p1)
        self.btn_3_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_3_p1)
        self.btn_4_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_4_p1)
        self.btn_5_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_5_p1)
        self.btn_6_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_6_p1)
        self.btn_7_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_7_p1)
        self.btn_8_p1 = Button(background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_8_p1)

        self.syllogism_box_row_5 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_5)
        
        self.premis_two_label = Label(text='2. Formula', size_hint_x = 2.5)
        self.syllogism_box_row_5.add_widget(self.premis_two_label)

        self.btn_1_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_1_p2)
        self.btn_2_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_2_p2)
        self.btn_3_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_3_p2)
        self.btn_4_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_4_p2)
        self.btn_5_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_5_p2)
        self.btn_6_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_6_p2)
        self.btn_7_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_7_p2)
        self.btn_8_p2 = Button(background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_8_p2)

        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.premis_three_label = Label(text='3. Formula', size_hint_x = 2.5)
        self.syllogism_box_row_6.add_widget(self.premis_three_label)

        self.btn_1_p3 = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_p3)
        self.btn_2_p3 = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_p3)
        self.btn_3_p3 = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_p3)
        self.btn_4_p3 = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_p3)
        self.btn_5_p3 = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_p3)
        self.btn_6_p3 = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_p3)
        self.btn_7_p3 = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_p3)
        self.btn_8_p3 = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_p3)

        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.conclusion_label = Label(text='Total-formula', size_hint_x = 2.5)
        self.syllogism_box_row_6.add_widget(self.conclusion_label)

        self.btn_1_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_c)
        self.btn_2_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_c)
        self.btn_3_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_c)
        self.btn_4_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_c)
        self.btn_5_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_c)
        self.btn_6_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_c)
        self.btn_7_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_c)
        self.btn_8_c = Button(background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_c)

        self.syllogism_box_col_2 = BoxLayout(orientation='vertical')
        vertical.add_widget(self.syllogism_box_col_2)

        self.label_5 = Label(font_size= 20)
        vertical.add_widget(self.label_5)

        self.box_horizontal_buttons_down = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.box_horizontal_buttons_down)

        self.btn_n = Button(text='n', background_normal='', background_color=(1, 0, 0, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_n)
        variable_btn_n ='n'
        self.btn_n.bind(on_press=self.append_function)

        self.btn_a = Button(text='a', background_normal='', background_color=(0, 1, 0, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_a)
        variable_btn_a ='a'
        self.btn_a.bind(on_press=self.append_function)

        self.btn_u = Button(text='u', background_normal='', background_color=(1, 1, 1, .7))
        self.box_horizontal_buttons_down.add_widget(self.btn_u)
        variable_btn_u ='u'
        self.btn_u.bind(on_press=self.append_function)

        self.label_3 = Label(font_size= 20, size_hint_x = .5)
        horizontal.add_widget(self.label_3)
        


        self.refresh_button.bind(on_press=self.clear_widgets_function)

    def __init__(self, **kwargs):
        super(Total_formulas_QuizScreen, self).__init__(**kwargs)
        
        self.refresh_button = Button(text='Generate!', size_hint=(.1, .1), pos_hint={'x': .9, 'y': .8})
        self.add_widget(self.refresh_button)
        self.refresh_button.bind(on_press=self.refresh_function)

class Menu_TransformationsScreen(Screen):
    pass

class TransformationsScreen(Screen):

    def inital_judge_values(self, inital_judge):
        if inital_judge == "SaP":
            inital_judge = "auna"
        elif inital_judge == "SeP":
            inital_judge = "naau"
        elif inital_judge == "SiP":
            inital_judge = "auuu"
        elif inital_judge == "SoP":
            inital_judge = "uuau"
        return (inital_judge)

    def output_judge_fn(self, solution):
        if solution == "auna":
            return "\n\nAll S are P,\nalso known as SaP"
        elif solution == "auuu":
            return "\n\nSome S are P,\nalso known as SiP"
        elif solution == "naau":
            return "\n\nNo S is P,\nalso known as SeP"
        elif solution == "uuau":
            return "\n\nSome S are no P,\nalso known as SoP"
        else:
            return ("\n\nNo traditional\njudge!")

    def __init__(self, **kwargs):
        super(TransformationsScreen, self).__init__(**kwargs)

        layout_hor = BoxLayout(orientation='horizontal')
        self.add_widget(layout_hor)

        layout = BoxLayout(orientation='vertical')
        layout_hor.add_widget(layout)

        layout_in_layout = BoxLayout(orientation='horizontal')
        layout.add_widget(layout_in_layout)

        self.Initial_judge_label = Label(text= 'Initial Judge/Formula: ', font_size= 20)
        layout_in_layout.add_widget(self.Initial_judge_label)

        self.Initial_judge = TextInput(multiline=False)
        layout_in_layout.add_widget(self.Initial_judge)

        layout_in_layout_2 = BoxLayout(orientation='horizontal')
        layout.add_widget(layout_in_layout_2)

        self.conversion_btn = Button(text= 'Conversion', font_size= 20)
        self.conversion_btn.bind(on_press=self.conversion_fn)
        layout_in_layout_2.add_widget(self.conversion_btn)

        self.obversion_btn = Button(text= 'Obversion', font_size= 20)
        self.obversion_btn.bind(on_press=self.obversion_fn)
        layout_in_layout_2.add_widget(self.obversion_btn)

        self.contradiction_btn = Button(text= 'Contradiction', font_size= 20)
        self.contradiction_btn.bind(on_press=self.contradiction_fn)
        layout_in_layout_2.add_widget(self.contradiction_btn)

        layout_in_layout_3 = BoxLayout(orientation='horizontal')
        layout.add_widget(layout_in_layout_3)

        self.partial_inversion_btn = Button(text="Partial Inversion", font_size= 20)
        self.partial_inversion_btn.bind(on_press=self.partial_inversion_fn)
        layout_in_layout_3.add_widget(self.partial_inversion_btn)

        self.inversion_btn = Button(text="Inversion", font_size= 20)
        self.inversion_btn.bind(on_press=self.inversion_fn)
        layout_in_layout_3.add_widget(self.inversion_btn)

        self.conclusion_label = Label(text='Enter Formula!', font_size= 20)
        layout_hor.add_widget(self.conclusion_label)

    def conversion_fn(self, button):
        inital_judge = self.Initial_judge.text        
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        conversion = inital_judge_values_[0] + inital_judge_values_[2] + inital_judge_values_[1] + inital_judge_values_[3]
        solution = conversion
        output_judge = self.output_judge_fn(solution)
        self.conclusion_label.text = conversion + "\n\n" + output_judge

    def obversion_fn(self, button):
        inital_judge = self.Initial_judge.text
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        obversion = inital_judge_values_[2] + inital_judge_values_[3] + inital_judge_values_[0] + inital_judge_values_[1]
        solution = obversion
        output_judge = self.output_judge_fn(solution)
        self.conclusion_label.text = obversion + "\n\n" + output_judge

    def contradiction_fn(self, button):
        inital_judge = self.Initial_judge.text
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        contradiction = inital_judge_values_[3] + inital_judge_values_[1] + inital_judge_values_[2] + inital_judge_values_[0]
        solution = contradiction
        output_judge = self.output_judge_fn(solution)
        self.conclusion_label.text = contradiction + "\n\n" + output_judge

    def partial_inversion_fn(self, button):
        inital_judge = self.Initial_judge.text
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        partial_inversion = inital_judge_values_[1] + inital_judge_values_[0] + inital_judge_values_[3] + inital_judge_values_[2]
        solution = partial_inversion
        output_judge = self.output_judge_fn(solution)
        self.conclusion_label.text = partial_inversion + "\n\n" + output_judge

    def inversion_fn(self, button):
        inital_judge = self.Initial_judge.text
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        inversion = inital_judge_values_[3] + inital_judge_values_[2] + inital_judge_values_[1] + inital_judge_values_[0]
        solution = inversion
        output_judge = self.output_judge_fn(solution)
        self.conclusion_label.text = inversion + "\n\n" + output_judge

class Conditional_StatementsScreen(Screen):
    pass

class RessourcesScreen(Screen):
    pass

class TestApp(App):
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Menu_conclusionsScreen(name='menu_conclusions'))
        sm.add_widget(GeneralScreen(name='general'))
        sm.add_widget(Menu_introductionScreen(name='menu_introduction'))
        sm.add_widget(Menu_introductionScreen_1(name='menu_introduction_1'))
        sm.add_widget(TrainingScreen(name='training'))
        sm.add_widget(Menu_total_formulas_Screen(name='menu-total-formulas'))
        sm.add_widget(Total_formulas_QuizScreen(name='total-formulas-quiz'))
        sm.add_widget(ConclusionsScreen(name='conclusions'))
        sm.add_widget(Menu_TransformationsScreen(name='menu_transformations'))
        sm.add_widget(TransformationsScreen(name='transformations'))
        sm.add_widget(Conditional_StatementsScreen(name='conditional-statements'))
        sm.add_widget(RessourcesScreen(name='ressources'))
        self.use_kivy_settings = False
        return sm
    
    def build_config(self, config):
        config.setdefaults('trainer', {
            'completedsyllogistic': 0,
            'particularpremis': 0})
        
    def build_settings(self, settings):
        settings.add_json_panel('Settings - Syllogistic Trainer',
                                self.config,
                                data=settings_json)
    
    def on_config_change(self, config, section, key, value):
        print(config, section, key, value)
        if config is self.config:
            token = (section, key)
            if token == ('trainer', 'completedsyllogistic'):
                TrainingScreen.function_completed_syllogistic_settings(self)
            elif token == ('trainer', 'particularpremis'):
                TrainingScreen.function_particularpremis_settings(self)

if __name__ == '__main__':
    TestApp().run()
