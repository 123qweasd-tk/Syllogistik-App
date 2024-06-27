from kivy.app import App
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty, ConfigParserProperty, ObjectProperty, NumericProperty, ListProperty
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
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.clock import Clock
from kivy.uix.scatter import Scatter


from kivy.config import Config
from kivy.config import ConfigParser

from settingsjson import settings_json
import webbrowser
import random
import flatlatex

Builder.load_string("""

<LineRectangle>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Line:
            width: 1.3
            rectangle: (self.x, self.y, self.width, self.height)

<CustomLabel_green>:
    canvas.before:
        Color: 
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size

<CustomLabel_red>:
    canvas.before:
        Color: 
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size

<CustomLabel>:
    canvas.before:
        Color: 
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size

<CustomBoxLayout>:
    canvas.before:
        Color:
            rgba: self.background_color
        Rectangle:
            pos: self.pos
            size: self.size

<EllipseLabel>:
    canvas:
        Color:
            rgba: 1, 1, 1, 1
        Line:
            width: 1.3
            circle:
                (self.center_x, self.center_y, min(self.width, self.height)*.8
                / 2)

<MenuScreen>:
    BoxLayout:
        orientation: 'vertical'
        space: dp(10)
        Label:
            text: 'Menü'
            font_size: dp(30)
            color: 0,1,0.5
        Button:
            text: 'Allgemein'
            halign: 'center'
            valign: 'center'
            font_size: dp(27)
            on_press: root.manager.current = 'general'
            background_normal: ''
            background_color: 1, .3, .4, .85
        Button:
            text: root.button_transformations_in_main_menu
            text_size: self.size
            halign: 'center'
            valign: 'center'
            font_size: dp(27)
            on_press: root.manager.current = 'menu_transformations'
            background_normal: ''
            background_color: 1, .2, .4, .3
        Button:
            text: root.button_conclusion_in_main_menu
            text_size: self.size
            halign: 'center'
            valign: 'center'
            font_size: dp(27)
            on_press: root.manager.current = 'menu_conclusions'
            background_normal: ''
            background_color: 255, 255, 0, .8
        Button:
            text: root.button_total_formulas_in_main_menu
            text_size: self.size
            halign: 'center'
            valign: 'center'
            font_size: dp(27)
            on_press: root.manager.current = 'menu-total-formulas'
            background_normal: ''
            background_color: 0, 1, 0, .2
        Button:
            text: 'Ressourcen'
            font_size: dp(27)
            on_press: root.manager.current = 'ressources'
            background_normal: ''
            background_color: 1, .3, .4, .85
        Button:
            text: 'Beenden'
            font_size: dp(27)
            on_press: app.stop()
            background_normal: ''
            background_color: 1, .5, .3, .3

<GeneralScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Einleitung'
            font_size: dp(27)
            on_press: root.manager.current = 'menu_introduction'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Quiz'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
    Button:
        text: "Menü"
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<Menu_introductionScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Die beiden logischen Prinzipien'
            on_press: root.manager.current = 'menu_introduction_1'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Analytische Verhältnisse und synthetische Verbindungen'
            on_press: root.manager.current = 'menu_introduction_1b'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Unmittelbare und mittelbare Schlüsse'
            on_press: root.manager.current = 'menu_introduction_2'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Reine und Angewandte Logik'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Das Problem der Wahrheit und transgressives Denken'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Struktur der App'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
    Button:
        text: "Menü"
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<Menu_introductionScreen_1>

<Menu_introductionScreen_1b>

<Menu_introductionScreen_2>

<Menu_introductionScreen_3>       

<Menu_conclusionsScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Einleitung'
            font_size: dp(27)
            on_press: root.manager.current = 'menu_conclusion_introduction'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Spielwiese'
            font_size: dp(27)
            
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Übungen - Quiz'
            font_size: dp(27)
            on_press:
                root.manager.current = 'training'
            background_normal: ''
            background_color: 1, 0, .5, .3
        Button:
            text: 'Rechnen - Quiz'
            font_size: dp(27)

            background_normal: ''
            background_color: 1, 0, .5, .3
    Button:
        text: 'Menü'
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<Menu_conclusion_introductionScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Überblick - Tabelle: Syllogistik'
            on_press: root.manager.current = 'table_overview'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Überblick - Tabelle: Verlängerte dyadische Formeln'
            on_press: root.manager.current = 'table_overview_2'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2

<Table_overviewScreen>:

<Table_overviewScreen_2>:

<ConclusionsScreen>:
    Button:
        text: 'Menü'
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<TrainingScreen>:
    Button:
        text: 'Menü'
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}
    Button:
        text: 'Generiere!'
        on_press: root.refresh_function()
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.8}
    Button:
        id: 'settings_button'
        text: 'Einstellungen'
        on_release: app.open_settings()
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.7}

<Training_calculating_quiz_Screen>

<Menu_total_formulas_Screen>:
    BoxLayout:
        orientation: "horizontal"
        BoxLayout:
            orientation: "vertical"
            Label:
                text: root.label_left_menu_total_formulas
                halign: 'center'
                valign: 'center'
                font_size: dp(27)
                color: (.5, .6, .8, 1)
                text_size: self.size
                halign: 'center'
            Button:
                text: 'Einleitung'
                font_size: dp(27)
                
                background_normal: ''
                background_color: 1, .1, .1, .2
            Button:
                text: 'Spielwiese'
                font_size: dp(27)
                on_press: root.manager.current = 'total-formulas-playground-left'
                background_normal: ''
                background_color: 1, .1, .1, .2
            Button:
                text: 'Quiz'
                font_size: dp(27)
                background_normal: ''
                background_color: 1, 0, .5, .3
        BoxLayout:
            orientation: "vertical"
            Label:
                text: root.label_right_menu_total_formulas
                halign: 'center'
                valign: 'center'
                font_size: dp(27)
                color: (.5, .6, .8, 1)
                text_size: self.size
                halign: 'center'
            Button:
                text: 'Einleitung'
                font_size: dp(27)
                background_normal: ''
                background_color: 1, .1, .1, .2
            Button:
                text: 'Spielwiese'
                font_size: dp(27)
                on_press: root.manager.current = 'total-formulas-playground-right'
                background_normal: ''
                background_color: 1, .1, .1, .2
            Button:
                text: 'Quiz'
                font_size: dp(27)
                background_normal: ''
                background_color: 1, 0, .5, .3

<Total_formulas_Playground_left_Screen>:
    Button:
        text: 'Menü'
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<Total_formulas_Playground_right_Screen>:
    Button:
        text: 'Menü'
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<Total_formulas_QuizScreen>:
    Button:
        text: 'Menü'
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<Menu_TransformationsScreen>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: 'Einleitung'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Spielwiese'
            font_size: dp(27)
            on_press: root.manager.current = 'transformations'
            background_normal: ''
            background_color: 1, .1, .1, .2
        Button:
            text: 'Quiz'
            font_size: dp(27)
            background_normal: ''
            background_color: 1, 0, .5, .3

<TransformationsScreen>:
    Button:
        text: 'Menü'
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<RessourcesScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Ressourcen"
            font_size: dp(30)
        Button:
            text: 'P vs. NP-Problem'
            font_size: dp(27)
            on_press:
                import webbrowser
                webbrowser.open('https://de.wikiversity.org/w/index.php?title=Projekt:Beweis_f%C3%BCr_P_ungleich_NP_von_Thomas_K%C3%A4fer&oldid=930414')
        Button:
            text: 'SAT'
            font_size: dp(27)
            on_press: root.manager.current = 'sat'
            background_normal: ''
            background_color: 1, 0, .5, .3
        Button:
            text: root.text_syllogism_ressource
            text_size: self.size
            halign: 'center'
            valign: 'center'
            font_size: dp(27)
            on_press:
                import webbrowser
                webbrowser.open('https://de.wikipedia.org/w/index.php?title=Walther_Br%C3%BCning&oldid=185439594#Strenge_Syllogistik')
    Button:
        text: "Menü"
        on_press: root.manager.current = 'menu'
        size_hint: "0.2", "0.1"
        pos_hint: {"x":0.8,"y":0.9}

<Sat_Screen>:

""")

class LineRectangle(Label):
    pass

class CustomLabel_green(Label):
    background_color = (0, 1, 0, 1)

class CustomLabel_red(Label):
    background_color = (1, 0, 0, 1)
    
class CustomLabel(Label):
    background_color = ListProperty([1, 1, 1, 1])

class CustomBoxLayout(BoxLayout):
    background_color = ListProperty([1, 1, 1, 1])
    
class EllipseLabel(Label):
    pass

class MenuScreen(Screen):
    button_transformations_in_main_menu = StringProperty('Dyadische Formeln\n(S•P <-> S•P)')
    button_conclusion_in_main_menu = StringProperty('Verlängerte dyadische Formeln\n(M•P, S•M -> S•P)')
    button_total_formulas_in_main_menu = StringProperty('Triadische Ganzformeln\n(M•P, S•M, S•P <-> S•M•P)')


    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)

class GeneralScreen(Screen):
    pass

class Menu_introductionScreen(Screen):
    pass

class Menu_introductionScreen_1(Screen):
    
    def change_screen_menu(self, *args):
        self.parent.current = 'menu'
    
    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        
        self.layout = GridLayout(cols=1, spacing=70, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        
        self.text_1 = Label(text='[u]Die logischen Prinzipien:[/u]\n\n"Die logischen Prinzipien sind Grundbestimmungen, die für das in der Logik Festgesetzte gelten. Sie beruhen selbst auf Festsetzung.\nFür die Strenge Logik sind zwei Prinzipien festzusetzen: Das Prinzip der Identität und das Prinzip der Limitation.\n\n\n[u]Das Prinzip der Identiät[/u]:\n\nPositive Formulierung:\nJedes in der Logik Festgesetzte ist mit sich selbst und nur mit sich selbst identisch.\n\nNegativeFormulierung:\n(Satz vom ausgeschlossenen Widerspruch)\nKein in der Logik Festgesetztes ist mit sich selbst nicht identisch (d. h. steht mit sich selbst im Widerspruch).\nKein Festgesetztes ist mit anderem identisch.\n(Diese letzte Bestimmung kann als Satz der ausgeschlossenen Fremdidentifizierung bezeichnet werden).\n\n\n[u]Das Prinzip der Limitation[/u]:\n\nPositive Formulierung:\nJedes Festgesetzte ist\n1. von den anderen\n2. aber auch nur von den anderen limitativ unterschieden.\n\nNegative Formulierung:\n1. Kein Festgesetztes ist von den anderen nicht limitativ unterschieden. D. h. zwischen einem Festgesetzten und den anderen gibt es nicht Drittes (Satz vom ausgeschlossenen Dritten).\n2. Kein Festgesetztes ist von sich selbst limitativ unterschieden (Satz der ausgeschlossenen Selbstlimitation)." (Grundlagen der Strengen Logik, Seite 58f)', size_hint_y=None)
        self.text_1.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_1.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.text_1.markup = True
        self.layout.add_widget(self.text_1)
        
        #table "B, ~B":
        self.box_layout_introduction_formulas_0 = BoxLayout(orientation='horizontal', size_hint_y=None)
        self.layout.add_widget(self.box_layout_introduction_formulas_0)

        self.syllogism_box_1_col_0 = BoxLayout(orientation='vertical', size_hint_y=None)
        self.box_layout_introduction_formulas_0.add_widget(self.syllogism_box_1_col_0)

        self.s_1_0 = Label(text=' ')
        self.syllogism_box_1_col_0.add_widget(self.s_1_0)
        self.p_1_0 = Label(text=' ')
        self.syllogism_box_1_col_0.add_widget(self.p_1_0)
        self.formula_1_1_label = Label(text='1.', font_name='my_custom_font')
        self.syllogism_box_1_col_0.add_widget(self.formula_1_1_label)
        self.formula_1_2_label = Label(text='2.', font_name='my_custom_font')
        self.syllogism_box_1_col_0.add_widget(self.formula_1_2_label)
        self.formula_1_3_label = Label(text='3.', font_name='my_custom_font')
        self.syllogism_box_1_col_0.add_widget(self.formula_1_3_label)
        self.formula_1_4_label = Label(text='4.', font_name='my_custom_font')
        self.syllogism_box_1_col_0.add_widget(self.formula_1_4_label)
        
        self.syllogism_box_1_col_1 = BoxLayout(orientation='vertical', size_hint_y=None)
        self.box_layout_introduction_formulas_0.add_widget(self.syllogism_box_1_col_1)

        self.s_1_1 = Label(text='B', font_name='my_custom_font')
        self.syllogism_box_1_col_1.add_widget(self.s_1_1)
        for r in range(2):
            self.button_1_1_A = CustomLabel_green(text='A',color= (0, 0, 0, 1), font_name= 'my_custom_font')
            self.syllogism_box_1_col_1.add_widget(self.button_1_1_A)
        for r in range(2):
            self.button_1_1_N = CustomLabel_red(text='N',color= (0, 0, 0, 1), font_name= 'my_custom_font')
            self.syllogism_box_1_col_1.add_widget(self.button_1_1_N)

        self.syllogism_box_1_col_2 = BoxLayout(orientation='vertical', size_hint_y=None)
        self.box_layout_introduction_formulas_0.add_widget(self.syllogism_box_1_col_2)

        self.s_1_2 = Label(text='~B', font_name='my_custom_font')
        self.syllogism_box_1_col_2.add_widget(self.s_1_2)
        for r in range(2):
            self.button_1_2_N = CustomLabel_red(text='N',color= (0, 0, 0, 1), font_name= 'my_custom_font')
            self.syllogism_box_1_col_2.add_widget(self.button_1_2_N)
            self.button_1_2_A = CustomLabel_green(text='A',color= (0, 0, 0, 1), font_name= 'my_custom_font')
            self.syllogism_box_1_col_2.add_widget(self.button_1_2_A)

        self.syllogism_box_1_col_3 = BoxLayout(orientation='vertical', size_hint_y=None)
        self.box_layout_introduction_formulas_0.add_widget(self.syllogism_box_1_col_3)

        self.dummy_1_1 = Label(text=' ')
        self.syllogism_box_1_col_3.add_widget(self.dummy_1_1)
        self.dummy_1_2 = Label(text=' ')
        self.syllogism_box_1_col_3.add_widget(self.dummy_1_2)
        self.dummy_1_3 = Label(text=' ')
        self.syllogism_box_1_col_3.add_widget(self.dummy_1_3)
        self.dummy_1_4 = Label(text=' ')
        self.syllogism_box_1_col_3.add_widget(self.dummy_1_4)
        self.dummy_1_5 = Label(text=' ')
        self.syllogism_box_1_col_3.add_widget(self.dummy_1_5)

        #text dummy 1
        self.text_2 = Label(text='')
        self.text_2.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_2.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.layout.add_widget(self.text_2)

        #text dummy 2
        self.text_3 = Label(text='')
        self.text_3.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_3.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.layout.add_widget(self.text_3)
        
        #text dummy 3
        self.text_4 = Label(text='')
        self.text_4.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_4.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.layout.add_widget(self.text_4)

        #table "BC, ~BC, B~C, ~B~C":
        self.box_layout_introduction_formulas = BoxLayout(orientation='horizontal', size_hint_y=None)
        self.layout.add_widget(self.box_layout_introduction_formulas)
        
        self.syllogism_box_2_col_0 = BoxLayout(orientation='vertical', size_hint_y=3.5)
        self.box_layout_introduction_formulas.add_widget(self.syllogism_box_2_col_0)

        self.s_2_0 = Label(text=' ')
        self.syllogism_box_2_col_0.add_widget(self.s_2_0)
        self.p_2_0 = Label(text=' ')
        self.syllogism_box_2_col_0.add_widget(self.p_2_0)
        self.dyadic_formulas_list = ['B#C', 'BÄC', 'BÖC', 'B&C', 'B@C', 'B%C', 'B$C', 'BÜC',\
                                "BÜ'C", "B$'C", "B%'C", "B@'C", "B&'C", "BÖ'C", "BÄ'C", "B#'C"]
        
        for i, dyadic_junctor in enumerate(self.dyadic_formulas_list):
            self.formula_BC_label = Label(text= dyadic_junctor, font_name='my_custom_font')
            self.syllogism_box_2_col_0.add_widget(self.formula_BC_label)

        self.syllogism_box_col_2_1 = BoxLayout(orientation='vertical', size_hint_y=3.5)
        self.box_layout_introduction_formulas.add_widget(self.syllogism_box_col_2_1)

        self.s1 = Label(text='B', font_name='my_custom_font')
        self.syllogism_box_col_2_1.add_widget(self.s1)
        self.p1 = Label(text='C', font_name='my_custom_font')
        self.syllogism_box_col_2_1.add_widget(self.p1)
        for r in range(8):
            self.button_2_1_A = CustomLabel_green(text='A',color= (0, 0, 0, 1), font_name= 'my_custom_font')
            self.syllogism_box_col_2_1.add_widget(self.button_2_1_A)
        for r in range(8):
            self.button_2_1_N = CustomLabel_red(text='N',color= (0, 0, 0, 1), font_name= 'my_custom_font')
            self.syllogism_box_col_2_1.add_widget(self.button_2_1_N)

        self.syllogism_box_2_col_2 = BoxLayout(orientation='vertical', size_hint_y=3.5)
        self.box_layout_introduction_formulas.add_widget(self.syllogism_box_2_col_2)

        self.s_2_1 = Label(text='~B', font_name='my_custom_font')
        self.syllogism_box_2_col_2.add_widget(self.s_2_1)
        self.p_2_2 = Label(text='C', font_name='my_custom_font')
        self.syllogism_box_2_col_2.add_widget(self.p_2_2)
        for r in range(4):
            for i in range(2):
                self.button_2_2_A = CustomLabel_green(text='A',color= (0, 0, 0, 1), font_name= 'my_custom_font')
                self.syllogism_box_2_col_2.add_widget(self.button_2_2_A)
            for j in range(2):
                self.button_2_2_N = CustomLabel_red(text='N',color= (0, 0, 0, 1), font_name= 'my_custom_font')
                self.syllogism_box_2_col_2.add_widget(self.button_2_2_N)

        self.syllogism_box_2_col_3 = BoxLayout(orientation='vertical', size_hint_y=3.5)
        self.box_layout_introduction_formulas.add_widget(self.syllogism_box_2_col_3)

        self.s_2_3 = Label(text='B', font_name='my_custom_font')
        self.syllogism_box_2_col_3.add_widget(self.s_2_3)
        self.s_2_4 = Label(text='~C', font_name='my_custom_font')
        self.syllogism_box_2_col_3.add_widget(self.s_2_4)
        for r in range(2):
            for i in range(4):
                self.button_2_3_A = CustomLabel_green(text='A',color= (0, 0, 0, 1), font_name= 'my_custom_font')
                self.syllogism_box_2_col_3.add_widget(self.button_2_3_A)
            for j in range(4):
                self.button_2_3_N = CustomLabel_red(text='N',color= (0, 0, 0, 1), font_name= 'my_custom_font')
                self.syllogism_box_2_col_3.add_widget(self.button_2_3_N)

        self.syllogism_box_2_col_4 = BoxLayout(orientation='vertical', size_hint_y=3.5)
        self.box_layout_introduction_formulas.add_widget(self.syllogism_box_2_col_4)

        self.s_2_4 = Label(text='~B', font_name='my_custom_font')
        self.syllogism_box_2_col_4.add_widget(self.s_2_4)
        self.p_2_4 = Label(text='~C', font_name='my_custom_font')
        self.syllogism_box_2_col_4.add_widget(self.p_2_4)
        for r in range(8):
            self.button_2_4_A = CustomLabel_green(text='A',color= (0, 0, 0, 1), font_name= 'my_custom_font')
            self.syllogism_box_2_col_4.add_widget(self.button_2_4_A)
            self.button_2_4_N = CustomLabel_red(text='N',color= (0, 0, 0, 1), font_name= 'my_custom_font')
            self.syllogism_box_2_col_4.add_widget(self.button_2_4_N)

        self.syllogism_box_2_col_5 = BoxLayout(orientation='vertical', size_hint_y=3.5)
        self.box_layout_introduction_formulas.add_widget(self.syllogism_box_2_col_5)

        self.dummy_1 = Label(text=' ')
        self.syllogism_box_2_col_5.add_widget(self.dummy_1)
        self.dummy_2 = Label(text=' ')
        self.syllogism_box_2_col_5.add_widget(self.dummy_2)
        self.dummy_3 = Label(text=' ')
        self.syllogism_box_2_col_5.add_widget(self.dummy_3)
        self.dummy_4 = Label(text=' ')
        self.syllogism_box_2_col_5.add_widget(self.dummy_4)

        #text dummy 1
        for r in range(77):
            self.text_5 = Label(text='')
            self.text_5.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
            self.text_5.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
            self.layout.add_widget(self.text_5)

        #function call to initalise first, to be able to access variable triadic_formulas_list in this function
        Clock.schedule_once(self.do_stuff)
        
        
        
        #table "BCD, ~BCD, B~CD, ~B~CD, BC~D, ~BC~D, B~C~D, ~B~C~D":
        
    def do_stuff(self, *args):
        
        screen_manager = self.manager
        window_one = screen_manager.get_screen('calculating_quiz')
        self.triadic_formulas_list = window_one.test
        
        
        self.box_layout_introduction_formulas_2 = BoxLayout(orientation='horizontal', size_hint_y=None)
        self.layout.add_widget(self.box_layout_introduction_formulas_2)
        
        self.syllogism_box_3_col_0 = BoxLayout(orientation='vertical', size_hint_y=55, size_hint_x=12)
        self.box_layout_introduction_formulas_2.add_widget(self.syllogism_box_3_col_0)
        
        self.s_3_0 = Label(text=' ')
        self.syllogism_box_3_col_0.add_widget(self.s_3_0)
        self.p_3_0 = Label(text=' ')
        self.syllogism_box_3_col_0.add_widget(self.p_3_0)
        self.m_3_0 = Label(text=' ')
        self.syllogism_box_3_col_0.add_widget(self.m_3_0)
        
        for i, triadic_formula in enumerate(self.triadic_formulas_list):
            if self.triadic_formulas_list[i][1] == 0:
                self.formula_BCD_label = Label(text= 'B§C§D '+str(i+1), font_name='my_custom_font')
                self.syllogism_box_3_col_0.add_widget(self.formula_BCD_label)
            else:
                if self.triadic_formulas_list[i][2][0] != [] and self.triadic_formulas_list[i][2][1] != []:
                    self.formula_BCD_label = Label(text= str(triadic_formula[1][0])+', '+str(triadic_formula[1][1])+', '+str(triadic_formula[1][2])+', '+str(triadic_formula[2][0][0])+', '+str(triadic_formula[2][1][0]), font_name='my_custom_font')
                    self.syllogism_box_3_col_0.add_widget(self.formula_BCD_label)
                elif self.triadic_formulas_list[i][2][1] != []:
                    self.formula_BCD_label = Label(text= str(triadic_formula[1][0])+', '+str(triadic_formula[1][1])+', '+str(triadic_formula[1][2])+', '+str(triadic_formula[2][0][0]), font_name='my_custom_font')
                    self.syllogism_box_3_col_0.add_widget(self.formula_BCD_label)
                else:
                    self.formula_BCD_label = Label(text= str(triadic_formula[1][0])+', '+str(triadic_formula[1][1])+', '+str(triadic_formula[1][2]), font_name='my_custom_font')
                    self.syllogism_box_3_col_0.add_widget(self.formula_BCD_label)
        
        b_list = []
        for b in range(4):
            b_list.append('B')
            b_list.append('~B')
            
        c_list = []
        for c in range(2):
            for x in range(2):
                c_list.append('C')
            for y in range(2):
                c_list.append('~C')
        
        d_list = []    
        for d in range(4):
            d_list.append('D')
        for d in range(4):
            d_list.append('~D')

        for i in range(8): 
            self.col_boxlayout = BoxLayout(orientation='vertical', size_hint_y=55)
            self.box_layout_introduction_formulas_2.add_widget(self.col_boxlayout)
            
                                                 
            self.s_3_1 = CustomLabel(text=b_list[i], background_color = [0, 0, 0, 1], font_name='my_custom_font')
            self.col_boxlayout.add_widget(self.s_3_1)
            self.p_3_1 = CustomLabel(text=c_list[i], background_color = [0, 0, 0, 1], font_name='my_custom_font')
            self.col_boxlayout.add_widget(self.p_3_1)
            self.m_3_1 = CustomLabel(text=d_list[i], background_color = [0, 0, 0, 1], font_name='my_custom_font')
            self.col_boxlayout.add_widget(self.m_3_1)

            for j, triadic_formula in enumerate(self.triadic_formulas_list):
                if triadic_formula[0][i] == 'a':
                    self.formula_BCD_label_x = CustomLabel_green(text= str(triadic_formula[0][i].upper()), font_name='my_custom_font', color = (0 ,0 ,0, 1))
                else:
                    self.formula_BCD_label_x = CustomLabel_red(text= str(triadic_formula[0][i].upper()), font_name='my_custom_font', color = (0 ,0 ,0, 1))
                self.col_boxlayout.add_widget(self.formula_BCD_label_x)


        self.menu_button = Button(text='Menü', background_normal= '', background_color=(1, 1, 1, .5), color=(0, 0, 0, 1), size_hint_y=None)
        self.layout.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.root = ScrollView(size=(Window.width, Window.height))
        self.root.add_widget(self.layout)
        self.add_widget(self.root)
        
class Menu_introductionScreen_1b(Screen):
    
    def change_screen_menu(self, *args):
        self.parent.current = 'menu'
    
    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        
        self.layout = GridLayout(cols=1, spacing=70, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        
        self.text_1 = Label(text='"Aus den beiden Prinzipien ergibt sich weiterhin:\n\n\nAnalytische (Identitäts-) Verhältnisse und synthetische Verbindungen sind scharf voneinander zu scheiden.\nEin Sachverhalt oder eine Sachverhaltsverbindung kann mit sich selbst nur durch das Identitätszeichen verknüpft werden, \nz. B. \n      B <-> B\n(BaC)<->(BaC)\n\nDie folgenden Verknüpfungen sind nicht zugelassen: \n           BaB\n (BaC) a (BaC) \nSie stellen Selbstlimitation dar.\n[...]\n\n\nEin Sachverhalt kann mit seinem Komplement gar nicht verknüpft werden. Hier besteht weder analytische noch synthetische Verknüpfung. \nHier besteht nur komplementäre Limitation. \nEs gilt aber: \nB <-> ~~B\n[...]" (Grundlagen der Strengen Logik, S.60f)\n\n\n', size_hint_y=None)
        self.text_1.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_1.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.layout.add_widget(self.text_1)

        self.menu_button = Button(text='Menü', background_normal= '', background_color=(1, 1, 1, .5), color=(0, 0, 0, 1), size_hint_y=None)
        self.layout.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        
        self.root = ScrollView(size=(Window.width, Window.height))
        self.root.add_widget(self.layout)
        self.add_widget(self.root)
        
class Menu_introductionScreen_2(Screen):
    
    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        
        self.layout = GridLayout(cols=1, spacing=13, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))
        
        self.text_1 = Label(text='Die logischen Prinzipien: \n\nAm Anfang des logischen Denkens ist alles eins (A\u00A5A\u00A5):', font_name= 'my_custom_font', size_hint_y = None)
        self.text_1.markup = True
        self.text_1.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_1.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        
        self.layout.add_widget(self.text_1)

        self.box_b_not_b = BoxLayout(orientation= 'horizontal', size_hint_y=None)

        self.box_1_1 = BoxLayout(orientation= 'vertical', size_hint_y=None, size_hint_x=None)
        self.box_b_not_b.add_widget(self.box_1_1)

        self.label_box_0_0_1 = Button(text= 'B', background_normal= '', background_color=(.5, .5, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_1_1.add_widget(self.label_box_0_0_1)
        self.label_box_0_0_2 = Button(text= 'A\u00A5', background_normal= '', background_color=(1, 1, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_1_1.add_widget(self.label_box_0_0_2)

        self.box_1_2 = BoxLayout(orientation= 'vertical', size_hint_y=None, size_hint_x=None)
        self.box_b_not_b.add_widget(self.box_1_2)

        self.label_box_0_1_1 = Button(text= '~B', background_normal= '', background_color=(.5, .5, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_1_2.add_widget(self.label_box_0_1_1)
        self.label_box_0_1_2 = Button(text= 'A\u00A5', background_normal= '', background_color=(1, 1, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_1_2.add_widget(self.label_box_0_1_2)

        self.layout.add_widget(self.box_b_not_b)
        
        self.text_2 = Label(text='\n\n\n1. [u]Die erste Stufe[/u]: \nDer Unterschied der durch gleichzeitige Anwendung der beiden logischen Prinzipien (das Prinzip der Identität und das Prinzip der Limitation) definiert wird, teilt das Eins in Zwei. Es entstehen vier Möglichkeiten, die sich alle ausschließen. Zudem entstehen Kollektiv-Kennzeichnungen (Au und uN bzw. Nu und uA (unmittelbare Schlüsse)):', size_hint_y = None)
        self.text_2.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_2.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.text_2.markup = True
        self.layout.add_widget(self.text_2)
        
        self.box_1 = BoxLayout(orientation= 'horizontal', size_hint_y=None)

        self.box_2 = BoxLayout(orientation= 'vertical', size_hint_y=None, size_hint_x=None)
        self.box_1.add_widget(self.box_2)

        self.label_box_1_1 = Button(text= 'B', background_normal= '', background_color=(.5, .5, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_2.add_widget(self.label_box_1_1)
        self.label_box_1_2 = Button(text= 'A', background_normal= '', background_color=(0, 1, 0, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_2.add_widget(self.label_box_1_2)
        self.label_box_1_3 = Button(text= 'u', background_normal= '', background_color=(1, 1, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_2.add_widget(self.label_box_1_3)
        self.label_box_1_4 = Button(text= 'N', background_normal= '', background_color=(1, 0, 0, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_2.add_widget(self.label_box_1_4)
        self.label_box_1_5 = Button(text= 'u', background_normal= '', background_color=(1, 1, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_2.add_widget(self.label_box_1_5)

        self.box_3 = BoxLayout(orientation= 'vertical', size_hint_y=None, size_hint_x=None)
        self.box_1.add_widget(self.box_3)

        self.label_box_2_1 = Button(text= '~B', background_normal= '', background_color=(.5, .5, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_3.add_widget(self.label_box_2_1)
        self.label_box_2_2 = Button(text= 'u', background_normal= '', background_color=(1, 1, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_3.add_widget(self.label_box_2_2)
        self.label_box_2_3 = Button(text= 'N', background_normal= '', background_color=(1, 0, 0, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_3.add_widget(self.label_box_2_3)
        self.label_box_2_4 = Button(text= 'u', background_normal= '', background_color=(1, 1, 1, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_3.add_widget(self.label_box_2_4)
        self.label_box_2_5 = Button(text= 'A', background_normal= '', background_color=(0, 1, 0, 1), color=(0, 0, 0, 1), font_name= 'my_custom_font')
        self.box_3.add_widget(self.label_box_2_5)

        self.box_4 = BoxLayout(orientation= 'vertical', size_hint_x= .4, size_hint_y=None)
        self.box_1.add_widget(self.box_4)

        self.label_box_3_1 = Label(text= ' ', size_hint_y= .2)
        self.box_4.add_widget(self.label_box_3_1)
        self.label_box_3_2 = LineRectangle(text= 'A\u00A5', size_hint_y= .4, font_name= 'my_custom_font')
        self.box_4.add_widget(self.label_box_3_2)
        self.label_box_3_3 = LineRectangle(text= 'A\u00A5', size_hint_y= .4, font_name= 'my_custom_font')
        
        self.box_4.add_widget(self.label_box_3_3)

        self.box_5 = BoxLayout(orientation= 'vertical', size_hint_x= .4, size_hint_y=None)
        self.box_1.add_widget(self.box_5)

        self.label_box_4_1 = Label(text= ' ', size_hint_y= .2)
        self.box_5.add_widget(self.label_box_4_1)
        self.label_box_4_2 = LineRectangle(text= 'A\u00A5', size_hint_y= .8, font_name= 'my_custom_font')
        self.box_5.add_widget(self.label_box_4_2)
        
        self.layout.add_widget(self.box_1)
        
        self.text_3 = Label(text='Unmittelbare Schlüsse (auf derselben Stufe): \n\n   a) [u]Ganzformel -> Ganzformel[/u] \nAN -> Au \nNN -> uN \nusw. \n\nAus der Annahme\n  "Es gibt keine Nicht-Menschen." (uN)\nfolgt nicht:\n  "Es gibt Menschen." (Au)\n\n\n2. [u]Die zweite Stufe[/u]: \nDer Unterschied der durch gleichzeitige Anwendung der beiden logischen Prinzipien definiert wird, teilt das Zwei in Vier. Ab nun überschneiden sich Begriffe. Jetzt sind es Zwei. Es entstehen 16 Möglichkeiten, die sich alle ausschließen. Werden unbestimmte Geltungswertstellen erlaubt, entstehen unmittelbare Schlüsse zwischen Stufen: \n\nUnmittelbare Schlüsse zwischen Stufen: \n\n   b) [u]Ganzformel -> Teilformeln[/u]: \nANNA -> auau \n            -> aauu \n\n   c) [u]Teilformeln -> Ganzformel[/u]: \nuaua und \nuuaa und \nnunu und \nnnuu        -> NNNA \n\nZum Beispiel folgt aus: "Einige p sind q." (Auuu, piq)\n-->p (auau)\n-->q (aauu).\n\n[Und unmittelbare Schlüsse auf derselben (dyadischen) Stufe:] \n\n   •) Ganzformel -> Ganzformel \nSubalternation; Konversion, Obversion, Kontraposition, Partielle Inversion, Inversion; \n   •) Ganzformel <-> Ganzformel \nKontradiktorischer Widerspruch, Konträrer Widerspruch, Subkontrarietät \n\n\n3. [u]Die dritte Stufe[/u]: \nDer Unterschied der durch gleichzeitige Anwendung der beiden logischen Prinzipien definiert wird, teilt das Vier in Acht. Jetzt überschneiden sich drei Begriffe. Es entstehen 256 Möglichkeiten, die sich alle ausschließen. Werden unbestimmte Geltungswertstellen erlaubt, entstehen mittelbare Schlüsse innerhalb einer Stufe (z. B. die traditionelle (und die vollständige traditionelle) Syllogistik): \n\nMittelbare Schlüsse innerhalb einer Stufe (über Mittelbegriff): \n\n   d) [u]Teilformeln -> Teilformel[/u]: \naauunnaa und \naunaauna           -> auaunana \n\n\n\nMittelbar innerhalb einer Stufe kann erst ab dritter Stufe geschlossen werden. Dies geschieht über einen Mittelbegriff. Dabei werden die Geltungswertstellen und die dazugehörigen Geltungswerte jeweils um den sozusagen unbeteiligten Begriff verlängert. Aus zwei Formeln (zum Beispiel kategorische Urteile), folgt eine dritte Formel (zum Beispiel ein kategorisches Urteil):\n\nMaP, SaM -> SaP (Barbara). (Siehe "Ressourcen" -> "Strenge Syllogistik")', size_hint_y=None)
        self.text_3.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_3.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.text_3.markup = True
        self.layout.add_widget(self.text_3)

        self.menu_button = Button(text='Menü', background_normal= '', background_color=(1, 1, 1, .5), color=(0, 0, 0, 1), size_hint_y=None)
        self.layout.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.root = ScrollView(size=(Window.width, Window.height))
        self.root.add_widget(self.layout)
        self.add_widget(self.root)
        
class Menu_introductionScreen_3(Screen):
    pass
    
"""    def change_screen_menu(self, *args):
        self.parent.current = 'menu'
        
    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        
        self.layout = GridLayout(cols=1, spacing=13, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))
        
        self.text_1 = Label(text='[u]Das Problem der Wahrheit[/u] \n\n"Ein [...] Problem [...] der Angewandten Logik überhaupt ist das der Wahrheit, d. h. der Richtigkeit im außerformalen Sinn. \nDafür gilt: Aus wahren Prämissen können sich (formallogisch korrekt) nur wahre Konklusionen ergeben. \n Wahre Konklusionen können aber unter Umständen auch aus falschen Prämissen folgen. \nz. B. \n   Alle Steine sind Lebewesen (f) \n   [u]Alle Menschen sind Steine (f)[/u] \n   Alle Menschen sind Lebewesen (w) \n[...]" \n(Grundlagen der Strengen Logik, S.161) \n\n\n[u]Transgressives Denken[/u] \n"[...] Ist für die Zukunft zu fordern, daß transgressives Denken grundsätzlich vermieden wird? Nicht unbedingt; unbekannte Bereiche sollte man möglichst weiterer Forschung zugänglich machen. Versuche mit Widerspruchsdialektiken und Selbstlimitationskonstruktionen können vielleicht ihre fruchtbaren Aspekte haben, aber nur dann, wenn sie von einem festen Ausgangspunkt unternommen werden. Sonst gerät man in willkürliche Kombinatorik und leere Spielerei." (Grundlagen der Strengen Logik, S. 223)', size_hint_y = None)
        self.text_1.markup = True
        self.text_1.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_1.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        
        self.layout.add_widget(self.text_1)
        
        self.menu_button = Button(text='Menü', background_normal= '', background_color=(1, 1, 1, .5), color=(0, 0, 0, 1), size_hint_y=None)
        self.layout.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.root = ScrollView(size=(Window.width, Window.height))
        self.root.add_widget(self.layout)
        self.add_widget(self.root)"""
        
class Menu_conclusion_introductionScreen(Screen):
    pass

class Table_overviewScreen(Screen):

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'
 
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.layout = GridLayout(cols= 9, pos_hint= {'y': .075}, size_hint_y= .925)
        
        list_text = ['M•P,', 'SaM', 'SäM', 'SeM', 'SëM', 'SiM', 'SïM', 'SoM', 'SöM',
                     'S•M', ' ', ' ', ' ', '<=>', ' ', '<=>', ' ', ' ',
                     '->S•P', ' ', ' ', ' ', 'MeS', ' ', 'MiS', ' ', ' ',
                     'MaP', 'a', 'i', 'ö', 'ë', 'i', '-', '-', 'ö',
                     ' ', '->i', ' ', ' ', '->o', ' ', ' ', ' ', ' ',
                     ' ', '->ï', ' ', ' ', '->ö', ' ', ' ', ' ', ' ',
                     'MäP', 'ï', 'ä', 'e', 'o', '-', 'ï', 'o', '-',
                     ' ', ' ', '->i', '->o', ' ', ' ', ' ', ' ', ' ',
                     ' ', ' ', '->ï', '->ö', ' ', ' ', ' ', ' ', ' ',
                     'MeP', 'e', 'o', 'ï', 'ä', 'o', '-', '-', 'ï',
                     ' ', '->o', ' ', ' ', '->i', ' ', ' ', ' ', ' ',
                     ' ', '->ö', ' ', ' ', '->ï', ' ', ' ', ' ', ' ',
                     'MëP', 'ö', 'ë', 'a', 'i', '-', 'ö', 'i', '-',
                     '<=>', ' ', '->o', '->i', ' ', ' ', ' ', ' ', ' ',
                     'PeM', ' ', '->ö', '->ï', ' ', ' ', ' ', ' ', ' ',
                     'MiP', '-', 'i', 'ö', '-', '-', '-', '-', '-',
                     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                     'MïP', 'ï', '-', '-', 'o', '-', '-', '-', '-',
                     '<=>', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                     'PiM', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                     'MoP', '-', 'o', 'ï', '-', '-', '-', '-', '-',
                     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                     'MöP', 'ö', '-', '-', 'i', '-', '-', '-', '-',
                     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
                     ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        
        for r in range(1,244):
            lbl = Button(color= (0, 0, 0, 1), background_normal= '', text=(list_text[r-1]))
            self.layout.add_widget(lbl)

            if r==2 or r==3 or r==4 or r==5 or r==6 or r==7 or r==8 or r==9 or\
            r==11 or r==12 or r==13 or r==14 or r==15 or r==16 or r==17 or r==18 or\
            r==20 or r==21 or r==22 or r==23 or r==24 or r==25 or r==26 or r==27 or\
            r==28 or r==37 or r==46 or r==55 or r==64 or r==73 or r==82 or r==91 or\
            r==100 or r==109 or r==118 or r==127 or r==136 or r==145 or r==154 or r==163 or\
            r==172 or r==181 or r==190 or r==199 or r==208 or r==217 or r==226 or r==235:
                lbl.background_color=(.7, .6, 1, 1) #synthetic judges
                
            elif r==29 or r==30 or r==31 or r==32 or r==33 or r==34 or r==35 or r==36 or\
            r==56 or r==57 or r==58 or r==59 or r==60 or r==61 or r==62 or r==63 or\
            r==83 or r==84 or r==85 or r==86 or r==87 or r==88 or r==89 or r==90 or\
            r==110 or r==111 or r==112 or r==113 or r==114 or r==115 or r==116 or r==117 or\
            r==137 or r==138 or r==139 or r==140 or r==141 or r==142 or r==143 or r==144 or\
            r==164 or r==165 or r==166 or r==167 or r==168 or r==169 or r==170 or r==171 or\
            r==191 or r==192 or r==193 or r==194 or r==195 or r==196 or r==197 or r==198 or\
            r==218 or r==219 or r==220 or r==221 or r==222 or r==223 or r==224 or r==225:
                lbl.background_color=(.2, 7, .5, 1) #conclusion judges
                
            elif r==38 or r==41 or r==47 or r==50 or r==66 or r==67 or r==75 or r==76 or\
            r==92 or r==95 or r==101 or r==104 or r==120 or r==121 or r==129 or r==130:
                lbl.background_color=(.7, 1, .2, 1) #subaltern conclusion judges

        self.box_layout_menu_button = BoxLayout(orientation='horizontal', size_hint_y= .075)

        self.menu_button = Button(text='Menü', background_normal= '', background_color=(1, 1, 1, .5),color=(0, 0, 0, 1))
        self.box_layout_menu_button.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)        

        self.add_widget(self.layout)
        self.add_widget(self.box_layout_menu_button)

class Table_overviewScreen_2(Screen):

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'
        
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        #self.layout = GridLayout(cols= 9, pos_hint= {'y': .075}, size_hint_y= .925)

        #function call to initalise first, to be able to access variable triadic_formulas_list in this function
        Clock.schedule_once(self.do_stuff)
        
        
        #table "BCD, ~BCD, B~CD, ~B~CD, BC~D, ~BC~D, B~C~D, ~B~C~D":
        
    def do_stuff(self, *args):
        
        screen_manager = self.manager
        window_one = screen_manager.get_screen('calculating_quiz')
        self.enlonged_list = window_one.enlonged_list

        self.dyadic_formulas_list_2 = ['B#C', 'BÄC', 'BÖC', 'B&C', 'B@C', 'B%C', 'B$C', 'BÜC',\
                                "BÜ'C", "B$'C", "B%'C", "B@'C", "B&'C", "BÖ'C", "BÄ'C", "B#'C"]

        self.dyadic_formulas_list = ['C#D', 'CÄD', 'C@D', 'C%D', 'CÖD', 'C&D', 'C$D', 'CÜD',\
                                "CÜ'D", "C$'D",  "C&'D", "CÖ'D","C%'D", "C@'D", "CÄ'D", "C#'D"]
                
#1.2
        self.layout = BoxLayout(orientation= 'horizontal', size_hint_x= 1, size_hint_y=1)
        

        
        self.col_1 = BoxLayout(orientation= 'vertical', size_hint_y= 1, size_hint_x=1)
        self.layout.add_widget(self.col_1)
        
        self.figure_one_box = BoxLayout(orientation= 'vertical', size_hint_y= 1, size_hint_x=1)
        self.col_1.add_widget(self.figure_one_box)
        
        self.first_figure_label_one = Label(text= 'B§C,', font_name= 'my_custom_font')
        self.figure_one_box.add_widget(self.first_figure_label_one)
        self.first_figure_label_two = Label(text= 'C§D', font_name= 'my_custom_font')
        self.figure_one_box.add_widget(self.first_figure_label_two)
        self.first_figure_label_three = Label(text= '->B§D', font_name= 'my_custom_font')
        self.figure_one_box.add_widget(self.first_figure_label_three)
        
        
        
        for i in range(len(self.dyadic_formulas_list)):
            self.label_test = Label(text= self.dyadic_formulas_list[i], font_name= 'my_custom_font')
            self.col_1.add_widget(self.label_test)
        
        count_1 = 0
        
        for j in range(len(self.dyadic_formulas_list)):

            self.col_x = BoxLayout(orientation= 'vertical', size_hint_y= 1, size_hint_x=1)
            self.layout.add_widget(self.col_x)
            self.c_d = Label(text= self.dyadic_formulas_list_2[j], font_name= 'my_custom_font')
            self.col_x.add_widget(self.c_d)
            #self.label_test = Label(text= self.dyadic_formulas_list[k], font_name= 'my_custom_font')
            #self.col_x.add_widget(self.label_test)

            for i in range(len(self.enlonged_list)):
                #print(self.enlonged_list[i][0])
            
                if self.enlonged_list[i][0][1] == self.dyadic_formulas_list_2[j]:
                    for k in range(len(self.dyadic_formulas_list_2)):
                        if self.enlonged_list[i][0][0] == self.dyadic_formulas_list[k]:
                            count_1 = count_1 + 1
                            
                            #print(self.enlonged_list[i])
                            if self.enlonged_list[i][1][1] != [0]:
                                self.label_test_2 = CustomLabel_red(text= str(len(self.enlonged_list[i][1][1])), font_name= 'my_custom_font')
                            elif self.enlonged_list[i][0][2] == None:
                                self.label_test_2 = CustomLabel(text= 'u', background_color = [1, .3, .3, 1], font_name= 'my_custom_font')
                            elif self.enlonged_list[i][1][0].count('u') > 0 and self.enlonged_list[i][0][2] != None:
                                self.label_test_2 = CustomLabel(text= str(self.enlonged_list[i][0][2]), background_color = [.3, 1, .3, .7], font_name= 'my_custom_font')
                            else:
                                self.label_test_2 = CustomLabel_green(text= str(self.enlonged_list[i][0][2]), font_name= 'my_custom_font', color= (0, 0, 0, 1))
                            self.col_x.add_widget(self.label_test_2)
                            
                            #print(count_1, j, k, self.enlonged_list[i])


        
        #for r, bd in enumerate(self.dyadic_formulas_list):
        #    lbl = Label(text= bd, font_name = 'my_custom_font')
        #for r in range(1,244):
        #    lbl = Button(color= (0, 0, 0, 1), background_normal= '', text=(list_text[r-1]), font_name= 'my_custom_font')
        #    self.layout.add_widget(lbl)
        
        self.box_layout_menu_button = BoxLayout(orientation='horizontal')

        self.menu_button = Button(text='Menü', background_normal= '', background_color=(1, 1, 1, .5),color=(0, 0, 0, 1))
        self.box_layout_menu_button.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)        

        #self.add_widget(self.layout)
        self.layout.add_widget(self.box_layout_menu_button)

        self.root = ScrollView(size=(Window.width, Window.height))
        self.root.add_widget(self.layout)
        self.add_widget(self.root)
        
class TrainingScreen(Screen):
    global foo_1
    global active_4_dummy
    
    foo_1 = []
    active_4_dummy = False
    
    def dyadic_name_first_formula(self, formula):
        if formula == ['a', 'u', 'n', 'a']: # traditionelle Syllogistik
            return "MaP"
        elif formula == ['n', 'a', 'a', 'u']:
            return "MeP"
        elif formula == ['a', 'u', 'n', 'a']:
            return "MiP"
        elif formula == ['u', 'u', 'a', 'u']:
            return "MoP"
        elif formula == ['a', 'n', 'u', 'a']:
            return "PaM"
        elif formula == ['n', 'a', 'a', 'u']:
            return "PeM"
        elif formula == ['a', 'u', 'u', 'u']:
            return "PiM"
        elif formula == ['u', 'a', 'u', 'u']:
            return "PoM"
        elif formula == ['a', 'n', 'u', 'a']:
            return "MãP" # vervollständigte Syllogistik
        elif formula == ['u', 'a', 'a', 'n']:
            return "MëP"
        elif formula == ['u', 'u', 'u', 'a']:
            return "MïP"
        elif formula == ['u', 'a', 'u', 'u']:
            return "MõP"
        elif formula == ['a', 'u', 'n', 'a']:
            return "PãM"
        elif formula == ['u', 'a', 'a', 'n']:
            return "PëM"
        elif formula == ['u', 'u', 'u', 'a']:
            return "PïM"
        elif formula == ['u', 'u', 'a', 'u']:
            return "PõM"
        elif formula == ['a', 'a', 'a', 'a']: # Dyadische Formeln
            return "P#M"
        elif formula == ['a', 'a', 'a', 'n']:
            return "PÄM"
        elif formula == ['a', 'n', 'a', 'a']:
            return "PÖM"
        elif formula == ['a', 'n', 'a', 'n']:
            return "P&M"
        elif formula == ['a', 'a', 'n', 'a']:
            return "P@M"
        elif formula == ['a', 'a', 'n', 'n']:
            return "P%M"
        elif formula == ['a', 'n', 'n', 'a']:
            return "P$M"
        elif formula == ['a', 'n', 'n', 'n']:
            return "PÜM"
        elif formula == ['n', 'a', 'a', 'a']:
            return "PÜ'M"
        elif formula == ['n', 'a', 'a', 'n']:
            return "P$'M"
        elif formula == ['n', 'n', 'a', 'a']:
            return "P%'M"
        elif formula == ['n', 'n', 'a', 'n']:
            return "P@'M"
        elif formula == ['n', 'a', 'n', 'a']:
            return "P&'M"
        elif formula == ['n', 'a', 'n', 'n']:
            return "PÖ'M"
        elif formula == ['n', 'n', 'n', 'a']:
            return "PÄ'M"
        elif formula == ['n', 'n', 'n', 'n']:
            return "P#'M"
        elif formula == ['a', 'u', 'a', 'u']: # erweiterte Syllogistik (naheliegend)
            return "MioP"
        elif formula == ['a', 'a', 'u', 'u']:
            return "MiõP"
        elif formula == ['u', 'a', 'a', 'u']:
            return "MoõP"
        elif formula == ['u', 'u', 'a', 'a']:
            return "MoïP"
        elif formula == ['u', 'a', 'u', 'a']:
            return "MõïP"
        elif formula == ['a', 'u', 'a', 'a']: # erweiterte Syllogistik (sogar)
            return "MioïP"
        elif formula == ['a', 'a', 'u', 'a']:
            return "MiõïP"
        elif formula == ['a', 'a', 'a', 'a']:
            return "MiõoïP"
        else:
            return " "
        
    def dyadic_name_second_formula(self, formula):
        if formula == ['a', 'u', 'n', 'a']: # traditionelle Syllogistik
            return "SaM"
        elif formula == ['n', 'a', 'a', 'u']:
            return "SeM"
        elif formula == ['a', 'u', 'n', 'a']:
            return "SiM"
        elif formula == ['u', 'u', 'a', 'u']:
            return "SoM"
        elif formula == ['a', 'n', 'u', 'a']:
            return "MaS"
        elif formula == ['n', 'a', 'a', 'u']:
            return "MeS"
        elif formula == ['a', 'u', 'u', 'u']:
            return "MiS"
        elif formula == ['u', 'a', 'u', 'u']:
            return "MoS"
        elif formula == ['a', 'n', 'u', 'a']:
            return "SãM" # vervollständigte Syllogistik
        elif formula == ['u', 'a', 'a', 'n']:
            return "SëM"
        elif formula == ['u', 'u', 'u', 'a']:
            return "SïM"
        elif formula == ['u', 'a', 'u', 'u']:
            return "MõM"
        elif formula == ['a', 'u', 'n', 'a']:
            return "MãS"
        elif formula == ['u', 'a', 'a', 'n']:
            return "MëS"
        elif formula == ['u', 'u', 'u', 'a']:
            return "MïS"
        elif formula == ['u', 'u', 'a', 'u']:
            return "MõS"
        elif formula == ['a', 'a', 'a', 'a']: # Dyadische Formeln
            return "M#S"
        elif formula == ['a', 'a', 'a', 'n']:
            return "MÄS"
        elif formula == ['a', 'n', 'a', 'a']:
            return "MÖS"
        elif formula == ['a', 'n', 'a', 'n']:
            return "M&S"
        elif formula == ['a', 'a', 'n', 'a']:
            return "M@S"
        elif formula == ['a', 'a', 'n', 'n']:
            return "M%S"
        elif formula == ['a', 'n', 'n', 'a']:
            return "M$S"
        elif formula == ['a', 'n', 'n', 'n']:
            return "MÜS"
        elif formula == ['n', 'a', 'a', 'a']:
            return "MÜ'S"
        elif formula == ['n', 'a', 'a', 'n']:
            return "M$'S"
        elif formula == ['n', 'n', 'a', 'a']:
            return "M%'S"
        elif formula == ['n', 'n', 'a', 'n']:
            return "M@'S"
        elif formula == ['n', 'a', 'n', 'a']:
            return "M&'S"
        elif formula == ['n', 'a', 'n', 'n']:
            return "MÖ'S"
        elif formula == ['n', 'n', 'n', 'a']:
            return "MÄ'S"
        elif formula == ['n', 'n', 'n', 'n']:
            return "M#'S"
        elif formula == ['a', 'u', 'a', 'u']: # erweiterte Syllogistik (naheliegend)
            return "SioM"
        elif formula == ['a', 'a', 'u', 'u']:
            return "SiõM"
        elif formula == ['u', 'a', 'a', 'u']:
            return "SoõM"
        elif formula == ['u', 'u', 'a', 'a']:
            return "SoïM"
        elif formula == ['u', 'a', 'u', 'a']:
            return "SõïM"
        elif formula == ['a', 'u', 'a', 'a']: # erweiterte Syllogistik (sogar)
            return "SioïM"
        elif formula == ['a', 'a', 'u', 'a']:
            return "SiõïM"
        elif formula == ['a', 'a', 'a', 'a']:
            return "SiõoïM"
        else:
            return " "
        
    def dyadic_name_third_formula(self, formula):
        if formula == ['a', 'u', 'n', 'a']: # traditionelle Syllogistik
            return "SaP"
        elif formula == ['n', 'a', 'a', 'u']:
            return "SeP"
        elif formula == ['a', 'u', 'n', 'a']:
            return "SiP"
        elif formula == ['u', 'u', 'a', 'u']:
            return "SoP"
        elif formula == ['a', 'n', 'u', 'a']:
            return "PaS"
        elif formula == ['n', 'a', 'a', 'u']:
            return "PeS"
        elif formula == ['a', 'u', 'u', 'u']:
            return "PiS"
        elif formula == ['u', 'a', 'u', 'u']:
            return "PoS"
        elif formula == ['a', 'n', 'u', 'a']:
            return "SãP" # vervollständigte Syllogistik
        elif formula == ['u', 'a', 'a', 'n']:
            return "SëP"
        elif formula == ['u', 'u', 'u', 'a']:
            return "SïP"
        elif formula == ['u', 'a', 'u', 'u']:
            return "SõP"
        elif formula == ['a', 'u', 'n', 'a']:
            return "PãS"
        elif formula == ['u', 'a', 'a', 'n']:
            return "PëS"
        elif formula == ['u', 'u', 'u', 'a']:
            return "PïS"
        elif formula == ['u', 'u', 'a', 'u']:
            return "PõS"
        elif formula == ['a', 'a', 'a', 'a']:
            return "S#P"
        elif formula == ['a', 'a', 'a', 'n']:
            return "SÄP"
        elif formula == ['a', 'n', 'a', 'a']:
            return "SÖP"
        elif formula == ['a', 'n', 'a', 'n']:
            return "S&P"
        elif formula == ['a', 'a', 'n', 'a']:
            return "S@P"
        elif formula == ['a', 'a', 'n', 'n']:
            return "S%P"
        elif formula == ['a', 'n', 'n', 'a']:
            return "S$P"
        elif formula == ['a', 'n', 'n', 'n']:
            return "SÜP"
        elif formula == ['n', 'a', 'a', 'a']:
            return "SÜ'P"
        elif formula == ['n', 'a', 'a', 'n']:
            return "S$'P"
        elif formula == ['n', 'n', 'a', 'a']:
            return "S%'P"
        elif formula == ['n', 'n', 'a', 'n']:
            return "S@'P"
        elif formula == ['n', 'a', 'n', 'a']:
            return "S&'P"
        elif formula == ['n', 'a', 'n', 'n']:
            return "SÖ'P"
        elif formula == ['n', 'n', 'n', 'a']:
            return "SÄ'P"
        elif formula == ['n', 'n', 'n', 'n']:
            return "S#'P"
        elif formula == ['a', 'u', 'a', 'u']: # erweiterte Syllogistik
            return "PioS"
        elif formula == ['a', 'a', 'u', 'u']:
            return "PiõS"
        elif formula == ['u', 'a', 'a', 'u']:
            return "PoõS"
        elif formula == ['u', 'u', 'a', 'a']:
            return "PoïS"
        elif formula == ['u', 'a', 'u', 'a']:
            return "PõïS"
        else:
            return " "

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
        elif premis_one == "MëP" and premis_two == "SeM":  # example-sentences - completed syllogistic (page 127 - "Einführung in die formale Logik")
            return ("Wenn alle Nicht-Mitglieder doppelten Eintritt bezahlen und \nkeine Frau Mitglied ist, \nso bezahlen alle Frauen doppelten Eintritt.")
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
        if first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] != "n":
            return ("a")
        elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
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
        if first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] != "n":
            return ("a")
        elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
            return ("a")
        else:
            return ("u")

    def syllogism_deduction_first_value_a_contradiction(self, first_formula, second_formula):
        if first_formula[0] == "a" and second_formula[1] == "n" and second_formula[
            0] == "n":  # calculates potential "a"-values of first value
            self.error_number_enlonged.append([[0], [0]])
        if second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
            self.error_number_enlonged.append([[1], [0]])
        if first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
            self.error_number_enlonged.append([[0], [1]])
        if second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
            self.error_number_enlonged.append([[1], [2]])

    def syllogism_deduction_second_value_a_contradiction(self, first_formula, second_formula):
        if first_formula[0] == "a" and second_formula[0] == "n" and second_formula[1] == "n":  # calculates potential "a"-values of second value
            self.error_number_enlonged.append([[0], [0]])
        if second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
            self.error_number_enlonged.append([[1], [1]])
        if first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
            self.error_number_enlonged.append([[0], [1]])
        if second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
            self.error_number_enlonged.append([[1], [3]])

    def syllogism_deduction_third_value_a_contradiction(self, first_formula, second_formula):
        if first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] == "n":
            self.error_number_enlonged.append([[0], [2]])
        if second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
            self.error_number_enlonged.append([[1], [0]])
        if first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
            self.error_number_enlonged.append([[0], [3]])
        if second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
            self.error_number_enlonged.append([[1], [2]])
        
    def syllogism_deduction_fourth_value_a_contradiction(self, first_formula, second_formula):
        if first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] == "n":
            self.error_number_enlonged.append([[0], [2]])
        if second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
            self.error_number_enlonged.append([[1], [1]])
        if first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
            self.error_number_enlonged.append([[0], [3]])
        if second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
            self.error_number_enlonged.append([[1], [3]])

    def syllogism_contradiction_test(self, first_formula, second_formula):
        self.error_number_enlonged = []
        conclusion = [0, 0, 0, 0, 0, 0, 0, 0]
        conclusion[0] = self.syllogism_deduction_first_value_n(first_formula, second_formula)
        conclusion_1_contradiction_value = self.syllogism_deduction_first_value_a_contradiction(first_formula, second_formula)
        conclusion[1] = conclusion_1_contradiction_value
        if conclusion[0] == 'n' and conclusion[1] == 'a':
            self.syllogism_deduction_first_value_a_contradiction(first_formula, second_formula)
        conclusion[2]  = self.syllogism_deduction_second_value_n(first_formula, second_formula)
        conclusion_3_contradiction_value = self.syllogism_deduction_second_value_a_contradiction(first_formula, second_formula)
        conclusion[3] = conclusion_3_contradiction_value
        if conclusion[2] == 'n' and conclusion[3] == 'a':
            self.syllogism_deduction_second_value_a_contradiction(first_formula, second_formula)
        conclusion[4] = self.syllogism_deduction_third_value_n(first_formula, second_formula)
        conclusion_5_contradiction_value = self.syllogism_deduction_third_value_a_contradiction(first_formula, second_formula)
        conclusion[5] = conclusion_5_contradiction_value
        if conclusion[4] == 'n' and conclusion[5] == 'a':
            self.syllogism_deduction_third_value_a_contradiction(first_formula, second_formula)
        conclusion[6] = self.syllogism_deduction_fourth_value_n(first_formula, second_formula)
        conclusion_7_contradiction_value = self.syllogism_deduction_fourth_value_a_contradiction(first_formula, second_formula)
        conclusion[7] = conclusion_7_contradiction_value
        if conclusion[6] == 'n' and conclusion[7] == 'a':
            self.syllogism_deduction_fourth_value_a_contradiction(first_formula, second_formula)
        if (len(self.error_number_enlonged) != 0):
            return self.error_number_enlonged[:]
        else:
            return ([0])


    def syllogism_deduction_first_value(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of first value
            self.n_goes_into_conclusion.append([[0], [0]])
            self.n_goes_into_conclusion.append([[0], [2]])
            return ("n")
        elif second_formula[0] == "n" and first_formula[1] == "n":
            self.n_goes_into_conclusion.append([[1], [0]])
            self.n_goes_into_conclusion.append([[0], [2]])
            return ("n")
        elif first_formula[0] == "n" and second_formula[2] == "n":
            self.n_goes_into_conclusion.append([[0], [0]])
            self.n_goes_into_conclusion.append([[1], [2]])
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            self.n_goes_into_conclusion.append([[1], [0]])
            self.n_goes_into_conclusion.append([[1], [2]])
            return ("n")
        elif first_formula[0] == "a" and second_formula[1] == "n" and second_formula[
            0] != "n":  # calculates potential "a"-values of first value
            self.a_goes_into_conclusion.append([[0], [0]]) # first value: first or second premis, second value: from [0] to [7]
            return ("a")
        elif second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] != "n":
            self.a_goes_into_conclusion.append([[1], [0]])
            return ("a")
        elif first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
            self.a_goes_into_conclusion.append([[0], [2]])
            return ("a")
        elif second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] != "n":
            self.a_goes_into_conclusion.append([[1], [2]])
            return ("a")
        else:  # calculates potential "u"-values of first value
            return ("u")

    def syllogism_deduction_second_value(self, first_formula, second_formula):
        if first_formula[0] == "n" and first_formula[1] == "n":  # caluculates potential "n"-values of second value
            self.n_goes_into_conclusion.append([[0], [1]])
            self.n_goes_into_conclusion.append([[0], [3]])
            return ("n")
        elif second_formula[1] == "n" and first_formula[1] == "n":
            self.n_goes_into_conclusion.append([[1], [1]])
            self.n_goes_into_conclusion.append([[0], [3]])
            return ("n")
        elif first_formula[0] == "n" and second_formula[3] == "n":
            self.n_goes_into_conclusion.append([[0], [1]])
            self.n_goes_into_conclusion.append([[1], [3]])
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            self.n_goes_into_conclusion.append([[1], [1]])
            self.n_goes_into_conclusion.append([[1], [3]])
            return ("n")
        elif first_formula[0] == "a" and second_formula[0] == "n" and second_formula[
            1] != "n":  # calculates potential "a"-values of second value
            self.a_goes_into_conclusion.append([[0], [1]])
            return ("a")
        elif second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] != "n":
            self.a_goes_into_conclusion.append([[1], [1]])
            return ("a")
        elif first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
            self.a_goes_into_conclusion.append([[0], [3]])
            return ("a")
        elif second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] != "n":
            self.a_goes_into_conclusion.append([[1], [3]])
            return ("a")
        else:  # calculates potential "u"-values of second value
            return ("u")

    def syllogism_deduction_third_value(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            self.n_goes_into_conclusion.append([[0], [4]])
            self.n_goes_into_conclusion.append([[0], [6]])
            return ("n")
        elif second_formula[0] == "n" and first_formula[3] == "n":
            self.n_goes_into_conclusion.append([[1], [4]])
            self.n_goes_into_conclusion.append([[0], [6]])
            return ("n")
        elif first_formula[2] == "n" and second_formula[2] == "n":
            self.n_goes_into_conclusion.append([[0], [4]])
            self.n_goes_into_conclusion.append([[1], [6]])
            return ("n")
        elif second_formula[0] == "n" and second_formula[2] == "n":
            self.n_goes_into_conclusion.append([[1], [4]])
            self.n_goes_into_conclusion.append([[1], [6]])
            return ("n")
        elif first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] != "n":
            self.a_goes_into_conclusion.append([[0], [4]])
            return ("a")
        elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            self.a_goes_into_conclusion.append([[1], [4]])
            return ("a")
        elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
            self.a_goes_into_conclusion.append([[0], [6]])
            return ("a")
        elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
            self.a_goes_into_conclusion.append([[1], [6]])
            return ("a")
        else:
            return ("u")

    def syllogism_deduction_fourth_value(self, first_formula, second_formula):
        if first_formula[2] == "n" and first_formula[3] == "n":
            self.n_goes_into_conclusion.append([[0], [5]])
            self.n_goes_into_conclusion.append([[0], [7]])
            return ("n")
        elif second_formula[1] == "n" and first_formula[3] == "n":
            self.n_goes_into_conclusion.append([[1], [5]])
            self.n_goes_into_conclusion.append([[0], [7]])
            return ("n")
        elif first_formula[2] == "n" and second_formula[3] == "n":
            self.n_goes_into_conclusion.append([[0], [5]])
            self.n_goes_into_conclusion.append([[1], [7]])
            return ("n")
        elif second_formula[1] == "n" and second_formula[3] == "n":
            self.n_goes_into_conclusion.append([[1], [5]])
            self.n_goes_into_conclusion.append([[1], [7]])
            return ("n")
        elif first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] != "n":
            self.a_goes_into_conclusion.append([[0], [5]])
            return ("a")
        elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            self.a_goes_into_conclusion.append([[1], [5]])
            return ("a")
        elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
            self.a_goes_into_conclusion.append([[0], [7]])
            return ("a")
        elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
            self.a_goes_into_conclusion.append([[1], [7]])
            return ("a")
        else:
            return ("u")

    def syllogism_solution(self,first_formula, second_formula):
        self.a_goes_into_conclusion = []
        self.n_goes_into_conclusion = []
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
                self.btn_1_p1.background_color=(1, 0, 0, 1)
                self.btn_2_p1.text ='n'
                self.btn_2_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_1_p1.text ='a'
                self.btn_1_p1.background_color=(0, 1, 0, 1)
                self.btn_2_p1.text ='a'
                self.btn_2_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_1_p1.text ='u'
                self.btn_1_p1.background_color=(1, 1, 1, 1)
                self.btn_2_p1.text ='u'
                self.btn_2_p1.background_color=(1, 1, 1, 1)
        elif len(foo_1) == 1:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_3_p1.text ='n'
                self.btn_3_p1.background_color=(1, 0, 0, 1)
                self.btn_4_p1.text ='n'
                self.btn_4_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_3_p1.text ='a'
                self.btn_3_p1.background_color=(0, 1, 0, 1)
                self.btn_4_p1.text ='a'
                self.btn_4_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_3_p1.text ='u'
                self.btn_3_p1.background_color=(1, 1, 1, 1)
                self.btn_4_p1.text ='u'
                self.btn_4_p1.background_color=(1, 1, 1, 1)
        elif len(foo_1) == 2:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_5_p1.text ='n'
                self.btn_5_p1.background_color=(1, 0, 0, 1)
                self.btn_6_p1.text ='n'
                self.btn_6_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_5_p1.text ='a'
                self.btn_5_p1.background_color=(0, 1, 0, 1)
                self.btn_6_p1.text ='a'
                self.btn_6_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_5_p1.text ='u'
                self.btn_5_p1.background_color=(1, 1, 1, 1)
                self.btn_6_p1.text ='u'
                self.btn_6_p1.background_color=(1, 1, 1, 1)
        elif len(foo_1) == 3:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_7_p1.text ='n'
                self.btn_7_p1.background_color=(1, 0, 0, 1)
                self.btn_8_p1.text ='n'
                self.btn_8_p1.background_color=(1, 0, 0, 1)
                self.first_formula = foo_1
                button.bind(on_release=self.rename_fn)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_7_p1.text ='a'
                self.btn_7_p1.background_color=(0, 1, 0, 1)
                self.btn_8_p1.text ='a'
                self.btn_8_p1.background_color=(0, 1, 0, 1)
                self.first_formula = foo_1
                button.bind(on_release=self.rename_fn)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_7_p1.text ='u'
                self.btn_7_p1.background_color=(1, 1, 1, 1)
                self.btn_8_p1.text ='u'
                self.btn_8_p1.background_color=(1, 1, 1, 1)
                self.first_formula = foo_1
                button.bind(on_release=self.rename_fn)
        elif len(foo_1) == 4:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_1_p2.text ='n'
                self.btn_1_p2.background_color=(1, 0, 0, 1)
                self.btn_5_p2.text ='n'
                self.btn_5_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_1_p2.text ='a'
                self.btn_1_p2.background_color=(0, 1, 0, 1)
                self.btn_5_p2.text ='a'
                self.btn_5_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_1_p2.text ='u'
                self.btn_1_p2.background_color=(1, 1, 1, 1)
                self.btn_5_p2.text ='u'
                self.btn_5_p2.background_color=(1, 1, 1, 1)
        elif len(foo_1) == 5:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_2_p2.text ='n'
                self.btn_2_p2.background_color=(1, 0, 0, 1)
                self.btn_6_p2.text ='n'
                self.btn_6_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_2_p2.text ='a'
                self.btn_2_p2.background_color=(0, 1, 0, 1)
                self.btn_6_p2.text ='a'
                self.btn_6_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_2_p2.text ='u'
                self.btn_2_p2.background_color=(1, 1, 1, 1)
                self.btn_6_p2.text ='u'
                self.btn_6_p2.background_color=(1, 1, 1, 1)
        elif len(foo_1) == 6:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_3_p2.text ='n'
                self.btn_3_p2.background_color=(1, 0, 0, 1)
                self.btn_7_p2.text ='n'
                self.btn_7_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_3_p2.text ='a'
                self.btn_3_p2.background_color=(0, 1, 0, 1)
                self.btn_7_p2.text ='a'
                self.btn_7_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_3_p2.text ='u'
                self.btn_3_p2.background_color=(1, 1, 1, 1)
                self.btn_7_p2.text ='u'
                self.btn_7_p2.background_color=(1, 1, 1, 1)
        elif len(foo_1) == 7:
            if button == self.btn_n:
                z = foo_1.append('n')
                self.btn_4_p2.text ='n'
                self.btn_4_p2.background_color=(1, 0, 0, 1)
                self.btn_8_p2.text ='n'
                self.btn_8_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_1.append('a')
                self.btn_4_p2.text ='a'
                self.btn_4_p2.background_color=(0, 1, 0, 1)
                self.btn_8_p2.text ='a'
                self.btn_8_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_1.append('u')
                self.btn_4_p2.text ='u'
                self.btn_4_p2.background_color=(1, 1, 1, 1)
                self.btn_8_p2.text ='u'
                self.btn_8_p2.background_color=(1, 1, 1, 1)
        if len(foo_1) == 8:
            self.second_formula = foo_1[4:8]
            self.premis_two_label.text = self.dyadic_name_second_formula(self.second_formula)
            self.btn_n.disabled = True
            self.btn_a.disabled = True
            self.btn_u.disabled = True
            self.click(button)
            foo_1.clear()

    def rename_fn(self, button):
        self.premis_one_label.text = self.dyadic_name_first_formula(self.first_formula)
        button.unbind(on_release=self.rename_fn)

    def draw(self):
        self.line.points = [
            self.width*0.1,
            self.height*.7,
            self.width*0.2,
            self.height*.7
        ]

    def right_answer(self, button):
        right_label = Label(color= (0, 1, 0, 1), text='Right!', size_hint=(.5, .3), pos_hint={'x': .25, 'y': .2})
        self.add_widget(right_label)

    def wrong_answer(self, button):
        wrong_label = Label(color= (1, 0, 0, 1), text='Wrong!', size_hint=(.5, .3), pos_hint={'x': .25, 'y': .15})
        self.add_widget(wrong_label)


    def on_checkbox_Active_3(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active_example.text = self.syllogism_example_text
        else:
            self.lbl_active_example.text = "OFF"
        
    def on_checkbox_Active_4(self, checkboxInstance, isActive):
        global active_4_dummy
        
        active_4_dummy = isActive
        
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
        self.error_number_enlonged.clear()
        self.a_goes_into_conclusion.clear()
        self.n_goes_into_conclusion.clear()
        
        self.menu_button = Button(text='Menü', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .9})
        self.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.settings_button = Button(text='Einstellungen', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .7})
        self.add_widget(self.settings_button)
        self.settings_button.bind(on_press=self.open_settings)
        

        
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



    def refresh_function(self, *args):
        global active_4_dummy

        completedsyllogistic = self.function_completed_syllogistic_settings()#looks for setting
        particularpremis = self.function_particularpremis_settings()#looks for setting

        if completedsyllogistic == 1:
            a = random.randint(0, 15)
            b = random.randint(0, 15)
            if particularpremis == 0: 
                while (((a == 4) or (a == 5) or (a == 6) or (a == 7) or (a == 12) or (a == 13) or (a == 14) or (a == 15)) and ((b == 4) or (b == 5) or (b == 6) or (b == 7) or (b == 12) or (b == 13) or (b == 14) or (b == 15))):
                    a = random.randint(0, 15)
                    b = random.randint(0, 15)
            self.refresh2_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
            self.add_widget(self.refresh2_button)
            self.refresh2_button.bind(on_press=lambda x:self.refresh_function(a, b))
        else:
            a = random.randint(0, 7)
            b = random.randint(0, 7)
            if particularpremis == 0:
                while (((a == 4) or (a == 5) or (a == 6) or (a == 7)) and ((b == 4) or (b == 5) or (b == 6) or (b == 7))):
                    a = random.randint(0, 7)
                    b = random.randint(0, 7)
            self.refresh2_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
            self.add_widget(self.refresh2_button)
            self.refresh2_button.bind(on_press=lambda x:self.refresh_function(a, b))

        judges_premis_one = ["MaP", "MeP", "PaM", "PeM", "MiP", "MoP", "PiM", "PoM",  #traditionelle Syllogistik
                             "MãP", "MëP",  "PãM", "PëM", "MïP", "MõP","PïM", "PõM"]  #vervollständigte Syllogistik
        judges_premis_second = ["SaM", "SeM", "MaS", "MeS", "MiS", "MoS","SiM", "SoM", #traditionelle Syllogistik
                                "SãM", "SëM", "MãS", "MëS", "SïM", "SõM", "MïS", "MõS"] #vervollständigte Syllogistik
        

        
        second_formula = judges_premis_second[a]
        self.my_text2 = second_formula
        first_formula = judges_premis_one[b]
        self.my_text = first_formula

        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        
        self.function_output_list = self.output2(self.my_text, self.my_text2)
        
        syllogism_example_text = self.syllogism_example_function(self.my_text, self.my_text2, self.function_output_list[3])
        self.syllogism_example_text = syllogism_example_text

        self.label_first_premis = Label(text='')
        self.label_second_premis = Label(text='')
        self.label_questionmark = Label(text='?')

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
        
        horizontal_up.add_widget(Label(text='Syllogism-\nTrainer'))
        horizontal_up.add_widget(Label(text=' '))
        
        self.boxlayout_up = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.boxlayout_up)

        self.checkboxes_BoxLayout = BoxLayout(orientation='horizontal')
        self.boxlayout_up.add_widget(self.checkboxes_BoxLayout)

        self.boxlayout_Checkbox_3 = BoxLayout(orientation='vertical')
        self.checkboxes_BoxLayout.add_widget(self.boxlayout_Checkbox_3)
        self.boxlayout_Checkbox_4 = BoxLayout(orientation='vertical')
        self.checkboxes_BoxLayout.add_widget(self.boxlayout_Checkbox_4)
        
        self.dummy_label_checkboxes_BoxLayout_right = Label(text= ' ')
        self.checkboxes_BoxLayout.add_widget(self.dummy_label_checkboxes_BoxLayout_right)
        
        
        self.label_example = Label(text='Example:')
        self.label_sentences = Label(text='Sentences')
        
        self.active_3 = CheckBox(active=False)

        self.checkbox_4_dummy_label = Label(text='')

        self.boxlayout_Checkbox_3.add_widget(self.label_example)
        self.boxlayout_Checkbox_3.add_widget(self.active_3)
        self.boxlayout_Checkbox_4.add_widget(self.label_sentences)
        self.boxlayout_Checkbox_4.add_widget(self.checkbox_4_dummy_label)
        

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
        
        self.premis_one_label = Label(text='Erste Prämisse', size_hint_x = 2.0, font_name = 'my_custom_font')
        self.syllogism_box_row_4.add_widget(self.premis_one_label)

        self.btn_1_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_1_p1)
        self.btn_2_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_2_p1)
        self.btn_3_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_3_p1)
        self.btn_4_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_4_p1)
        self.btn_5_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_5_p1)
        self.btn_6_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_6_p1)
        self.btn_7_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_7_p1)
        self.btn_8_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_8_p1)
        
        self.buttons_premis_one = [self.btn_1_p1, self.btn_2_p1, self.btn_3_p1, self.btn_4_p1, \
                                   self.btn_5_p1, self.btn_6_p1, self.btn_7_p1, self.btn_8_p1]

        self.syllogism_box_row_5 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_5)
        
        self.premis_two_label = Label(text='Zweite Prämisse', size_hint_x = 2.0, font_name = 'my_custom_font')
        self.syllogism_box_row_5.add_widget(self.premis_two_label)

        self.btn_1_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_1_p2)
        self.btn_2_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_2_p2)
        self.btn_3_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_3_p2)
        self.btn_4_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_4_p2)
        self.btn_5_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_5_p2)
        self.btn_6_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_6_p2)
        self.btn_7_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_7_p2)
        self.btn_8_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_8_p2)
        
        self.buttons_premis_two = [self.btn_1_p2, self.btn_2_p2, self.btn_3_p2, self.btn_4_p2, \
                                   self.btn_5_p2, self.btn_6_p2, self.btn_7_p2, self.btn_8_p2]
        
        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.conclusion_label = Label(text='Konklusion', size_hint_x = 2.0, font_name = 'my_custom_font')
        self.syllogism_box_row_6.add_widget(self.conclusion_label)

        self.btn_1_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_c)
        self.btn_2_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_c)
        self.btn_3_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_c)
        self.btn_4_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_c)
        self.btn_5_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_c)
        self.btn_6_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_c)
        self.btn_7_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_c)
        self.btn_8_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_c)
        
        self.buttons_conclusion = [self.btn_1_c, self.btn_2_c, self.btn_3_c, self.btn_4_c,\
                                   self.btn_5_c, self.btn_6_c, self.btn_7_c, self.btn_8_c]

        self.syllogism_box_row_7 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_7)
        
        self.solution_label = Label(text='Lösung', size_hint_x = 2.0, font_name = 'my_custom_font')
        self.syllogism_box_row_7.add_widget(self.solution_label)

        self.btn_1_s = Button(color= (0, 0, 0, 1))
        self.syllogism_box_row_7.add_widget(self.btn_1_s)
        self.btn_2_s = Button(color= (0, 0, 0, 1))
        self.syllogism_box_row_7.add_widget(self.btn_2_s)
        self.btn_3_s = Button(color= (0, 0, 0, 1))
        self.syllogism_box_row_7.add_widget(self.btn_3_s)
        self.btn_4_s = Button(color= (0, 0, 0, 1))
        self.syllogism_box_row_7.add_widget(self.btn_4_s)
        self.btn_5_s = Button(color= (0, 0, 0, 1))
        self.syllogism_box_row_7.add_widget(self.btn_5_s)
        self.btn_6_s = Button(color= (0, 0, 0, 1))
        self.syllogism_box_row_7.add_widget(self.btn_6_s)
        self.btn_7_s = Button(color= (0, 0, 0, 1))
        self.syllogism_box_row_7.add_widget(self.btn_7_s)
        self.btn_8_s = Button(color= (0, 0, 0, 1))
        self.syllogism_box_row_7.add_widget(self.btn_8_s)

        self.buttons_solution = [self.btn_1_s, self.btn_2_s, self.btn_3_s, self.btn_4_s,\
                                 self.btn_5_s, self.btn_6_s, self.btn_7_s, self.btn_8_s]
        
        self.answer_buttons_and_advices = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.answer_buttons_and_advices)

        self.answer_buttons = BoxLayout(orientation='vertical', size_hint_x = .75)
        self.answer_buttons_and_advices.add_widget(self.answer_buttons)
        
        self.button1 = Button()
        self.button2 = Button()
        self.button3 = Button()

        self.answer_buttons.add_widget(self.button1)
        self.answer_buttons.add_widget(self.button2)
        self.answer_buttons.add_widget(self.button3)

        self.buttons = [self.button1, self.button2, self.button3]
        correct_answer = random.randrange(len(self.buttons))

        button_text = self.function_output_list[0]
        
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

        self.lbl_active_example = Label(text="Example OFF", font_size= 20)
        self.box_advices_and_example_BoxLayout.add_widget(self.lbl_active_example)

        self.box_horizontal_buttons_down = BoxLayout(orientation='horizontal', size_hint_y= .75)
        vertical.add_widget(self.box_horizontal_buttons_down)

        self.btn_n = Button(text='n', color= (0, 0, 0, 1), background_normal='', background_color=(1, 0, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_n)
        variable_btn_n ='n'
        self.btn_n.bind(on_press=self.append_function)

        self.btn_a = Button(text='a', color= (0, 0, 0, 1), background_normal='', background_color=(0, 1, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_a)
        variable_btn_a ='a'
        self.btn_a.bind(on_press=self.append_function)

        self.btn_u = Button(text='u', color= (0, 0, 0, 1), background_normal='', background_color=(1, 1, 1, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_u)
        variable_btn_u ='u'
        self.btn_u.bind(on_press=self.append_function)
  
        self.refresh2_button.bind(on_press=self.clear_widgets_function)

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def click(self,my_button2):
        my_text = self.first_formula
        first_formula = my_text
        my_text2 = self.second_formula
        second_formula = my_text2[:]
        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        function_output_list = self.output2(my_text, my_text2)
        formulas_list_first_premis = first_formula[0:4][:]
        print(formulas_list_first_premis)
        print(second_formula)
        formulas_list = [formulas_list_first_premis, second_formula]
        print(function_output_list[3])

        solution = [self.function_output_list[3][0][:], self.function_output_list[3][1][:], self.function_output_list[3][0][:], self.function_output_list[3][1][:], \
            self.function_output_list[3][2][:], self.function_output_list[3][3][:], self.function_output_list[3][2][:], self.function_output_list[3][3][:]] 
 
        self.conclusion_label.text = self.dyadic_name_third_formula(function_output_list[3])
        self.solution_label.text =  self.dyadic_name_third_formula(self.function_output_list[3])

        self.btn_1_c.text = function_output_list[3][0]
        self.btn_3_c.text = function_output_list[3][0]
        self.btn_2_c.text = function_output_list[3][1]
        self.btn_4_c.text = function_output_list[3][1]
        self.btn_5_c.text = function_output_list[3][2]
        self.btn_7_c.text = function_output_list[3][2]
        self.btn_6_c.text = function_output_list[3][3]
        self.btn_8_c.text = function_output_list[3][3]
        if function_output_list[3][0] == 'n':
            self.btn_1_c.background_color=(1, 0, 0, 1)
            self.btn_3_c.background_color=(1, 0, 0, 1)
        elif function_output_list[3][0] == 'a':
            self.btn_1_c.background_color=(0, 1, 0, 1)
            self.btn_3_c.background_color=(0, 1, 0, 1)
        elif function_output_list[3][0] == 'u':
            self.btn_1_c.background_color=(1, 1, 1, 1)
            self.btn_3_c.background_color=(1, 1, 1, 1)
        if function_output_list[3][1] == 'n':
            self.btn_2_c.background_color=(1, 0, 0, 1)
            self.btn_4_c.background_color=(1, 0, 0, 1)
        elif function_output_list[3][1] == 'a':
            self.btn_2_c.background_color=(0, 1, 0, 1)
            self.btn_4_c.background_color=(0, 1, 0, 1)
        elif function_output_list[3][1] == 'u':
            self.btn_2_c.background_color=(1, 1, 1, 1)
            self.btn_4_c.background_color=(1, 1, 1, 1)
        if function_output_list[3][2] == 'n':
            self.btn_5_c.background_color=(1, 0, 0, 1)
            self.btn_7_c.background_color=(1, 0, 0, 1)
        elif function_output_list[3][2] == 'a':
            self.btn_5_c.background_color=(0, 1, 0, 1)
            self.btn_7_c.background_color=(0, 1, 0, 1)
        elif function_output_list[3][2] == 'u':
            self.btn_5_c.background_color=(1, 1, 1, 1)
            self.btn_7_c.background_color=(1, 1, 1, 1)
        if function_output_list[3][3] == 'n':
            self.btn_6_c.background_color=(1, 0, 0, 1)
            self.btn_8_c.background_color=(1, 0, 0, 1)
        elif function_output_list[3][3] == 'a':
            self.btn_6_c.background_color=(0, 1, 0, 1)
            self.btn_8_c.background_color=(0, 1, 0, 1)
        elif function_output_list[3][3] == 'u':
            self.btn_6_c.background_color=(1, 1, 1, 1)
            self.btn_8_c.background_color=(1, 1, 1, 1)
        
        if function_output_list[4] == [0]:
            for r in range(len(self.a_goes_into_conclusion)):
                for s in range(8):
                    if self.a_goes_into_conclusion[r][0][0] == 0 and self.a_goes_into_conclusion[r][1][0] == s:
                        self.buttons_premis_one[s].underline = True
                    if self.a_goes_into_conclusion[r][0][0] == 1 and self.a_goes_into_conclusion[r][1][0] == s:
                        self.buttons_premis_two[s].underline = True
                        
            for r in range(len(self.n_goes_into_conclusion)):
                for s in range(8):
                    if self.n_goes_into_conclusion[r][0][0] == 0 and self.n_goes_into_conclusion[r][1][0] == s:
                        self.buttons_premis_one[s].underline = True
                    if self.n_goes_into_conclusion[r][0][0] == 1 and self.n_goes_into_conclusion[r][1][0] == s:
                        self.buttons_premis_two[s].underline = True
                        
        
        if function_output_list[4] != [0]:
            self.conclusion_label.text = "Widerspruch!"
            print(formulas_list)
            print(function_output_list[4])
            for r in range(len(function_output_list[4])):
                for s in range(4):
                    for t in range(2):
                        if function_output_list[4][r][0][0] == 0 and function_output_list[4][r][1][0] == s:
                            self.buttons_conclusion[(s+s)+t].background_color = (0, 0, 1, 1)
                            self.buttons_conclusion[(s+s)+t].text = str((s+s)+t+1)
                            self.buttons_premis_one[(s+s)+t].underline = True
                        if function_output_list[4][r][0][0] == 1 and function_output_list[4][r][1][0] == s:
                            print(t)
                            self.buttons_conclusion[s+4*t].background_color = (0, 0, 1, 1)
                            self.buttons_conclusion[s+4*t].text = str(s+4*t+1)
                            self.buttons_premis_two[s+4*t].underline = True
                            
        
        self.btn_1_s.text = self.function_output_list[3][0]
        self.btn_3_s.text = self.function_output_list[3][0]
        self.btn_2_s.text = self.function_output_list[3][1]
        self.btn_4_s.text = self.function_output_list[3][1]
        self.btn_5_s.text = self.function_output_list[3][2]
        self.btn_7_s.text = self.function_output_list[3][2]
        self.btn_6_s.text = self.function_output_list[3][3]
        self.btn_8_s.text = self.function_output_list[3][3]
        if self.function_output_list[3][0] == 'n':
            self.btn_1_s.background_color=(1, 0, 0, 1)
            self.btn_1_s.background_normal= ''
            self.btn_3_s.background_color=(1, 0, 0, 1)
            self.btn_3_s.background_normal= ''
        elif self.function_output_list[3][0] == 'a':
            self.btn_1_s.background_color=(0, 1, 0, 1)
            self.btn_1_s.background_normal= ''
            self.btn_3_s.background_color=(0, 1, 0, 1)
            self.btn_3_s.background_normal= ''
        elif self.function_output_list[3][0] == 'u':
            self.btn_1_s.background_color=(1, 1, 1, 1)
            self.btn_1_s.background_normal= ''
            self.btn_3_s.background_color=(1, 1, 1, 1)
            self.btn_3_s.background_normal= ''
        if self.function_output_list[3][1] == 'n':
            self.btn_2_s.background_color=(1, 0, 0, 1)
            self.btn_2_s.background_normal= ''
            self.btn_4_s.background_color=(1, 0, 0, 1)
            self.btn_4_s.background_normal= ''
        elif self.function_output_list[3][1] == 'a':
            self.btn_2_s.background_color=(0, 1, 0, 1)
            self.btn_2_s.background_normal= ''
            self.btn_4_s.background_color=(0, 1, 0, 1)
            self.btn_4_s.background_normal= ''
        elif self.function_output_list[3][1] == 'u':
            self.btn_2_s.background_color=(1, 1, 1, 1)
            self.btn_2_s.background_normal= ''
            self.btn_4_s.background_color=(1, 1, 1, 1)
            self.btn_4_s.background_normal= ''
        if self.function_output_list[3][2] == 'n':
            self.btn_5_s.background_color=(1, 0, 0, 1)
            self.btn_5_s.background_normal= ''
            self.btn_7_s.background_color=(1, 0, 0, 1)
            self.btn_7_s.background_normal= ''
        elif self.function_output_list[3][2] == 'a':
            self.btn_5_s.background_color=(0, 1, 0, 1)
            self.btn_5_s.background_normal= ''
            self.btn_7_s.background_color=(0, 1, 0, 1)
            self.btn_7_s.background_normal= ''
        elif self.function_output_list[3][2] == 'u':
            self.btn_5_s.background_color=(1, 1, 1, 1)
            self.btn_5_s.background_normal= ''
            self.btn_7_s.background_color=(1, 1, 1, 1)
            self.btn_7_s.background_normal= ''
        if self.function_output_list[3][3] == 'n':
            self.btn_6_s.background_color=(1, 0, 0, 1)
            self.btn_6_s.background_normal= ''
            self.btn_8_s.background_color=(1, 0, 0, 1)
            self.btn_8_s.background_normal= ''
        elif self.function_output_list[3][3] == 'a':
            self.btn_6_s.background_color=(0, 1, 0, 1)
            self.btn_6_s.background_normal= ''
            self.btn_8_s.background_color=(0, 1, 0, 1)
            self.btn_8_s.background_normal= ''
        elif self.function_output_list[3][3] == 'u':
            self.btn_6_s.background_color=(1, 1, 1, 1)
            self.btn_6_s.background_normal= ''
            self.btn_8_s.background_color=(1, 1, 1, 1)
            self.btn_8_s.background_normal= ''
        
        
        if self.function_output_list[4] != [0]:
            self.conclusion_label.text = "Contradiction!"
            for r in range(len(self.function_output_list[4])):
                for s in range(4):
                    for t in range(2):
                        if self.function_output_list[4][r][0][0] == 0 and self.function_output_list[4][r][1][0] == s:
                            self.buttons_solution[(s+s)+t].background_color = (0, 0, 1, 1)
                            self.buttons_solution[(s+s)+t].text = str((s+s)+t+1)
                        if self.function_output_list[4][r][0][0] == 1 and self.function_output_list[4][r][1][0] == s:
                            print(t)
                            self.buttons_solution[s+4*t].background_color = (0, 0, 1, 1)
                            self.buttons_solution[s+4*t].text = str(s+4*t+1)

    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)

        self.active_4 = CheckBox(active=False)
        self.add_widget(self.active_4)
        self.active_4.bind(active=self.on_checkbox_Active_4)

        self.active_4.pos_hint = {'x': .45, 'y': .6} # not beautiful code
        self.active_4.size_hint = (.1, .1)

        lambda x:self.clear_widgets_function

class Menu_conclusionsScreen(Screen):
    pass   

class ConclusionsScreen(Screen):
    pass
"""    global foo
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
        if first_formula[0] == "a" and second_formula[1] == "n":  # calculates potential "a"-values of first value
            return ("a")
        elif second_formula[0] == "a" and first_formula[2] == "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[3] == "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[3] == "n":
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
        if first_formula[0] == "a" and second_formula[0] == "n":  # calculates potential "a"-values of second value
            return ("a")
        elif second_formula[1] == "a" and first_formula[2] == "n":
            return ("a")
        elif first_formula[1] == "a" and second_formula[2] == "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[3] == "n":
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
        if first_formula[2] == "a" and second_formula[1] == "n":
            return ("a")
        elif second_formula[0] == "a" and first_formula[0] == "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[3] == "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[1] == "n":
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
        if first_formula[2] == "a" and second_formula[0] == "n":
            return ("a")
        elif second_formula[1] == "a" and first_formula[0] == "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[2] == "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[1] == "n":
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
        if foo == []:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_1_p1.text ='n'
                self.btn_1_p1.background_color=(1, 0, 0, 1)
                self.btn_2_p1.text ='n'
                self.btn_2_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_1_p1.text ='a'
                self.btn_1_p1.background_color=(0, 1, 0, 1)
                self.btn_2_p1.text ='a'
                self.btn_2_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_1_p1.text ='u'
                self.btn_1_p1.background_color=(1, 1, 1, 1)
                self.btn_2_p1.text ='u'
                self.btn_2_p1.background_color=(1, 1, 1, 1)
        elif len(foo) == 1:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_3_p1.text ='n'
                self.btn_3_p1.background_color=(1, 0, 0, 1)
                self.btn_4_p1.text ='n'
                self.btn_4_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_3_p1.text ='a'
                self.btn_3_p1.background_color=(0, 1, 0, 1)
                self.btn_4_p1.text ='a'
                self.btn_4_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_3_p1.text ='u'
                self.btn_3_p1.background_color=(1, 1, 1, 1)
                self.btn_4_p1.text ='u'
                self.btn_4_p1.background_color=(1, 1, 1, 1)
        elif len(foo) == 2:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_5_p1.text ='n'
                self.btn_5_p1.background_color=(1, 0, 0, 1)
                self.btn_6_p1.text ='n'
                self.btn_6_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_5_p1.text ='a'
                self.btn_5_p1.background_color=(0, 1, 0, 1)
                self.btn_6_p1.text ='a'
                self.btn_6_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_5_p1.text ='u'
                self.btn_5_p1.background_color=(1, 1, 1, 1)
                self.btn_6_p1.text ='u'
                self.btn_6_p1.background_color=(1, 1, 1, 1)
        elif len(foo) == 3:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_7_p1.text ='n'
                self.btn_7_p1.background_color=(1, 0, 0, 1)
                self.btn_8_p1.text ='n'
                self.btn_8_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_7_p1.text ='a'
                self.btn_7_p1.background_color=(0, 1, 0, 1)
                self.btn_8_p1.text ='a'
                self.btn_8_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_7_p1.text ='u'
                self.btn_7_p1.background_color=(1, 1, 1, 1)
                self.btn_8_p1.text ='u'
                self.btn_8_p1.background_color=(1, 1, 1, 1)
        elif len(foo) == 4:
            self.first_formula = foo
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_1_p2.text ='n'
                self.btn_1_p2.background_color=(1, 0, 0, 1)
                self.btn_5_p2.text ='n'
                self.btn_5_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_1_p2.text ='a'
                self.btn_1_p2.background_color=(0, 1, 0, 1)
                self.btn_5_p2.text ='a'
                self.btn_5_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_1_p2.text ='u'
                self.btn_1_p2.background_color=(1, 1, 1, 1)
                self.btn_5_p2.text ='u'
                self.btn_5_p2.background_color=(1, 1, 1, 1)
        elif len(foo) == 5:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_2_p2.text ='n'
                self.btn_2_p2.background_color=(1, 0, 0, 1)
                self.btn_6_p2.text ='n'
                self.btn_6_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_2_p2.text ='a'
                self.btn_2_p2.background_color=(0, 1, 0, 1)
                self.btn_6_p2.text ='a'
                self.btn_6_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_2_p2.text ='u'
                self.btn_2_p2.background_color=(1, 1, 1, 1)
                self.btn_6_p2.text ='u'
                self.btn_6_p2.background_color=(1, 1, 1, 1)
        elif len(foo) == 6:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_3_p2.text ='n'
                self.btn_3_p2.background_color=(1, 0, 0, 1)
                self.btn_7_p2.text ='n'
                self.btn_7_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_3_p2.text ='a'
                self.btn_3_p2.background_color=(0, 1, 0, 1)
                self.btn_7_p2.text ='a'
                self.btn_7_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_3_p2.text ='u'
                self.btn_3_p2.background_color=(1, 1, 1, 1)
                self.btn_7_p2.text ='u'
                self.btn_7_p2.background_color=(1, 1, 1, 1)
        elif len(foo) == 7:
            if button == self.btn_n:
                z = foo.append('n')
                self.btn_4_p2.text ='n'
                self.btn_4_p2.background_color=(1, 0, 0, 1)
                self.btn_8_p2.text ='n'
                self.btn_8_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo.append('a')
                self.btn_4_p2.text ='a'
                self.btn_4_p2.background_color=(0, 1, 0, 1)
                self.btn_8_p2.text ='a'
                self.btn_8_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo.append('u')
                self.btn_4_p2.text ='u'
                self.btn_4_p2.background_color=(1, 1, 1, 1)
                self.btn_8_p2.text ='u'
                self.btn_8_p2.background_color=(1, 1, 1, 1)
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
        
        self.label_1 = Label(size_hint_x = .02)
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
        
        self.premis_one_label = Label(text='Erste Prämisse', size_hint_x = 2.0)
        self.syllogism_box_row_4.add_widget(self.premis_one_label)

        self.btn_1_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_1_p1)
        self.btn_2_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_2_p1)
        self.btn_3_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_3_p1)
        self.btn_4_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_4_p1)
        self.btn_5_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_5_p1)
        self.btn_6_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_6_p1)
        self.btn_7_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_7_p1)
        self.btn_8_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_8_p1)

        self.syllogism_box_row_5 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_5)
        
        self.premis_two_label = Label(text='Zweite Prämisse', size_hint_x = 2.0)
        self.syllogism_box_row_5.add_widget(self.premis_two_label)

        self.btn_1_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_1_p2)
        self.btn_2_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_2_p2)
        self.btn_3_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_3_p2)
        self.btn_4_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_4_p2)
        self.btn_5_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_5_p2)
        self.btn_6_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_6_p2)
        self.btn_7_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_7_p2)
        self.btn_8_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_8_p2)
        
        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.conclusion_label = Label(text='Konklusion', size_hint_x = 2.0)
        self.syllogism_box_row_6.add_widget(self.conclusion_label)

        self.btn_1_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_c)
        self.btn_2_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_c)
        self.btn_3_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_c)
        self.btn_4_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_c)
        self.btn_5_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_c)
        self.btn_6_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_c)
        self.btn_7_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_c)
        self.btn_8_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_c)

        self.syllogism_box_col_2 = BoxLayout(orientation='vertical')
        vertical.add_widget(self.syllogism_box_col_2)

        self.label_5 = Label()
        vertical.add_widget(self.label_5)

        self.box_horizontal_buttons_down = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.box_horizontal_buttons_down)

        self.btn_n = Button(text='n', color= (0, 0, 0, 1), background_normal='', background_color=(1, 0, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_n)
        variable_btn_n ='n'
        self.btn_n.bind(on_press=self.append_function)

        self.btn_a = Button(text='a', color= (0, 0, 0, 1), background_normal='', background_color=(0, 1, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_a)
        variable_btn_a ='a'
        self.btn_a.bind(on_press=self.append_function)

        self.btn_u = Button(text='u', color= (0, 0, 0, 1), background_normal='', background_color=(1, 1, 1, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_u)
        variable_btn_u ='u'
        self.btn_u.bind(on_press=self.append_function)

        self.label_3 = Label(size_hint_x = .02)
        horizontal.add_widget(self.label_3)
        


        self.refresh_button.bind(on_press=self.clear_widgets_function)

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def clear_widgets_function(self, *args):
        self.clear_widgets()
        foo.clear()
        
        self.refresh2_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
        self.add_widget(self.refresh2_button)
        
        self.menu_button = Button(text='Menü', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .9})
        self.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.refresh2_button.bind(on_press=self.refresh_function)
        
        self.refresh2_button.bind(on_press=self.clear_widgets_function)

    def __init__(self,**kwargs):
        super (ConclusionsScreen,self).__init__(**kwargs)
        
        self.refresh_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
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
                self.btn_1_c.background_color=(1, 0, 0, 1)
                self.btn_3_c.background_color=(1, 0, 0, 1)
            elif function_output_list[3][0] == 'a':
                self.btn_1_c.background_color=(0, 1, 0, 1)
                self.btn_3_c.background_color=(0, 1, 0, 1)
            elif function_output_list[3][0] == 'u':
                self.btn_1_c.background_color=(1, 1, 1, 1)
                self.btn_3_c.background_color=(1, 1, 1, 1)
            if function_output_list[3][1] == 'n':
                self.btn_2_c.background_color=(1, 0, 0, 1)
                self.btn_4_c.background_color=(1, 0, 0, 1)
            elif function_output_list[3][1] == 'a':
                self.btn_2_c.background_color=(0, 1, 0, 1)
                self.btn_4_c.background_color=(0, 1, 0, 1)
            elif function_output_list[3][1] == 'u':
                self.btn_2_c.background_color=(1, 1, 1, 1)
                self.btn_4_c.background_color=(1, 1, 1, 1)
            if function_output_list[3][2] == 'n':
                self.btn_5_c.background_color=(1, 0, 0, 1)
                self.btn_7_c.background_color=(1, 0, 0, 1)
            elif function_output_list[3][2] == 'a':
                self.btn_5_c.background_color=(0, 1, 0, 1)
                self.btn_7_c.background_color=(0, 1, 0, 1)
            elif function_output_list[3][2] == 'u':
                self.btn_5_c.background_color=(1, 1, 1, 1)
                self.btn_7_c.background_color=(1, 1, 1, 1)
            if function_output_list[3][3] == 'n':
                self.btn_6_c.background_color=(1, 0, 0, 1)
                self.btn_8_c.background_color=(1, 0, 0, 1)
            elif function_output_list[3][3] == 'a':
                self.btn_6_c.background_color=(0, 1, 0, 1)
                self.btn_8_c.background_color=(0, 1, 0, 1)
            elif function_output_list[3][3] == 'u':
                self.btn_6_c.background_color=(1, 1, 1, 1)
                self.btn_8_c.background_color=(1, 1, 1, 1)"""

class Menu_total_formulas_Screen(Screen):
    label_left_menu_total_formulas = StringProperty('Verlängerte Formeln ->\nGanzformeln')
    label_right_menu_total_formulas = StringProperty('Ganzformeln ->\nVerlängerte Formeln')

    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)

class Training_calculating_quiz_Screen(Screen):

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
        if first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] != "n":
            return ("a")
        elif second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] != "n":
            return ("a")
        elif second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
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
        if first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] != "n":
            return ("a")
        elif second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] != "n":
            return ("a")
        elif first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] != "n":
            return ("a")
        elif second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] != "n":
            return ("a")
        else:
            return ("u")

    def syllogism_deduction_first_value_a_contradiction(self, first_formula, second_formula):
        if first_formula[0] == "a" and second_formula[1] == "n" and second_formula[
            0] == "n":  # calculates potential "a"-values of first value
            self.error_number_enlonged.append([[0], [0]])
        if second_formula[0] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
            self.error_number_enlonged.append([[1], [0]])
        if first_formula[1] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
            self.error_number_enlonged.append([[0], [1]])
        if second_formula[2] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
            self.error_number_enlonged.append([[1], [2]])

    def syllogism_deduction_second_value_a_contradiction(self, first_formula, second_formula):
        if first_formula[0] == "a" and second_formula[0] == "n" and second_formula[1] == "n":  # calculates potential "a"-values of second value
            self.error_number_enlonged.append([[0], [0]])
        if second_formula[1] == "a" and first_formula[2] == "n" and first_formula[0] == "n":
            self.error_number_enlonged.append([[1], [1]])
        if first_formula[1] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
            self.error_number_enlonged.append([[0], [1]])
        if second_formula[3] == "a" and first_formula[3] == "n" and first_formula[1] == "n":
            self.error_number_enlonged.append([[1], [3]])

    def syllogism_deduction_third_value_a_contradiction(self, first_formula, second_formula):
        if first_formula[2] == "a" and second_formula[1] == "n" and second_formula[0] == "n":
            self.error_number_enlonged.append([[0], [2]])
        if second_formula[0] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
            self.error_number_enlonged.append([[1], [0]])
        if first_formula[3] == "a" and second_formula[3] == "n" and second_formula[2] == "n":
            self.error_number_enlonged.append([[0], [3]])
        if second_formula[2] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
            self.error_number_enlonged.append([[1], [2]])
        
    def syllogism_deduction_fourth_value_a_contradiction(self, first_formula, second_formula):
        if first_formula[2] == "a" and second_formula[0] == "n" and second_formula[1] == "n":
            self.error_number_enlonged.append([[0], [2]])
        if second_formula[1] == "a" and first_formula[0] == "n" and first_formula[2] == "n":
            self.error_number_enlonged.append([[1], [1]])
        if first_formula[3] == "a" and second_formula[2] == "n" and second_formula[3] == "n":
            self.error_number_enlonged.append([[0], [3]])
        if second_formula[3] == "a" and first_formula[1] == "n" and first_formula[3] == "n":
            self.error_number_enlonged.append([[1], [3]])

    def syllogism_contradiction_test_enlonged(self, first_formula, second_formula):
        self.error_number_enlonged = []
        conclusion = [0, 0, 0, 0, 0, 0, 0, 0]
        conclusion[0] = self.syllogism_deduction_first_value_n(first_formula, second_formula)
        conclusion_1_contradiction_value = self.syllogism_deduction_first_value_a_contradiction(first_formula, second_formula)
        conclusion[1] = conclusion_1_contradiction_value
        if conclusion[0] == 'n' and conclusion[1] == 'a':
            self.syllogism_deduction_first_value_a_contradiction(first_formula, second_formula)
        conclusion[2]  = self.syllogism_deduction_second_value_n(first_formula, second_formula)
        conclusion_3_contradiction_value = self.syllogism_deduction_second_value_a_contradiction(first_formula, second_formula)
        conclusion[3] = conclusion_3_contradiction_value
        if conclusion[2] == 'n' and conclusion[3] == 'a':
            self.syllogism_deduction_second_value_a_contradiction(first_formula, second_formula)
        conclusion[4] = self.syllogism_deduction_third_value_n(first_formula, second_formula)
        conclusion_5_contradiction_value = self.syllogism_deduction_third_value_a_contradiction(first_formula, second_formula)
        conclusion[5] = conclusion_5_contradiction_value
        if conclusion[4] == 'n' and conclusion[5] == 'a':
            self.syllogism_deduction_third_value_a_contradiction(first_formula, second_formula)
        conclusion[6] = self.syllogism_deduction_fourth_value_n(first_formula, second_formula)
        conclusion_7_contradiction_value = self.syllogism_deduction_fourth_value_a_contradiction(first_formula, second_formula)
        conclusion[7] = conclusion_7_contradiction_value
        if conclusion[6] == 'n' and conclusion[7] == 'a':
            self.syllogism_deduction_fourth_value_a_contradiction(first_formula, second_formula)
        if (len(self.error_number_enlonged) != 0):
            return self.error_number_enlonged[:]
        else:
            return ([0])

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

    def syllogism_solution_enlonged(self,first_formula, second_formula):
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

    def output2_enlonged(self, my_text, my_text2):
        first_formula = my_text
        second_formula = my_text2
        solution = self.syllogism_solution_enlonged(first_formula, second_formula)
        result_contradiction_test = self.syllogism_contradiction_test_enlonged(first_formula, second_formula)
        return [solution, result_contradiction_test]

    def enlonged_fn(self, *args):

        #calculate from enlonged dyadic formulas to third enlonged dyadic formula
        enlonged_third_formula = []
        enlonged_third_formula_list = []

        count_3 = 0
        for l in range(2):
            for m in range(2):
                for n in range(2):
                    for o in range(2):
                        for p in range(2):
                            for q in range(2):
                                for r in range(2):
                                    for s in range(2):
                                        if l == 0:
                                            enlonged_third_formula.append('a')
                                        elif l == 1:
                                            enlonged_third_formula.append('n')
                                        if m == 0:
                                            enlonged_third_formula.append('a')
                                        elif m == 1:
                                            enlonged_third_formula.append('n')
                                        if n == 0:
                                            enlonged_third_formula.append('a')
                                        elif n == 1:
                                            enlonged_third_formula.append('n')
                                        if o == 0:
                                            enlonged_third_formula.append('a')
                                        elif o == 1:
                                            enlonged_third_formula.append('n')
                                        if p == 0:
                                            enlonged_third_formula.append('a')
                                        elif p == 1:
                                            enlonged_third_formula.append('n')
                                        if q == 0:
                                            enlonged_third_formula.append('a')
                                        elif q == 1:
                                            enlonged_third_formula.append('n')
                                        if r == 0:
                                            enlonged_third_formula.append('a')
                                        elif r == 1:
                                            enlonged_third_formula.append('n')
                                        if s == 0:
                                            enlonged_third_formula.append('a')
                                        elif s == 1:
                                            enlonged_third_formula.append('n')
                                        if len(enlonged_third_formula) == 8:
                                            count_3 = count_3 + 1
                                            self.first_formula_enlonged = enlonged_third_formula[0:4]
                                            self.second_formula_enlonged = enlonged_third_formula[4:8]
                                            
                                            first_formula = self.dyadic_name_fn(self.first_formula_enlonged, 2)
                                            second_formula = self.dyadic_name_fn(self.second_formula_enlonged, 1)
                                            
                                            solution_and_contradiction_test_enlonged = self.output2_enlonged(self.first_formula_enlonged, self.second_formula_enlonged)
                                            
                                            third_formula = self.dyadic_name_fn(solution_and_contradiction_test_enlonged[0], 3)
                                            
                                            enlonged_third_formula_list.append([[first_formula, second_formula, third_formula], solution_and_contradiction_test_enlonged])
                                            
                                            #print(count_3, first_formula, second_formula, third_formula, solution_and_contradiction_test_enlonged)
                                            self.error_number_enlonged.clear()
                                        enlonged_third_formula.clear()
        return (enlonged_third_formula_list)

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
        self.error_number = []
        conclusion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        conclusion[0] = self.total_formula_deduction_first_value_n(first_formula, second_formula, third_formula)
        conclusion[1] = self.total_formula_deduction_first_value_a(first_formula, second_formula, third_formula)
        if conclusion[0] == 'n' and conclusion[1] == 'a':
            self.error_number.append('1')
        conclusion[2] = self.total_formula_deduction_second_value_n(first_formula, second_formula, third_formula)
        conclusion[3] = self.total_formula_deduction_second_value_a(first_formula, second_formula, third_formula)
        if conclusion[2] == 'n' and conclusion[3] == 'a':
            self.error_number.append('2')
        conclusion[4] = self.total_formula_deduction_third_value_n(first_formula, second_formula, third_formula)
        conclusion[5] = self.total_formula_deduction_third_value_a(first_formula, second_formula, third_formula)
        if conclusion[4] == 'n' and conclusion[5] == 'a':
            self.error_number.append('3')
        conclusion[6] = self.total_formula_deduction_fourth_value_n(first_formula, second_formula, third_formula)
        conclusion[7] = self.total_formula_deduction_fourth_value_a(first_formula, second_formula, third_formula)
        if conclusion[6] == 'n' and conclusion[7] == 'a':
            self.error_number.append('4')
        conclusion[8] = self.total_formula_deduction_fifth_value_n(first_formula, second_formula, third_formula)
        conclusion[9] = self.total_formula_deduction_fifth_value_a(first_formula, second_formula, third_formula)
        if conclusion[8] == 'n' and conclusion[9] == 'a':
            self.error_number.append('5')
        conclusion[10] = self.total_formula_deduction_sixth_value_n(first_formula, second_formula, third_formula)
        conclusion[11] = self.total_formula_deduction_sixth_value_a(first_formula, second_formula, third_formula)
        if conclusion[10] == 'n' and conclusion[11] == 'a':
            self.error_number.append('6')
        conclusion[12] = self.total_formula_deduction_seventh_value_n(first_formula, second_formula, third_formula)
        conclusion[13] = self.total_formula_deduction_seventh_value_a(first_formula, second_formula, third_formula)
        if conclusion[12] == 'n' and conclusion[13] == 'a':
            self.error_number.append('7')
        conclusion[14] = self.total_formula_deduction_eighth_value_n(first_formula, second_formula, third_formula)
        conclusion[15] = self.total_formula_deduction_eighth_value_a(first_formula, second_formula, third_formula)
        if conclusion[14] == 'n' and conclusion[15] == 'a':
            self.error_number.append('8')
        if (len(self.error_number) != 0):
            return self.error_number
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
    
    def dyadic_name_fn(self, formula, number):
        if formula == ['a', 'a', 'a', 'a'] and number == 1:
            return "B#C"
        elif formula == ['a', 'a', 'a', 'n'] and number == 1:
            return "BÄC"
        elif formula == ['a', 'n', 'a', 'a'] and number == 1:
            return "BÖC"
        elif formula == ['a', 'n', 'a', 'n'] and number == 1:
            return "B&C"
        elif formula == ['a', 'a', 'n', 'a'] and number == 1:
            return "B@C"
        elif formula == ['a', 'a', 'n', 'n'] and number == 1:
            return "B%C"
        elif formula == ['a', 'n', 'n', 'a'] and number == 1:
            return "B$C"
        elif formula == ['a', 'n', 'n', 'n'] and number == 1:
            return "BÜC"
        elif formula == ['n', 'a', 'a', 'a'] and number == 1:
            return "BÜ'C"
        elif formula == ['n', 'a', 'a', 'n'] and number == 1:
            return "B$'C"
        elif formula == ['n', 'n', 'a', 'a'] and number == 1:
            return "B%'C"
        elif formula == ['n', 'n', 'a', 'n'] and number == 1:
            return "B@'C"
        elif formula == ['n', 'a', 'n', 'a'] and number == 1:
            return "B&'C"
        elif formula == ['n', 'a', 'n', 'n'] and number == 1:
            return "BÖ'C"
        elif formula == ['n', 'n', 'n', 'a'] and number == 1:
            return "BÄ'C"
        elif formula == ['n', 'n', 'n', 'n'] and number == 1:
            return "B#'C"
        elif formula == ['a', 'a', 'a', 'a'] and number == 2:
            return "C#D"
        elif formula == ['a', 'a', 'a', 'n'] and number == 2:
            return "CÄD"
        elif formula == ['a', 'n', 'a', 'a'] and number == 2:
            return "CÖD"
        elif formula == ['a', 'n', 'a', 'n'] and number == 2:
            return "C&D"
        elif formula == ['a', 'a', 'n', 'a'] and number == 2:
            return "C@D"
        elif formula == ['a', 'a', 'n', 'n'] and number == 2:
            return "C%D"
        elif formula == ['a', 'n', 'n', 'a'] and number == 2:
            return "C$D"
        elif formula == ['a', 'n', 'n', 'n'] and number == 2:
            return "CÜD"
        elif formula == ['n', 'a', 'a', 'a'] and number == 2:
            return "CÜ'D"
        elif formula == ['n', 'a', 'a', 'n'] and number == 2:
            return "C$'D"
        elif formula == ['n', 'n', 'a', 'a'] and number == 2:
            return "C%'D"
        elif formula == ['n', 'n', 'a', 'n'] and number == 2:
            return "C@'D"
        elif formula == ['n', 'a', 'n', 'a'] and number == 2:
            return "C&'D"
        elif formula == ['n', 'a', 'n', 'n'] and number == 2:
            return "CÖ'D"
        elif formula == ['n', 'n', 'n', 'a'] and number == 2:
            return "CÄ'D"
        elif formula == ['n', 'n', 'n', 'n'] and number == 2:
            return "C#'D"
        elif formula == ['a', 'a', 'a', 'a'] and number == 3:
            return "B#D"
        elif formula == ['a', 'a', 'a', 'n'] and number == 3:
            return "BÄD"
        elif formula == ['a', 'n', 'a', 'a'] and number == 3:
            return "BÖD"
        elif formula == ['a', 'n', 'a', 'n'] and number == 3:
            return "B&D"
        elif formula == ['a', 'a', 'n', 'a'] and number == 3:
            return "B@D"
        elif formula == ['a', 'a', 'n', 'n'] and number == 3:
            return "B%D"
        elif formula == ['a', 'n', 'n', 'a'] and number == 3:
            return "B$D"
        elif formula == ['a', 'n', 'n', 'n'] and number == 3:
            return "BÜD"
        elif formula == ['n', 'a', 'a', 'a'] and number == 3:
            return "BÜ'D"
        elif formula == ['n', 'a', 'a', 'n'] and number == 3:
            return "B$'D"
        elif formula == ['n', 'n', 'a', 'a'] and number == 3:
            return "B%'D"
        elif formula == ['n', 'n', 'a', 'n'] and number == 3:
            return "B@'D"
        elif formula == ['n', 'a', 'n', 'a'] and number == 3:
            return "B&'D"
        elif formula == ['n', 'a', 'n', 'n'] and number == 3:
            return "BÖ'D"
        elif formula == ['n', 'n', 'n', 'a'] and number == 3:
            return "BÄ'D"
        elif formula == ['n', 'n', 'n', 'n'] and number == 3:
            return "B#'D"
        elif formula == ['a', 'u', 'n', 'a'] and number == 3:
            return "BaD"
        elif formula == ['n', 'a', 'a', 'u'] and number == 3:
            return "BeD"
        elif formula == ['a', 'u', 'u', 'u'] and number == 3:
            return "BiD"
        elif formula == ['u', 'u', 'a', 'u'] and number == 3:
            return "BoD"
        elif formula == ['a', 'n', 'u', 'a'] and number == 3:
            return "BãD"
        elif formula == ['u', 'a', 'a', 'n'] and number == 3:
            return "BëD"
        elif formula == ['u', 'u', 'u', 'a'] and number == 3:
            return "BïD"
        elif formula == ['u', 'a', 'u', 'u'] and number == 3:
            return "BõD"
        elif formula == ['a', 'u', 'a', 'u'] and number == 3:
            return "BioD"
        elif formula == ['a', 'a', 'u', 'u'] and number == 3:
            return "BiõD"
        elif formula == ['u', 'a', 'a', 'u'] and number == 3:
            return "BoõD"
        elif formula == ['u', 'u', 'a', 'a'] and number == 3:
            return "BoïD"
        elif formula == ['u', 'a', 'u', 'a'] and number == 3:
            return "BõïD"


    def replace_total_formulas_fn(self, total_formula_old, *args):
    

        for j in range(8):
            if total_formula_old[j] == 'u':
                total_formula_old[j] = 'a'    
                total_formula_new_A = total_formula_old[:]
                total_formula_old[j] = 'n'
                total_formula_new_N = total_formula_old[:]
                
                return(total_formula_new_A, total_formula_new_N, j+1)
        
        return(0)

    def __init__(self, **kwargs):
        super(Training_calculating_quiz_Screen, self).__init__(**kwargs)
        
        self.test = self.deduction_of_triadic_total_formulas_from_dyadic_level()
        self.enlonged_list = self.enlonged_fn()
        
    def deduction_of_triadic_total_formulas_from_dyadic_level(self, *args):
        #4.096 Possibilitys from dyadic possibilitys to triadic possibilitys:
        list_third_level_input = []
        count = 0
        #count_x = 0

        list_of_total_formulas_edited = []
        for l in range(2):
            for m in range(2):
                for n in range(2):
                    for o in range(2):
                        for p in range(2):
                            for q in range(2):
                                for r in range(2):
                                    for s in range(2):
                                        for t in range(2):
                                            for u in range(2):
                                                for v in range(2):
                                                    for w in range(2):
                                                        if l == 0:
                                                            list_third_level_input.append('a')
                                                        elif l == 1:
                                                            list_third_level_input.append('n')
                                                        if m == 0:
                                                            list_third_level_input.append('a')
                                                        elif m == 1:
                                                            list_third_level_input.append('n')
                                                        if n == 0:
                                                            list_third_level_input.append('a')
                                                        elif n == 1:
                                                            list_third_level_input.append('n')
                                                        if o == 0:
                                                            list_third_level_input.append('a')
                                                        elif o == 1:
                                                            list_third_level_input.append('n')
                                                        if p == 0:
                                                            list_third_level_input.append('a')
                                                        elif p == 1:
                                                            list_third_level_input.append('n')
                                                        if q == 0:
                                                            list_third_level_input.append('a')
                                                        elif q == 1:
                                                            list_third_level_input.append('n')
                                                        if r == 0:
                                                            list_third_level_input.append('a')
                                                        elif r == 1:
                                                            list_third_level_input.append('n')
                                                        if s == 0:
                                                            list_third_level_input.append('a')
                                                        elif s == 1:
                                                            list_third_level_input.append('n')
                                                        if t == 0:
                                                            list_third_level_input.append('a')
                                                        elif t == 1:
                                                            list_third_level_input.append('n')
                                                        if u == 0:
                                                            list_third_level_input.append('a')
                                                        elif u == 1:
                                                            list_third_level_input.append('n')
                                                        if v == 0:
                                                            list_third_level_input.append('a')
                                                        elif v == 1:
                                                            list_third_level_input.append('n')
                                                        if w == 0:
                                                            list_third_level_input.append('a')
                                                        elif w == 1:
                                                            list_third_level_input.append('n')
                                                        if len(list_third_level_input) == 12:
                                                            self.first_formula = list_third_level_input[0:4]
                                                            self.second_formula = list_third_level_input[4:8]
                                                            self.third_formula = list_third_level_input[8:12]

                                                            solution_and_contradiction_test = self.output2(self.first_formula, self.second_formula, self.third_formula)
                                                            #solution_and_contradiction_test[0].count('u') == 1 --> one 'u' in total-formula
                                                            #len(self.error_number) == 0 --> no contradiction
                                                            
                                                            #if len(self.error_number) != 0:
                                                            #    count_x = count_x + 1
                                                            #    print(self.error_number)                          
                                                            
                                                            if (solution_and_contradiction_test[0].count('u') == 0 or solution_and_contradiction_test[0].count('u') == 1 or solution_and_contradiction_test[0].count('u') == 2) and (len(self.error_number) == 0):
                                                                
                                                                first_formula = self.dyadic_name_fn(self.first_formula, 1)
                                                                second_formula = self.dyadic_name_fn(self.second_formula, 2)
                                                                third_formula = self.dyadic_name_fn(self.third_formula, 3)
                                                                count = count + 1
                                                                
                                                                new_total_formulas_A_and_N = self.replace_total_formulas_fn(solution_and_contradiction_test[0][:])
                                                                

                                                                
                                                                #if = append to list_of_total_formulas_edited
                                                                if solution_and_contradiction_test[0].count('u') == 0:

                                                                    
                                                                    list_of_total_formulas_edited.append([solution_and_contradiction_test[0], [first_formula, second_formula, third_formula], [[], []]])
                                                                    #count_x = count_x + 1
                                                                    #print('1')
                                                                    
                                                                    
                                                                elif solution_and_contradiction_test[0].count('u') == 1:
                                                                    
                                                                    list_of_total_formulas_edited.append([new_total_formulas_A_and_N[0], [first_formula, second_formula, third_formula], [[str(new_total_formulas_A_and_N[2])+'A'], []]])
                                                                    list_of_total_formulas_edited.append([new_total_formulas_A_and_N[1], [first_formula, second_formula, third_formula], [[str(new_total_formulas_A_and_N[2])+'N'], []]])
                                                                    #count_x = count_x + 1
                                                                    #print('0,5')
                                                                    
                                                                elif solution_and_contradiction_test[0].count('u') == 2:
                                                                    new_total_formulas_A_and_N_second = self.replace_total_formulas_fn(new_total_formulas_A_and_N[0][:])
                                                                    new_total_formulas_A_and_N_second_2 = self.replace_total_formulas_fn(new_total_formulas_A_and_N[1][:])

                                                                    list_of_total_formulas_edited.append([new_total_formulas_A_and_N_second[0], [first_formula, second_formula, third_formula], [[str(new_total_formulas_A_and_N[2])+'A'], [str(new_total_formulas_A_and_N_second[2])+'A']]])
                                                                    list_of_total_formulas_edited.append([new_total_formulas_A_and_N_second[1], [first_formula, second_formula, third_formula], [[str(new_total_formulas_A_and_N[2])+'A'], [str(new_total_formulas_A_and_N_second[2])+'N']]])
                                                                    list_of_total_formulas_edited.append([new_total_formulas_A_and_N_second_2[0], [first_formula, second_formula, third_formula], [[str(new_total_formulas_A_and_N[2])+'N'], [str(new_total_formulas_A_and_N_second_2[2])+'A']]])
                                                                    list_of_total_formulas_edited.append([new_total_formulas_A_and_N_second_2[1], [first_formula, second_formula, third_formula], [[str(new_total_formulas_A_and_N[2])+'N'], [str(new_total_formulas_A_and_N_second_2[2])+'N']]])
                                                                    
                                                                    #count_x = count_x + 1
                                                                    #print('0,25')
                                                                self.error_number.clear()
        
                                                        list_third_level_input.clear()
        
        #sort unnessacary here
        list_of_total_formulas_edited_sorted = list_of_total_formulas_edited[:]
        list_of_total_formulas_edited_sorted = sorted(list_of_total_formulas_edited_sorted, key=lambda x: (x!=('a'), (x[0][0], x[0][4], x[0][2], x[0][6], x[0][1], x[0][5], x[0][3], x[0][7])))
        
        only_formulas_total_formulas_from_dyadic_level_list = []
        
        #make list of formulas only to remove duplicates later in list_of_total_formulas_edited_sorted
        for r in range(len(list_of_total_formulas_edited_sorted)):
            only_formulas_total_formulas_from_dyadic_level_list.append(list_of_total_formulas_edited_sorted[r][0])
        
        list_removed_double_formulas_list = list_of_total_formulas_edited_sorted[:]
        
        #remove duplicates
        for r in range(len(list_of_total_formulas_edited_sorted)):
            if (only_formulas_total_formulas_from_dyadic_level_list.count(list_of_total_formulas_edited_sorted[r][0]) != 1) and (list_of_total_formulas_edited_sorted[r][2][0] != []):
                list_removed_double_formulas_list.remove(list_of_total_formulas_edited_sorted[r])

        #generate 256 possibilitys of triadic total-formulas and replace those possibilities which are deducable on dyadic level
        list_third_level = []
        list_third_level_list = []

        count_2 = 0
        for l in range(2):
            for m in range(2):
                for n in range(2):
                    for o in range(2):
                        for p in range(2):
                            for q in range(2):
                                for r in range(2):
                                    for s in range(2):
                                        if l == 0:
                                            list_third_level.append('a')
                                        elif l == 1:
                                            list_third_level.append('n')
                                        if m == 0:
                                            list_third_level.append('a')
                                        elif m == 1:
                                            list_third_level.append('n')
                                        if n == 0:
                                            list_third_level.append('a')
                                        elif n == 1:
                                            list_third_level.append('n')
                                        if o == 0:
                                            list_third_level.append('a')
                                        elif o == 1:
                                            list_third_level.append('n')
                                        if p == 0:
                                            list_third_level.append('a')
                                        elif p == 1:
                                            list_third_level.append('n')
                                        if q == 0:
                                            list_third_level.append('a')
                                        elif q == 1:
                                            list_third_level.append('n')
                                        if r == 0:
                                            list_third_level.append('a')
                                        elif r == 1:
                                            list_third_level.append('n')
                                        if s == 0:
                                            list_third_level.append('a')
                                        elif s == 1:
                                            list_third_level.append('n')
                                        if len(list_third_level) == 8:
                                            count_2 = count_2 + 1
                                            list_third_level_list.append([list_third_level[:], 0])
                                            for t in range(len(list_removed_double_formulas_list)):
                                                if list_third_level == list_removed_double_formulas_list[t][0]:
                                                    list_third_level_list.remove([list_third_level, 0])
                                                    list_third_level_list.append([list_removed_double_formulas_list[t][0], list_removed_double_formulas_list[t][1], list_removed_double_formulas_list[t][2]])
                                        list_third_level.clear()

        #sort list_third_level_list_sorted
        list_third_level_list_sorted = list_third_level_list[:]
        list_third_level_list_sorted = sorted(list_third_level_list_sorted, key=lambda x: (x!=('a'), (x[0][0], x[0][4], x[0][2], x[0][6], x[0][1], x[0][5], x[0][3], x[0][7])))

        #make labels
        """for i in range(len(list_third_level_list_sorted)):
            if list_third_level_list_sorted[i][1] == 0:
                self.formulas_label = Label(text=str(i+1)+': '+str(list_third_level_list_sorted[i][0]), font_name= 'my_custom_font', size_hint_y=None, height=40)
                self.layout.add_widget(self.formulas_label)
            else:
                self.formulas_label = Label(text=str(i+1)+': '+str(list_third_level_list_sorted[i][1][0])+', '+str(list_third_level_list_sorted[i][1][1])+', '+str(list_third_level_list_sorted[i][1][2])+' '+str(list_third_level_list_sorted[i][2])+':', font_name= 'my_custom_font', size_hint_y=None, height=40)
                self.layout.add_widget(self.formulas_label)
                self.solution_label = Label(text=str(list_third_level_list_sorted[i][0]), font_name= 'my_custom_font', size_hint_y=None, height=40)
                self.layout.add_widget(self.solution_label)"""
        

        #self.add_widget(self.root)
        
        return list_third_level_list_sorted

class Total_formulas_Playground_left_Screen(Screen):
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
                self.btn_1_p1.background_color=(1, 0, 0, 1)
                self.btn_2_p1.text ='n'
                self.btn_2_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_1_p1.text ='a'
                self.btn_1_p1.background_color=(0, 1, 0, 1)
                self.btn_2_p1.text ='a'
                self.btn_2_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_1_p1.text ='u'
                self.btn_1_p1.background_color=(1, 1, 1, 1)
                self.btn_2_p1.text ='u'
                self.btn_2_p1.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 1:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_3_p1.text ='n'
                self.btn_3_p1.background_color=(1, 0, 0, 1)
                self.btn_4_p1.text ='n'
                self.btn_4_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_3_p1.text ='a'
                self.btn_3_p1.background_color=(0, 1, 0, 1)
                self.btn_4_p1.text ='a'
                self.btn_4_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_3_p1.text ='u'
                self.btn_3_p1.background_color=(1, 1, 1, 1)
                self.btn_4_p1.text ='u'
                self.btn_4_p1.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 2:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_5_p1.text ='n'
                self.btn_5_p1.background_color=(1, 0, 0, 1)
                self.btn_6_p1.text ='n'
                self.btn_6_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_5_p1.text ='a'
                self.btn_5_p1.background_color=(0, 1, 0, 1)
                self.btn_6_p1.text ='a'
                self.btn_6_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_5_p1.text ='u'
                self.btn_5_p1.background_color=(1, 1, 1, 1)
                self.btn_6_p1.text ='u'
                self.btn_6_p1.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 3:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_7_p1.text ='n'
                self.btn_7_p1.background_color=(1, 0, 0, 1)
                self.btn_8_p1.text ='n'
                self.btn_8_p1.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_7_p1.text ='a'
                self.btn_7_p1.background_color=(0, 1, 0, 1)
                self.btn_8_p1.text ='a'
                self.btn_8_p1.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_7_p1.text ='u'
                self.btn_7_p1.background_color=(1, 1, 1, 1)
                self.btn_8_p1.text ='u'
                self.btn_8_p1.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 4:
            print('test')
            self.first_formula = foo_3
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_1_p2.text ='n'
                self.btn_1_p2.background_color=(1, 0, 0, 1)
                self.btn_5_p2.text ='n'
                self.btn_5_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_1_p2.text ='a'
                self.btn_1_p2.background_color=(0, 1, 0, 1)
                self.btn_5_p2.text ='a'
                self.btn_5_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_1_p2.text ='u'
                self.btn_1_p2.background_color=(1, 1, 1, 1)
                self.btn_5_p2.text ='u'
                self.btn_5_p2.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 5:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_2_p2.text ='n'
                self.btn_2_p2.background_color=(1, 0, 0, 1)
                self.btn_6_p2.text ='n'
                self.btn_6_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_2_p2.text ='a'
                self.btn_2_p2.background_color=(0, 1, 0, 1)
                self.btn_6_p2.text ='a'
                self.btn_6_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_2_p2.text ='u'
                self.btn_2_p2.background_color=(1, 1, 1, 1)
                self.btn_6_p2.text ='u'
                self.btn_6_p2.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 6:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_3_p2.text ='n'
                self.btn_3_p2.background_color=(1, 0, 0, 1)
                self.btn_7_p2.text ='n'
                self.btn_7_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_3_p2.text ='a'
                self.btn_3_p2.background_color=(0, 1, 0, 1)
                self.btn_7_p2.text ='a'
                self.btn_7_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_3_p2.text ='u'
                self.btn_3_p2.background_color=(1, 1, 1, 1)
                self.btn_7_p2.text ='u'
                self.btn_7_p2.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 7:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_4_p2.text ='n'
                self.btn_4_p2.background_color=(1, 0, 0, 1)
                self.btn_8_p2.text ='n'
                self.btn_8_p2.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_4_p2.text ='a'
                self.btn_4_p2.background_color=(0, 1, 0, 1)
                self.btn_8_p2.text ='a'
                self.btn_8_p2.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_4_p2.text ='u'
                self.btn_4_p2.background_color=(1, 1, 1, 1)
                self.btn_8_p2.text ='u'
                self.btn_8_p2.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 8:
            print('test')
            self.second_formula = foo_3[4:8]
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_1_p3.text ='n'
                self.btn_1_p3.background_color=(1, 0, 0, 1)
                self.btn_3_p3.text ='n'
                self.btn_3_p3.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_1_p3.text ='a'
                self.btn_1_p3.background_color=(0, 1, 0, 1)
                self.btn_3_p3.text ='a'
                self.btn_3_p3.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_1_p3.text ='u'
                self.btn_1_p3.background_color=(1, 1, 1, 1)
                self.btn_3_p3.text ='u'
                self.btn_3_p3.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 9:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_2_p3.text ='n'
                self.btn_2_p3.background_color=(1, 0, 0, 1)
                self.btn_4_p3.text ='n'
                self.btn_4_p3.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_2_p3.text ='a'
                self.btn_2_p3.background_color=(0, 1, 0, 1)
                self.btn_4_p3.text ='a'
                self.btn_4_p3.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_2_p3.text ='u'
                self.btn_2_p3.background_color=(1, 1, 1, 1)
                self.btn_4_p3.text ='u'
                self.btn_4_p3.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 10:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_5_p3.text ='n'
                self.btn_5_p3.background_color=(1, 0, 0, 1)
                self.btn_7_p3.text ='n'
                self.btn_7_p3.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_5_p3.text ='a'
                self.btn_5_p3.background_color=(0, 1, 0, 1)
                self.btn_7_p3.text ='a'
                self.btn_7_p3.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_5_p3.text ='u'
                self.btn_5_p3.background_color=(1, 1, 1, 1)
                self.btn_7_p3.text ='u'
                self.btn_7_p3.background_color=(1, 1, 1, 1)
        elif len(foo_3) == 11:
            if button == self.btn_n:
                z = foo_3.append('n')
                self.btn_6_p3.text ='n'
                self.btn_6_p3.background_color=(1, 0, 0, 1)
                self.btn_8_p3.text ='n'
                self.btn_8_p3.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_3.append('a')
                self.btn_6_p3.text ='a'
                self.btn_6_p3.background_color=(0, 1, 0, 1)
                self.btn_8_p3.text ='a'
                self.btn_8_p3.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_3.append('u')
                self.btn_6_p3.text ='u'
                self.btn_6_p3.background_color=(1, 1, 1, 1)
                self.btn_8_p3.text ='u'
                self.btn_8_p3.background_color=(1, 1, 1, 1)
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
        
        self.refresh2_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
        self.add_widget(self.refresh2_button)
        
        self.menu_button = Button(text='Menü', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .9})
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
                self.btn_1_c.background_color=(1, 0, 0, 1)
                self.btn_1_c.background_color=(1, 0, 0, 1)
            elif function_output_list[0][0] == 'a':
                self.btn_1_c.background_color=(0, 1, 0, 1)
                self.btn_1_c.background_color=(0, 1, 0, 1)
            elif function_output_list[0][0] == 'u':
                self.btn_1_c.background_color=(1, 1, 1, 1)
                self.btn_1_c.background_color=(1, 1, 1, 1)
            if function_output_list[0][1] == 'n':
                self.btn_2_c.background_color=(1, 0, 0, 1)
                self.btn_2_c.background_color=(1, 0, 0, 1)
            elif function_output_list[0][1] == 'a':
                self.btn_2_c.background_color=(0, 1, 0, 1)
                self.btn_2_c.background_color=(0, 1, 0, 1)
            elif function_output_list[0][1] == 'u':
                self.btn_2_c.background_color=(1, 1, 1, 1)
                self.btn_2_c.background_color=(1, 1, 1, 1)
            if function_output_list[0][2] == 'n':
                self.btn_3_c.background_color=(1, 0, 0, 1)
                self.btn_3_c.background_color=(1, 0, 0, 1)
            elif function_output_list[0][2] == 'a':
                self.btn_3_c.background_color=(0, 1, 0, 1)
                self.btn_3_c.background_color=(0, 1, 0, 1)
            elif function_output_list[0][2] == 'u':
                self.btn_3_c.background_color=(1, 1, 1, 1)
                self.btn_3_c.background_color=(1, 1, 1, 1)
            if function_output_list[0][3] == 'n':
                self.btn_4_c.background_color=(1, 0, 0, 1)
                self.btn_4_c.background_color=(1, 0, 0, 1)
            elif function_output_list[0][3] == 'a':
                self.btn_4_c.background_color=(0, 1, 0, 1)
                self.btn_4_c.background_color=(0, 1, 0, 1)
            elif function_output_list[0][3] == 'u':
                self.btn_4_c.background_color=(1, 1, 1, 1)
                self.btn_4_c.background_color=(1, 1, 1, 1)
            if function_output_list[0][4] == 'n':
                self.btn_5_c.background_color=(1, 0, 0, 1)
                self.btn_5_c.background_color=(1, 0, 0, 1)
            elif function_output_list[0][4] == 'a':
                self.btn_5_c.background_color=(0, 1, 0, 1)
                self.btn_5_c.background_color=(0, 1, 0, 1)
            elif function_output_list[0][4] == 'u':
                self.btn_5_c.background_color=(1, 1, 1, 1)
                self.btn_5_c.background_color=(1, 1, 1, 1)
            if function_output_list[0][5] == 'n':
                self.btn_6_c.background_color=(1, 0, 0, 1)
                self.btn_6_c.background_color=(1, 0, 0, 1)
            elif function_output_list[0][5] == 'a':
                self.btn_6_c.background_color=(0, 1, 0, 1)
                self.btn_6_c.background_color=(0, 1, 0, 1)
            elif function_output_list[0][5] == 'u':
                self.btn_6_c.background_color=(1, 1, 1, 1)
                self.btn_6_c.background_color=(1, 1, 1, 1)
            if function_output_list[0][6] == 'n':
                self.btn_7_c.background_color=(1, 0, 0, 1)
                self.btn_7_c.background_color=(1, 0, 0, 1)
            elif function_output_list[0][6] == 'a':
                self.btn_7_c.background_color=(0, 1, 0, 1)
                self.btn_7_c.background_color=(0, 1, 0, 1)
            elif function_output_list[0][6] == 'u':
                self.btn_7_c.background_color=(1, 1, 1, 1)
                self.btn_7_c.background_color=(1, 1, 1, 1)
            if function_output_list[0][7] == 'n':
                self.btn_8_c.background_color=(1, 0, 0, 1)
                self.btn_8_c.background_color=(1, 0, 0, 1)
            elif function_output_list[0][7] == 'a':
                self.btn_8_c.background_color=(0, 1, 0, 1)
                self.btn_8_c.background_color=(0, 1, 0, 1)
            elif function_output_list[0][7] == 'u':
                self.btn_8_c.background_color=(1, 1, 1, 1)
                self.btn_8_c.background_color=(1, 1, 1, 1)
                
    def refresh_function(self, button):
        
        horizontal = BoxLayout(orientation='horizontal')
        self.add_widget(horizontal)
        
        self.label_1 = Label(size_hint_x = .2)
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
        
        self.premis_one_label = Label(text='1. Formel', size_hint_x = 2.5)
        self.syllogism_box_row_4.add_widget(self.premis_one_label)

        self.btn_1_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_1_p1)
        self.btn_2_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_2_p1)
        self.btn_3_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_3_p1)
        self.btn_4_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_4_p1)
        self.btn_5_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_5_p1)
        self.btn_6_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_6_p1)
        self.btn_7_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_7_p1)
        self.btn_8_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_8_p1)

        self.syllogism_box_row_5 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_5)
        
        self.premis_two_label = Label(text='2. Formel', size_hint_x = 2.5)
        self.syllogism_box_row_5.add_widget(self.premis_two_label)

        self.btn_1_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_1_p2)
        self.btn_2_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_2_p2)
        self.btn_3_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_3_p2)
        self.btn_4_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_4_p2)
        self.btn_5_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_5_p2)
        self.btn_6_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_6_p2)
        self.btn_7_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_7_p2)
        self.btn_8_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_8_p2)

        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.premis_three_label = Label(text='3. Formel', size_hint_x = 2.5)
        self.syllogism_box_row_6.add_widget(self.premis_three_label)

        self.btn_1_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_p3)
        self.btn_2_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_p3)
        self.btn_3_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_p3)
        self.btn_4_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_p3)
        self.btn_5_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_p3)
        self.btn_6_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_p3)
        self.btn_7_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_p3)
        self.btn_8_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_p3)

        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.conclusion_label = Label(text='Ganzformel', size_hint_x = 2.5)
        self.syllogism_box_row_6.add_widget(self.conclusion_label)

        self.btn_1_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_c)
        self.btn_2_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_c)
        self.btn_3_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_c)
        self.btn_4_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_c)
        self.btn_5_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_c)
        self.btn_6_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_c)
        self.btn_7_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_c)
        self.btn_8_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_c)

        self.syllogism_box_col_2 = BoxLayout(orientation='vertical')
        vertical.add_widget(self.syllogism_box_col_2)

        self.label_5 = Label()
        vertical.add_widget(self.label_5)

        self.box_horizontal_buttons_down = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.box_horizontal_buttons_down)

        self.btn_n = Button(text='n', color= (0, 0, 0, 1), background_normal='', background_color=(1, 0, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_n)
        variable_btn_n ='n'
        self.btn_n.bind(on_press=self.append_function)

        self.btn_a = Button(text='a', color= (0, 0, 0, 1), background_normal='', background_color=(0, 1, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_a)
        variable_btn_a ='a'
        self.btn_a.bind(on_press=self.append_function)

        self.btn_u = Button(text='u', color= (0, 0, 0, 1), background_normal='', background_color=(1, 1, 1, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_u)
        variable_btn_u ='u'
        self.btn_u.bind(on_press=self.append_function)

        self.label_3 = Label(size_hint_x = .2)
        horizontal.add_widget(self.label_3)
        


        self.refresh_button.bind(on_press=self.clear_widgets_function)

    def __init__(self, **kwargs):
        super(Total_formulas_Playground_left_Screen, self).__init__(**kwargs)
        
        self.refresh_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
        self.add_widget(self.refresh_button)
        self.refresh_button.bind(on_press=self.refresh_function)

class Total_formulas_Playground_right_Screen(Screen):
    global foo_4
    foo_4 = []
    
    def first_formula_deduction_first_value(self, total_formula):
        if total_formula[0] == "n" and total_formula[4] == "n":
            return("n")
        else:
            return("a")
        
    def first_formula_deduction_second_value(self, total_formula):
        if total_formula[1] == "n" and total_formula[5] == "n":
            return("n")
        else:
            return("a")
        
    def first_formula_deduction_third_value(self, total_formula):
        if total_formula[2] == "n" and total_formula[6] == "n":
            return("n")
        else:
            return("a")
        
    def first_formula_deduction_fourth_value(self, total_formula):
        if total_formula[3] == "n" and total_formula[7] == "n":
            return("n")
        else:
            return("a")

    def second_formula_deduction_first_value(self, total_formula):
        if total_formula[0] == "n" and total_formula[1] == "n":
            return("n")
        else:
            return("a")

    def second_formula_deduction_second_value(self, total_formula):
        if total_formula[2] == "n" and total_formula[3] == "n":
            return("n")
        else:
            return("a")
        
    def second_formula_deduction_third_value(self, total_formula):
        if total_formula[4] == "n" and total_formula[5] == "n":
            return("n")
        else:
            return("a")
        
    def second_formula_deduction_fourth_value(self, total_formula):
        if total_formula[6] == "n" and total_formula[7] == "n":
            return("n")
        else:
            return("a")
        
    def third_formula_deduction_first_value(self, total_formula):
        if total_formula[0] == "n" and total_formula[2] == "n":
            return("n")
        else:
            return("a")
        
    def third_formula_deduction_second_value(self, total_formula):
        if total_formula[1] == "n" and total_formula[3] == "n":
            return("n")
        else:
            return("a")
        
    def third_formula_deduction_third_value(self, total_formula):
        if total_formula[4] == "n" and total_formula[6] == "n":
            return("n")
        else:
            return("a")
        
    def third_formula_deduction_fourth_value(self, total_formula):
        if total_formula[5] == "n" and total_formula[7] == "n":
            return("n")
        else:
            return("a")
    
    def analyize_solution(self, total_formula):
        first_formula = [0, 0, 0, 0]
        second_formula = [0, 0, 0, 0]
        third_formula = [0, 0, 0, 0]
        
        first_formula[0] = self.first_formula_deduction_first_value(total_formula)
        first_formula[1] = self.first_formula_deduction_second_value(total_formula)
        first_formula[2] = self.first_formula_deduction_third_value(total_formula)
        first_formula[3] = self.first_formula_deduction_fourth_value(total_formula)
        
        second_formula[0] = self.second_formula_deduction_first_value(total_formula)
        second_formula[1] = self.second_formula_deduction_second_value(total_formula)
        second_formula[2] = self.second_formula_deduction_third_value(total_formula)
        second_formula[3] = self.second_formula_deduction_fourth_value(total_formula)
        
        third_formula[0] = self.third_formula_deduction_first_value(total_formula)
        third_formula[1] = self.third_formula_deduction_second_value(total_formula)
        third_formula[2] = self.third_formula_deduction_third_value(total_formula)
        third_formula[3] = self.third_formula_deduction_fourth_value(total_formula)
        
        return([first_formula, second_formula, third_formula])

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def append_function(self, button):
        print(button)
        if foo_4 == []:
            if button == self.btn_n:
                z = foo_4.append('n')
                self.btn_1_c.text ='N'
                self.btn_1_c.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_4.append('a')
                self.btn_1_c.text ='A'
                self.btn_1_c.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_4.append('u')
                self.btn_1_c.text ='u'
                self.btn_1_c.background_color=(1, 1, 1, 1)
        elif len(foo_4) == 1:
            if button == self.btn_n:
                z = foo_4.append('n')
                self.btn_2_c.text ='N'
                self.btn_2_c.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_4.append('a')
                self.btn_2_c.text ='A'
                self.btn_2_c.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_4.append('u')
                self.btn_2_c.text ='u'
                self.btn_2_c.background_color=(1, 1, 1, 1)
        elif len(foo_4) == 2:
            if button == self.btn_n:
                z = foo_4.append('n')
                self.btn_3_c.text ='N'
                self.btn_3_c.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_4.append('a')
                self.btn_3_c.text ='A'
                self.btn_3_c.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_4.append('u')
                self.btn_3_c.text ='u'
                self.btn_3_c.background_color=(1, 1, 1, 1)
        elif len(foo_4) == 3:
            if button == self.btn_n:
                z = foo_4.append('n')
                self.btn_4_c.text ='N'
                self.btn_4_c.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_4.append('a')
                self.btn_4_c.text ='A'
                self.btn_4_c.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_4.append('u')
                self.btn_4_c.text ='u'
                self.btn_4_c.background_color=(1, 1, 1, 1)
        elif len(foo_4) == 4:
            if button == self.btn_n:
                z = foo_4.append('n')
                self.btn_5_c.text ='N'
                self.btn_5_c.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_4.append('a')
                self.btn_5_c.text ='A'
                self.btn_5_c.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_4.append('u')
                self.btn_5_c.text ='u'
                self.btn_5_c.background_color=(1, 1, 1, 1)
        elif len(foo_4) == 5:
            if button == self.btn_n:
                z = foo_4.append('n')
                self.btn_6_c.text ='N'
                self.btn_6_c.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_4.append('a')
                self.btn_6_c.text ='A'
                self.btn_6_c.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_4.append('u')
                self.btn_6_c.text ='u'
                self.btn_6_c.background_color=(1, 1, 1, 1)
        elif len(foo_4) == 6:
            if button == self.btn_n:
                z = foo_4.append('n')
                self.btn_7_c.text ='N'
                self.btn_7_c.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_4.append('a')
                self.btn_7_c.text ='A'
                self.btn_7_c.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_4.append('u')
                self.btn_7_c.text ='u'
                self.btn_7_c.background_color=(1, 1, 1, 1)
        elif len(foo_4) == 7:
            if button == self.btn_n:
                z = foo_4.append('n')
                self.btn_8_c.text ='N'
                self.btn_8_c.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_4.append('a')
                self.btn_8_c.text ='A'
                self.btn_8_c.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_4.append('u')
                self.btn_8_c.text ='u'
                self.btn_8_c.background_color=(1, 1, 1, 1)
            self.total_formula = foo_4[0:8]
            self.btn_n.disabled = True
            self.btn_a.disabled = True
            self.btn_u.disabled = True
            self.click(button)
            foo_4.clear()

    def clear_widgets_function(self, *args):
        self.clear_widgets()
        foo_4.clear()
        
        self.refresh2_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
        self.add_widget(self.refresh2_button)
        
        self.menu_button = Button(text='Menü', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .9})
        self.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.refresh2_button.bind(on_press=self.refresh_function)
        
        self.refresh2_button.bind(on_press=self.clear_widgets_function)

    def click(self,my_button2):
        print(self.total_formula)
        print(self.total_formula)
        my_text = self.total_formula

        function_output_list = self.analyize_solution(my_text)
        print(function_output_list)

        self.btn_1_p1.text = function_output_list[0][0]
        self.btn_2_p1.text = function_output_list[0][0]
        self.btn_3_p1.text = function_output_list[0][1]
        self.btn_4_p1.text = function_output_list[0][1]
        self.btn_5_p1.text = function_output_list[0][2]
        self.btn_6_p1.text = function_output_list[0][2]
        self.btn_7_p1.text = function_output_list[0][3]
        self.btn_8_p1.text = function_output_list[0][3]

        self.btn_1_p2.text = function_output_list[1][0]
        self.btn_2_p2.text = function_output_list[1][1]
        self.btn_3_p2.text = function_output_list[1][2]
        self.btn_4_p2.text = function_output_list[1][3]
        self.btn_5_p2.text = function_output_list[1][0]
        self.btn_6_p2.text = function_output_list[1][1]
        self.btn_7_p2.text = function_output_list[1][2]
        self.btn_8_p2.text = function_output_list[1][3]
        
        self.btn_1_p3.text = function_output_list[2][0]
        self.btn_2_p3.text = function_output_list[2][1]
        self.btn_3_p3.text = function_output_list[2][0]
        self.btn_4_p3.text = function_output_list[2][1]
        self.btn_5_p3.text = function_output_list[2][2]
        self.btn_6_p3.text = function_output_list[2][3]
        self.btn_7_p3.text = function_output_list[2][2]
        self.btn_8_p3.text = function_output_list[2][3]

        if function_output_list[0][0] == 'n':
            self.btn_1_p1.background_color=(1, 0, 0, 1)
            self.btn_1_p1.background_color=(1, 0, 0, 1)
            self.btn_2_p1.background_color=(1, 0, 0, 1)
            self.btn_2_p1.background_color=(1, 0, 0, 1)
        elif function_output_list[0][0] == 'a':
            self.btn_1_p1.background_color=(0, 1, 0, 1)
            self.btn_1_p1.background_color=(0, 1, 0, 1)
            self.btn_2_p1.background_color=(0, 1, 0, 1)
            self.btn_2_p1.background_color=(0, 1, 0, 1)
        if function_output_list[0][1] == 'n':
            self.btn_3_p1.background_color=(1, 0, 0, 1)
            self.btn_3_p1.background_color=(1, 0, 0, 1)
            self.btn_4_p1.background_color=(1, 0, 0, 1)
            self.btn_4_p1.background_color=(1, 0, 0, 1)
        elif function_output_list[0][1] == 'a':
            self.btn_3_p1.background_color=(0, 1, 0, 1)
            self.btn_3_p1.background_color=(0, 1, 0, 1)
            self.btn_4_p1.background_color=(0, 1, 0, 1)
            self.btn_4_p1.background_color=(0, 1, 0, 1)
        if function_output_list[0][2] == 'n':
            self.btn_5_p1.background_color=(1, 0, 0, 1)
            self.btn_5_p1.background_color=(1, 0, 0, 1)
            self.btn_6_p1.background_color=(1, 0, 0, 1)
            self.btn_6_p1.background_color=(1, 0, 0, 1)
        elif function_output_list[0][2] == 'a':
            self.btn_5_p1.background_color=(0, 1, 0, 1)
            self.btn_5_p1.background_color=(0, 1, 0, 1)
            self.btn_6_p1.background_color=(0, 1, 0, 1)
            self.btn_6_p1.background_color=(0, 1, 0, 1)
        if function_output_list[0][3] == 'n':
            self.btn_7_p1.background_color=(1, 0, 0, 1)
            self.btn_7_p1.background_color=(1, 0, 0, 1)
            self.btn_8_p1.background_color=(1, 0, 0, 1)
            self.btn_8_p1.background_color=(1, 0, 0, 1)
        elif function_output_list[0][3] == 'a':
            self.btn_7_p1.background_color=(0, 1, 0, 1)
            self.btn_7_p1.background_color=(0, 1, 0, 1)
            self.btn_8_p1.background_color=(0, 1, 0, 1)
            self.btn_8_p1.background_color=(0, 1, 0, 1)

        if function_output_list[1][0] == 'n':
            self.btn_1_p2.background_color=(1, 0, 0, 1)
            self.btn_1_p2.background_color=(1, 0, 0, 1)
            self.btn_5_p2.background_color=(1, 0, 0, 1)
            self.btn_5_p2.background_color=(1, 0, 0, 1)
        elif function_output_list[1][0] == 'a':
            self.btn_1_p2.background_color=(0, 1, 0, 1)
            self.btn_1_p2.background_color=(0, 1, 0, 1)
            self.btn_5_p2.background_color=(0, 1, 0, 1)
            self.btn_5_p2.background_color=(0, 1, 0, 1)
        if function_output_list[1][1] == 'n':
            self.btn_2_p2.background_color=(1, 0, 0, 1)
            self.btn_2_p2.background_color=(1, 0, 0, 1)
            self.btn_6_p2.background_color=(1, 0, 0, 1)
            self.btn_6_p2.background_color=(1, 0, 0, 1)
        elif function_output_list[1][1] == 'a':
            self.btn_2_p2.background_color=(0, 1, 0, 1)
            self.btn_2_p2.background_color=(0, 1, 0, 1)
            self.btn_6_p2.background_color=(0, 1, 0, 1)
            self.btn_6_p2.background_color=(0, 1, 0, 1)
        if function_output_list[1][2] == 'n':
            self.btn_3_p2.background_color=(1, 0, 0, 1)
            self.btn_3_p2.background_color=(1, 0, 0, 1)
            self.btn_7_p2.background_color=(1, 0, 0, 1)
            self.btn_7_p2.background_color=(1, 0, 0, 1)
        elif function_output_list[1][2] == 'a':
            self.btn_3_p2.background_color=(0, 1, 0, 1)
            self.btn_3_p2.background_color=(0, 1, 0, 1)
            self.btn_7_p2.background_color=(0, 1, 0, 1)
            self.btn_7_p2.background_color=(0, 1, 0, 1)
        if function_output_list[1][3] == 'n':
            self.btn_4_p2.background_color=(1, 0, 0, 1)
            self.btn_4_p2.background_color=(1, 0, 0, 1)
            self.btn_8_p2.background_color=(1, 0, 0, 1)
            self.btn_8_p2.background_color=(1, 0, 0, 1)
        elif function_output_list[1][3] == 'a':
            self.btn_4_p2.background_color=(0, 1, 0, 1)
            self.btn_4_p2.background_color=(0, 1, 0, 1)
            self.btn_8_p2.background_color=(0, 1, 0, 1)
            self.btn_8_p2.background_color=(0, 1, 0, 1)

        if function_output_list[2][0] == 'n':
            self.btn_1_p3.background_color=(1, 0, 0, 1)
            self.btn_1_p3.background_color=(1, 0, 0, 1)
            self.btn_3_p3.background_color=(1, 0, 0, 1)
            self.btn_3_p3.background_color=(1, 0, 0, 1)
        elif function_output_list[2][0] == 'a':
            self.btn_1_p3.background_color=(0, 1, 0, 1)
            self.btn_1_p3.background_color=(0, 1, 0, 1)
            self.btn_3_p3.background_color=(0, 1, 0, 1)
            self.btn_3_p3.background_color=(0, 1, 0, 1)
        if function_output_list[2][1] == 'n':
            self.btn_2_p3.background_color=(1, 0, 0, 1)
            self.btn_2_p3.background_color=(1, 0, 0, 1)
            self.btn_4_p3.background_color=(1, 0, 0, 1)
            self.btn_4_p3.background_color=(1, 0, 0, 1)
        elif function_output_list[2][1] == 'a':
            self.btn_2_p3.background_color=(0, 1, 0, 1)
            self.btn_2_p3.background_color=(0, 1, 0, 1)
            self.btn_4_p3.background_color=(0, 1, 0, 1)
            self.btn_4_p3.background_color=(0, 1, 0, 1)
        if function_output_list[2][2] == 'n':
            self.btn_5_p3.background_color=(1, 0, 0, 1)
            self.btn_5_p3.background_color=(1, 0, 0, 1)
            self.btn_7_p3.background_color=(1, 0, 0, 1)
            self.btn_7_p3.background_color=(1, 0, 0, 1)
        elif function_output_list[2][2] == 'a':
            self.btn_5_p3.background_color=(0, 1, 0, 1)
            self.btn_5_p3.background_color=(0, 1, 0, 1)
            self.btn_7_p3.background_color=(0, 1, 0, 1)
            self.btn_7_p3.background_color=(0, 1, 0, 1)
        if function_output_list[2][3] == 'n':
            self.btn_6_p3.background_color=(1, 0, 0, 1)
            self.btn_6_p3.background_color=(1, 0, 0, 1)
            self.btn_8_p3.background_color=(1, 0, 0, 1)
            self.btn_8_p3.background_color=(1, 0, 0, 1)
        elif function_output_list[2][3] == 'a':
            self.btn_6_p3.background_color=(0, 1, 0, 1)
            self.btn_6_p3.background_color=(0, 1, 0, 1)
            self.btn_8_p3.background_color=(0, 1, 0, 1)
            self.btn_8_p3.background_color=(0, 1, 0, 1)

                
    def refresh_function(self, button):
        
        horizontal = BoxLayout(orientation='horizontal')
        self.add_widget(horizontal)
        
        self.label_1 = Label(size_hint_x = .2)
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
        
        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.conclusion_label = Label(text='Ganzformel', size_hint_x = 2.5)
        self.syllogism_box_row_6.add_widget(self.conclusion_label)

        self.btn_1_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_c)
        self.btn_2_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_c)
        self.btn_3_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_c)
        self.btn_4_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_c)
        self.btn_5_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_c)
        self.btn_6_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_c)
        self.btn_7_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_c)
        self.btn_8_c = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_c)

        self.syllogism_box_col_2 = BoxLayout(orientation='vertical')
        vertical.add_widget(self.syllogism_box_col_2)

        self.syllogism_box_row_4 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_4)
        
        self.premis_one_label = Label(text='1. Formel', size_hint_x = 2.5)
        self.syllogism_box_row_4.add_widget(self.premis_one_label)

        self.btn_1_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_1_p1)
        self.btn_2_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_2_p1)
        self.btn_3_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_3_p1)
        self.btn_4_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_4_p1)
        self.btn_5_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_5_p1)
        self.btn_6_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_6_p1)
        self.btn_7_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_7_p1)
        self.btn_8_p1 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_8_p1)

        self.syllogism_box_row_5 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_5)
        
        self.premis_two_label = Label(text='2. Formel', size_hint_x = 2.5)
        self.syllogism_box_row_5.add_widget(self.premis_two_label)

        self.btn_1_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_1_p2)
        self.btn_2_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_2_p2)
        self.btn_3_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_3_p2)
        self.btn_4_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_4_p2)
        self.btn_5_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_5_p2)
        self.btn_6_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_6_p2)
        self.btn_7_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_7_p2)
        self.btn_8_p2 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_5.add_widget(self.btn_8_p2)

        self.syllogism_box_row_6 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_6)
        
        self.premis_three_label = Label(text='3. Formel', size_hint_x = 2.5)
        self.syllogism_box_row_6.add_widget(self.premis_three_label)

        self.btn_1_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_1_p3)
        self.btn_2_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_2_p3)
        self.btn_3_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_3_p3)
        self.btn_4_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_4_p3)
        self.btn_5_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_5_p3)
        self.btn_6_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_6_p3)
        self.btn_7_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_7_p3)
        self.btn_8_p3 = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_6.add_widget(self.btn_8_p3)

        self.label_5 = Label()
        vertical.add_widget(self.label_5)

        self.box_horizontal_buttons_down = BoxLayout(orientation='horizontal')
        vertical.add_widget(self.box_horizontal_buttons_down)

        self.btn_n = Button(text='n', color= (0, 0, 0, 1), background_normal='', background_color=(1, 0, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_n)
        variable_btn_n ='n'
        self.btn_n.bind(on_press=self.append_function)

        self.btn_a = Button(text='a', color= (0, 0, 0, 1), background_normal='', background_color=(0, 1, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_a)
        variable_btn_a ='a'
        self.btn_a.bind(on_press=self.append_function)

        self.btn_u = Button(text='u', color= (0, 0, 0, 1), background_normal='', background_color=(1, 1, 1, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_u)
        variable_btn_u ='u'
        self.btn_u.bind(on_press=self.append_function)

        self.label_3 = Label(size_hint_x = .2)
        horizontal.add_widget(self.label_3)
        


        self.refresh_button.bind(on_press=self.clear_widgets_function)


    def __init__(self, **kwargs):
        super(Total_formulas_Playground_right_Screen, self).__init__(**kwargs)
        
        self.refresh_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
        self.add_widget(self.refresh_button)
        self.refresh_button.bind(on_press=self.refresh_function)

class Menu_TransformationsScreen(Screen):
    pass

class TransformationsScreen(Screen):
    global foo_5
    
    foo_5 = []
    

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def inital_judge_values(self, inital_judge):
        if inital_judge == "SaP":
            inital_judge = "AuNA"
        elif inital_judge == "SeP":
            inital_judge = "NAAu"
        elif inital_judge == "SiP":
            inital_judge = "Auuu"
        elif inital_judge == "SoP":
            inital_judge = "uuAu"
        return (inital_judge)

    def output_judge_fn(self, solution):
        if solution == ['A', 'u', 'N', 'A']:
            return "\n\nAll S are P,\nalso known as SaP"
        elif solution == ['A', 'u', 'u', 'u']:
            return "\n\nSome S are P,\nalso known as SiP"
        elif solution == ['N', 'A', 'A', 'u']:
            return "\n\nNo S is P,\nalso known as SeP"
        elif solution == ['u', 'u', 'A', 'u']:
            return "\n\nSome S are no P,\nalso known as SoP"
        else:
            return ("\n\nNo traditional\njudge!")

    def append_function(self, button):
        print(button)
        if foo_5 == []:
            if button == self.btn_n:
                z = foo_5.append('N')
                self.btn_1_inital_judge.text ='N'
                self.btn_1_inital_judge.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_5.append('A')
                self.btn_1_inital_judge.text ='A'
                self.btn_1_inital_judge.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_5.append('u')
                self.btn_1_inital_judge.text ='u'
                self.btn_1_inital_judge.background_color=(1, 1, 1, 1)
        elif len(foo_5) == 1:
            if button == self.btn_n:
                z = foo_5.append('N')
                self.btn_2_inital_judge.text ='N'
                self.btn_2_inital_judge.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_5.append('A')
                self.btn_2_inital_judge.text ='A'
                self.btn_2_inital_judge.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_5.append('u')
                self.btn_2_inital_judge.text ='u'
                self.btn_2_inital_judge.background_color=(1, 1, 1, 1)
        elif len(foo_5) == 2:
            if button == self.btn_n:
                z = foo_5.append('N')
                self.btn_3_inital_judge.text ='N'
                self.btn_3_inital_judge.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_5.append('A')
                self.btn_3_inital_judge.text ='A'
                self.btn_3_inital_judge.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_5.append('u')
                self.btn_3_inital_judge.text ='u'
                self.btn_3_inital_judge.background_color=(1, 1, 1, 1)
        elif len(foo_5) == 3:
            if button == self.btn_n:
                z = foo_5.append('N')
                self.btn_4_inital_judge.text ='N'
                self.btn_4_inital_judge.background_color=(1, 0, 0, 1)
            elif button == self.btn_a:
                z = foo_5.append('A')
                self.btn_4_inital_judge.text ='A'
                self.btn_4_inital_judge.background_color=(0, 1, 0, 1)
            elif button == self.btn_u:
                z = foo_5.append('u')
                self.btn_4_inital_judge.text ='u'
                self.btn_4_inital_judge.background_color=(1, 1, 1, 1)
            self.conclusion_label.text = 'Wähle eine Transformation!'
            self.inversion_btn.disabled = False
            self.conversion_btn.disabled = False
            self.obversion_btn.disabled = False
            self.contraposition_btn.disabled = False
            self.partial_inversion_btn.disabled = False
            self.inital_judge_variable = foo_5
            self.btn_n.disabled = True
            self.btn_a.disabled = True
            self.btn_u.disabled = True
    
    def refresh_function(self, button):

        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.layout_in_layout = BoxLayout(orientation='horizontal')
        self.layout.add_widget(self.layout_in_layout)

        self.vertical = BoxLayout(orientation='vertical')
        self.layout_in_layout.add_widget(self.vertical)
        
        self.boxlayout_up = BoxLayout(orientation='horizontal')
        self.vertical.add_widget(self.boxlayout_up)
    
        self.syllogism_box_col_1 = BoxLayout(orientation='vertical')
        self.vertical.add_widget(self.syllogism_box_col_1)
        
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

        self.dummy_label_two = Label(text='', size_hint_x = 2.5)
        self.syllogism_box_row_1.add_widget(self.dummy_label_two)

        self.syllogism_box_row_2 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_2)
        
        self.dummy_label_three = Label(text='', size_hint_x = 2.5)
        self.syllogism_box_row_2.add_widget(self.dummy_label_three)

        self.p1 = Label(text='P')
        self.syllogism_box_row_2.add_widget(self.p1)
        self.p2 = Label(text='P')
        self.syllogism_box_row_2.add_widget(self.p2)
        self.p3 = Label(text='~P')
        self.syllogism_box_row_2.add_widget(self.p3)
        self.p4 = Label(text='~P')
        self.syllogism_box_row_2.add_widget(self.p4)
        
        self.dummy_label_four = Label(text='', size_hint_x = 2.5)
        self.syllogism_box_row_2.add_widget(self.dummy_label_four)

        self.syllogism_box_row_3 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_3)

        self.conclusion_label_text = Label(text='Ursprüngliches Urteil', size_hint_x = 2.5)
        self.syllogism_box_row_3.add_widget(self.conclusion_label_text)

        self.btn_1_inital_judge = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_3.add_widget(self.btn_1_inital_judge)
        self.btn_2_inital_judge = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_3.add_widget(self.btn_2_inital_judge)
        self.btn_3_inital_judge = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_3.add_widget(self.btn_3_inital_judge)
        self.btn_4_inital_judge = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_3.add_widget(self.btn_4_inital_judge)
    
        self.dummy_label_five = Label(text=' ', size_hint_x = 2.5)
        self.syllogism_box_row_3.add_widget(self.dummy_label_five)

        self.syllogism_box_row_4 = BoxLayout(orientation='horizontal')
        self.syllogism_box_col_1.add_widget(self.syllogism_box_row_4)

        self.transformed_judge_label = Label(text='Transformiertes Urteil', size_hint_x = 2.5)
        self.syllogism_box_row_4.add_widget(self.transformed_judge_label)

        self.btn_1_transformed_judge = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_1_transformed_judge)
        self.btn_2_transformed_judge = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_2_transformed_judge)
        self.btn_3_transformed_judge = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_3_transformed_judge)
        self.btn_4_transformed_judge = Button(color= (0, 0, 0, 1), background_normal='')
        self.syllogism_box_row_4.add_widget(self.btn_4_transformed_judge)

        self.dummy_label_six = Label(text=' ', size_hint_x = 2.5)
        self.syllogism_box_row_4.add_widget(self.dummy_label_six)

        self.syllogism_box_col_2 = BoxLayout(orientation='vertical')
        self.vertical.add_widget(self.syllogism_box_col_2)

        self.conclusion_label = Label(text='Gib eine Formel ein!')
        self.layout.add_widget(self.conclusion_label)

        self.layout_in_layout_2 = BoxLayout(orientation='horizontal', size_hint_y =.4)
        self.layout.add_widget(self.layout_in_layout_2)

        self.conversion_btn = Button(text= 'Konversion')
        self.conversion_btn.disabled = True
        self.conversion_btn.bind(on_press=self.conversion_fn)
        self.layout_in_layout_2.add_widget(self.conversion_btn)

        self.obversion_btn = Button(text= 'Obversion')
        self.obversion_btn.disabled = True
        self.obversion_btn.bind(on_press=self.obversion_fn)
        self.layout_in_layout_2.add_widget(self.obversion_btn)

        self.contraposition_btn = Button(text= 'Kontraposition')
        self.contraposition_btn.disabled = True
        self.contraposition_btn.bind(on_press=self.contraposition_fn)
        self.layout_in_layout_2.add_widget(self.contraposition_btn)

        self.layout_in_layout_3 = BoxLayout(orientation='horizontal', size_hint_y =.4)
        self.layout.add_widget(self.layout_in_layout_3)

        self.partial_inversion_btn = Button(text='Partielle Inversion')
        self.partial_inversion_btn.disabled = True
        self.partial_inversion_btn.bind(on_press=self.partial_inversion_fn)
        self.layout_in_layout_3.add_widget(self.partial_inversion_btn)

        self.inversion_btn = Button(text='Inversion')
        self.inversion_btn.disabled = True
        self.inversion_btn.bind(on_press=self.inversion_fn)
        self.layout_in_layout_3.add_widget(self.inversion_btn)
        
        self.box_horizontal_buttons_down = BoxLayout(orientation='horizontal', size_hint_y =.4)
        self.layout.add_widget(self.box_horizontal_buttons_down)

        self.btn_n = Button(text='n', color= (0, 0, 0, 1), background_normal='', background_color=(1, 0, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_n)
        variable_btn_n ='N'
        self.btn_n.bind(on_press=self.append_function)

        self.btn_a = Button(text='a', color= (0, 0, 0, 1), background_normal='', background_color=(0, 1, 0, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_a)
        variable_btn_a ='A'
        self.btn_a.bind(on_press=self.append_function)

        self.btn_u = Button(text='u', color= (0, 0, 0, 1), background_normal='', background_color=(1, 1, 1, 1))
        self.box_horizontal_buttons_down.add_widget(self.btn_u)
        variable_btn_u ='u'
        self.btn_u.bind(on_press=self.append_function)
        
        self.refresh_button.bind(on_press=self.clear_widgets_function)

    def clear_widgets_function(self, *args):
        self.clear_widgets()
        foo_5.clear()
        
        self.refresh2_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
        self.add_widget(self.refresh2_button)
        
        self.menu_button = Button(text='Menü', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .9})
        self.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.refresh2_button.bind(on_press=self.refresh_function)
        
        self.refresh2_button.bind(on_press=self.clear_widgets_function)

    def __init__(self, **kwargs):
        super(TransformationsScreen, self).__init__(**kwargs)

        self.refresh_button = Button(text='Generiere!', size_hint=(.2, .1), pos_hint={'x': .8, 'y': .8})
        self.add_widget(self.refresh_button)
        self.refresh_button.bind(on_press=self.refresh_function)

    def conversion_fn(self, button):
        inital_judge = self.inital_judge_variable
        print(inital_judge)
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        conversion = [inital_judge_values_[0], inital_judge_values_[2], inital_judge_values_[1], inital_judge_values_[3]]           
        solution = conversion
        output_judge = self.output_judge_fn(solution)
        self.output_buttons_function(solution)
        self.explanation_label = 'S•P -> P•S'
        self.conclusion_label.text = self.explanation_label+'\n'+output_judge

    def obversion_fn(self, button):
        inital_judge = self.inital_judge_variable
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        obversion = [inital_judge_values_[2], inital_judge_values_[3], inital_judge_values_[0], inital_judge_values_[1]]
        solution = obversion
        output_judge = self.output_judge_fn(solution)
        self.output_buttons_function(solution)
        self.explanation_label = 'S•P -> S•~P'
        self.conclusion_label.text = self.explanation_label+'\n'+output_judge

    def contraposition_fn(self, button):
        inital_judge = self.inital_judge_variable
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        contradiction = [inital_judge_values_[3], inital_judge_values_[1], inital_judge_values_[2], inital_judge_values_[0]]
        solution = contradiction
        output_judge = self.output_judge_fn(solution)
        self.output_buttons_function(solution)
        self.explanation_label = 'S•P -> ~P•~S'
        self.conclusion_label.text = self.explanation_label+'\n'+output_judge

    def partial_inversion_fn(self, button):
        inital_judge = self.inital_judge_variable
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        partial_inversion = [inital_judge_values_[1], inital_judge_values_[0], inital_judge_values_[3], inital_judge_values_[2]]
        solution = partial_inversion
        output_judge = self.output_judge_fn(solution)
        self.output_buttons_function(solution)
        self.explanation_label = 'S•P -> ~S•P'
        self.conclusion_label.text = self.explanation_label+'\n'+output_judge

    def inversion_fn(self, button):
        inital_judge = self.inital_judge_variable
        inital_judge_values_ = self.inital_judge_values(inital_judge)
        inversion = [inital_judge_values_[3], inital_judge_values_[2], inital_judge_values_[1], inital_judge_values_[0]]
        solution = inversion
        output_judge = self.output_judge_fn(solution)
        self.output_buttons_function(solution)
        self.explanation_label = 'S•P -> ~S•~P'
        self.conclusion_label.text = self.explanation_label+'\n'+output_judge


    def output_buttons_function(self, solution):
        if solution[0] == 'A':
            self.btn_1_transformed_judge.text = 'A'
            self.btn_1_transformed_judge.background_color=(0, 1, 0, 1)
        elif solution[0] == 'N':
            self.btn_1_transformed_judge.text = 'N'
            self.btn_1_transformed_judge.background_color=(1, 0, 0, 1)
        elif solution[0] == 'u':
            self.btn_1_transformed_judge.text = 'u'
            self.btn_1_transformed_judge.background_color=(1, 1, 1, 1)
        if solution[1] == 'A':
            self.btn_2_transformed_judge.text = 'A'
            self.btn_2_transformed_judge.background_color=(0, 1, 0, 1)
        elif solution[1] == 'N':
            self.btn_2_transformed_judge.text = 'N'
            self.btn_2_transformed_judge.background_color=(1, 0, 0, 1)
        elif solution[1] == 'u':
            self.btn_2_transformed_judge.text = 'u'
            self.btn_2_transformed_judge.background_color=(1, 1, 1, 1)
        if solution[2] == 'A':
            self.btn_3_transformed_judge.text = 'A'
            self.btn_3_transformed_judge.background_color=(0, 1, 0, 1)
        elif solution[2] == 'N':
            self.btn_3_transformed_judge.text = 'N'
            self.btn_3_transformed_judge.background_color=(1, 0, 0, 1)
        elif solution[2] == 'u':
            self.btn_3_transformed_judge.text = 'u'
            self.btn_3_transformed_judge.background_color=(1, 1, 1, 1)
        if solution[3] == 'A':
            self.btn_4_transformed_judge.text = 'A'
            self.btn_4_transformed_judge.background_color=(0, 1, 0, 1)
        elif solution[3] == 'N':
            self.btn_4_transformed_judge.text = 'N'
            self.btn_4_transformed_judge.background_color=(1, 0, 0, 1)
        elif solution[3] == 'u':
            self.btn_4_transformed_judge.text = 'u'
            self.btn_4_transformed_judge.background_color=(1, 1, 1, 1)

class RessourcesScreen(Screen):
    text_syllogism_ressource = 'Strenge Syllogistik,\n Version vom 6. Februar 2019'
            
    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)

class Sat_Screen(Screen):

    def change_screen_menu(self, *args):
        self.parent.current = 'menu'

    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        
        self.scatter = Scatter(do_rotation=False, do_scale=False,\
                  do_translation_y=False, rotation= 90, pos_hint={'x': 0, 'y': 0}, \
                               size_hint_x=None, size_hint_y=None, size=(Window.height, Window.width))
        
        self.layout = GridLayout(cols=1, spacing=13, size_hint_x=1.3, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        self.layout.bind(minimum_height=self.layout.setter('height'))
        
        self.text_1 = Label(text='(x \u00F3 y \u00F3 z) \u00F2 (\u00ACx \u00F3 y \u00F3 \u00ACz) \u00F2 \n(\u00ACx \u00F3 \u00ACy \u00F3 z) \u00F2 (\u00ACx \u00F3 \u00ACy \u00F3 \u00ACz)', font_name= 'my_custom_font', size_hint_y = None)
        self.text_1.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.text_1.bind(width=lambda instance, value: setattr(instance, 'text_size', (value, None)))
        self.layout.add_widget(self.text_1)

        #text dummy x
        for r in range(60):
            self.text_2 = Label(text='')
            self.layout.add_widget(self.text_2)
            
        
        self.boxlayout_sat = BoxLayout(orientation='horizontal', size_hint_y=None)
        self.layout.add_widget(self.boxlayout_sat)
        
        self.col_0 = BoxLayout(orientation='vertical', size_hint_x=2, size_hint_y=9)
        self.boxlayout_sat.add_widget(self.col_0)

        self.s_2_0 = Label(text=' ', size_hint_y= .3)
        self.col_0.add_widget(self.s_2_0)
        self.m_2_0 = Label(text=' ', size_hint_y= .3)
        self.col_0.add_widget(self.m_2_0)
        self.p_2_0 = Label(text=' ', size_hint_y= .3)
        self.col_0.add_widget(self.p_2_0)

        self.sat_list_boxlayout_formulas = ['p \u00E1\u00A5 q \u00E1\u00A5 r', '~p \u00E1\u00A5 q \u00E1\u00A5 ~r', '~p \u00E1\u00A5 ~q \u00E1\u00A5 r', '~p \u00E1\u00A5 ~q \u00E1\u00A5 ~r', ' ']
        
        for i, formula in enumerate(self.sat_list_boxlayout_formulas):
            self.formulas_label = Label(text= formula, font_name='my_custom_font')
            self.col_0.add_widget(self.formulas_label)

        self.sat_list_boxlayout_terms_p = ['P', '~P', 'P', '~P', 'P', '~P', 'P', '~P']
        self.sat_list_boxlayout_terms_q = ['Q', 'Q', '~Q', '~Q', 'Q', 'Q', '~Q', '~Q']
        self.sat_list_boxlayout_terms_r = ['R', 'R', 'R', 'R', '~R', '~R', '~R', '~R']
        
        self.values_list = ['A\u00A5', 'A\u00A5', 'A\u00A5', ' ',\
                            'A\u00A5', 'A\u00A5', 'A\u00A5', 'A\u00A5',\
                            'A\u00A5', ' ', 'A\u00A5', 'A\u00A5',\
                            'A\u00A5', 'A\u00A5', 'A\u00A5', 'A\u00A5',\
                            'A\u00A5', 'A\u00A5', ' ', 'A\u00A5',\
                            'A\u00A5', 'A\u00A5', 'A\u00A5', 'A\u00A5',\
                            'A\u00A5', 'A\u00A5', 'A\u00A5', 'A\u00A5',\
                            ' ', 'A\u00A5', 'A\u00A5', 'A\u00A5',]
        
        count_1 = 0
        
        for j in range(8):

            self.col_x = BoxLayout(orientation= 'vertical', size_hint_x=1, size_hint_y= 9)
            self.boxlayout_sat.add_widget(self.col_x)
            self.head_1 = Label(text= self.sat_list_boxlayout_terms_p[j], font_name= 'my_custom_font', size_hint_y= .3)
            self.col_x.add_widget(self.head_1)
            self.head_2 = Label(text= self.sat_list_boxlayout_terms_q[j], font_name= 'my_custom_font', size_hint_y= .3)
            self.col_x.add_widget(self.head_2)
            self.head_3 = Label(text= self.sat_list_boxlayout_terms_r[j], font_name= 'my_custom_font', size_hint_y= .3)
            self.col_x.add_widget(self.head_3)
            for k in range(4):
                self.value = CustomLabel(text= self.values_list[count_1], color = (0, 0, 0, 1),  font_name= 'my_custom_font')
                if count_1 == 4 or count_1 == 5 or count_1 == 6 or count_1 == 7 or\
                   count_1 == 12 or count_1 == 13 or count_1 == 14 or count_1 == 15 or\
                   count_1 == 20 or count_1 == 21 or count_1 == 22 or count_1 == 23 or\
                   count_1 == 24 or count_1 == 25 or count_1 == 26 or count_1 == 27:
                    self.value.background_color = [.9, 1, .9, 1]
                else:
                    self.value.background_color = [.3, 1, .3, 1]
                count_1 = count_1 + 1
                self.col_x.add_widget(self.value)
                if (j+1 == 2) or (j+1 == 4) or (j+1 == 6) or (j+1 == 7):
                    self.number = EllipseLabel(text= str(j+1), font_name= 'my_custom_font')
                else:
                    self.number = Label(text= str(j+1), font_name= 'my_custom_font')
            self.col_x.add_widget(self.number)
        
        #explanation column
        self.col_explanation = BoxLayout(orientation= 'vertical', size_hint_x=4, size_hint_y= 9)
        self.boxlayout_sat.add_widget(self.col_explanation)
        
        self.sat_list_boxlayout_formulas_explanation = [[['p'], ['\u00E1\u00A5'], ['q'], ['\u00E1\u00A5'], ['r']], [['~p'], ['\u00E1\u00A5'], ['q'], ['\u00E1\u00A5'], ['~r']],\
                                                        [['~p'], ['\u00E1\u00A5'], ['~q'], ['\u00E1\u00A5'], ['r']], [['~p'], ['\u00E1\u00A5'], ['~q'], ['\u00E1\u00A5'], ['~r']]]
        
        for r in range(3):
            self.dummy_label_explanation = Label(text= ' ', size_hint_y= .3)
            self.col_explanation.add_widget(self.dummy_label_explanation)

        self.p_list = [[1, 3, 5, 7], [2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8]]
        
        self.q_list = [[1, 2, 4, 5], [1, 2, 4, 5], [3, 4, 7, 8], [3, 4, 7, 8]]
        
        self.r_list = [[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [5, 6, 7, 8]]

        self.or_numbers_list = [[1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 6, 7, 8], \
                                [1, 2, 3, 4, 6, 7, 8], [2, 3, 4, 5, 6, 7, 8]]
        
        
        for i, formula in enumerate(self.sat_list_boxlayout_formulas_explanation):
            self.col_explanation_2 = BoxLayout(orientation= 'vertical', size_hint_x=1, size_hint_y= 1)
            self.col_explanation.add_widget(self.col_explanation_2)
            self.rows_explanation = BoxLayout(orientation= 'horizontal', size_hint_x=1, size_hint_y= 1)
            self.col_explanation_2.add_widget(self.rows_explanation)
            self.rows_explanation_2 = BoxLayout(orientation= 'horizontal', size_hint_x=1, size_hint_y= 1)
            self.col_explanation_2.add_widget(self.rows_explanation_2)
            
            self.numbers_label_p = CustomLabel(text= str(self.p_list[i]), font_name= 'my_custom_font', color= (0, 0, 0, 1), background_color = [.8, .8, 1, 1])
            self.rows_explanation.add_widget(self.numbers_label_p)
            self.numbers_label_q = CustomLabel(text= str(self.q_list[i]), font_name= 'my_custom_font', color= (0, 0, 0, 1), background_color = [.8, .8, 1, 1])
            self.rows_explanation.add_widget(self.numbers_label_q)
            self.numbers_label_r = CustomLabel(text= str(self.r_list[i]), font_name= 'my_custom_font', color= (0, 0, 0, 1), background_color = [.8, .8, 1, 1])
            self.rows_explanation.add_widget(self.numbers_label_r)
            for j in range(5):
                self.variable_label = CustomLabel(text= formula[j][0], font_name= 'my_custom_font', color= (0, 0, 0, 1), background_color = [.8, .8, 1, 1])
                self.rows_explanation_2.add_widget(self.variable_label)
                if (i == 1) or (i == 3):
                    self.variable_label.background_color = [.8, .8, 1, .8]
            self.or_numbers_list_label = CustomLabel(text= '\u00A9'+str(self.or_numbers_list[i]), font_name= 'my_custom_font', color= (0, 0, 0, 1), background_color = [.8, .8, 1, 1])
            self.col_explanation_2.add_widget(self.or_numbers_list_label)
            if (i == 1) or (i == 3):
                self.numbers_label_p.background_color = [.8, .8, 1, .8]
                self.numbers_label_q.background_color = [.8, .8, 1, .8]
                self.numbers_label_r.background_color = [.8, .8, 1, .8]
                self.or_numbers_list_label.background_color = [.8, .8, 1, .8]

        self.dummy_label_explanation_2 = Label(text= 'B \u00E0\u00A5 C \u00E0\u00A5 D \u00E0\u00A5 E\n\u00A9 [2, 4, 6, 7]', font_name= 'my_custom_font')
        self.col_explanation.add_widget(self.dummy_label_explanation_2)

        self.menu_button = Button(text='Menü', background_normal= '', background_color=(1, 1, 1, .5), color=(0, 0, 0, 1), size_hint_y=None)
        self.layout.add_widget(self.menu_button)
        self.menu_button.bind(on_press=self.change_screen_menu)
        
        self.root = ScrollView(size=(self.scatter.width, self.scatter.height))
        self.root.add_widget(self.layout)
        self.scatter.add_widget(self.root)
        
        self.add_widget(self.scatter)


class TestApp(App):
    
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(Menu_conclusionsScreen(name='menu_conclusions'))
        sm.add_widget(GeneralScreen(name='general'))
        sm.add_widget(Menu_introductionScreen(name='menu_introduction'))
        sm.add_widget(Menu_introductionScreen_1(name='menu_introduction_1'))
        sm.add_widget(Menu_introductionScreen_1b(name='menu_introduction_1b'))
        sm.add_widget(Menu_introductionScreen_2(name='menu_introduction_2'))
        sm.add_widget(Menu_introductionScreen_3(name='menu_introduction_3'))
        sm.add_widget(Menu_conclusion_introductionScreen(name='menu_conclusion_introduction'))
        sm.add_widget(Table_overviewScreen(name='table_overview'))
        sm.add_widget(Table_overviewScreen_2(name='table_overview_2'))
        sm.add_widget(TrainingScreen(name='training'))
        sm.add_widget(Training_calculating_quiz_Screen(name='calculating_quiz'))
        sm.add_widget(Menu_total_formulas_Screen(name='menu-total-formulas'))
        sm.add_widget(Total_formulas_Playground_left_Screen(name='total-formulas-playground-left'))
        sm.add_widget(Total_formulas_Playground_right_Screen(name='total-formulas-playground-right'))
        sm.add_widget(ConclusionsScreen(name='conclusions'))
        sm.add_widget(Menu_TransformationsScreen(name='menu_transformations'))
        sm.add_widget(TransformationsScreen(name='transformations'))
        sm.add_widget(RessourcesScreen(name='ressources'))
        sm.add_widget(Sat_Screen(name='sat'))
        self.use_kivy_settings = False
        return sm
    
    def build_config(self, config):
        config.setdefaults('trainer', {
            'completedsyllogistic': 0,
            'particularpremis': 0})
        
    def build_settings(self, settings):
        settings.add_json_panel('Einstellungen - Syllogistik Trainer',
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

LabelBase.register(name='my_custom_font', 
                   fn_regular='my_custom_font.ttf')

if __name__ == '__main__':
    TestApp().run()

