from kivy.app import App
from kivy.graphics import Line
from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
import webbrowser
import random

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
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
            text: 'Ressources'
            font_size: dp(25)
            on_press: root.manager.current = 'ressources'
        Button:
            text: 'Training'
            font_size: dp(25)
            on_press:
                root.manager.current = 'training'
        Button:
            text: 'Conclusions'
            font_size: dp(25)
            on_press: root.manager.current = 'conclusions'
        Button:
            text: 'Transformations'
            font_size: dp(25)
            on_press: root.manager.current = 'transformations'
        Button:
            text: 'Quit'
            font_size: dp(25)
            on_press: app.stop()

<RessourcesScreen>:
    BoxLayout:
        orientation: "vertical"
        Label:
            text: "Ressources"
            font_size: dp(30)
        Button:
            text: 'Syllogism Version from 19:04, 21 May 2018'
            font_size: dp(25)
            on_press:
                import webbrowser
                webbrowser.open('https://en.wikipedia.org/w/index.php?oldid=842329272#Strict_syllogistic')
    Button:
        text: "Menu"
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

<TrainingScreen>:
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

<TransformationsScreen>:
    Button:
        text: 'Menu'
        on_press: root.manager.current = 'menu'
        size_hint: "0.1", "0.1"
        pos_hint: {"x":0.9,"y":0.9}

""")


# Declare both screens
class MenuScreen(Screen):
    pass


class RessourcesScreen(Screen):
    pass


class TrainingScreen(Screen):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    text_input_str = StringProperty("foo")
    answer_true = "foo"
    random_answer1 = "foo"
    z = 'foo'
    my_text_training_conclusion = 'foo'

    def first_formula_values(self, first_formula):
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
        return (first_formula)

    def second_formula_values(self, second_formula):
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
        conclusion[0] = syllogism_deduction_first_value_n(first_formula, second_formula)
        conclusion[1] = syllogism_deduction_first_value_a(first_formula, second_formula)
        if conclusion[0] == 'n' and conclusion[1] == 'a':
            print('first error at 0')
            return (1)
        conclusion[2] = syllogism_deduction_second_value_n(first_formula, second_formula)
        conclusion[3] = syllogism_deduction_second_value_a(first_formula, second_formula)
        if conclusion[2] == 'n' and conclusion[3] == 'a':
            print('first error at 1')
            return (1)
        conclusion[4] = syllogism_deduction_third_value_n(first_formula, second_formula)
        conclusion[5] = syllogism_deduction_third_value_a(first_formula, second_formula)
        if conclusion[4] == 'n' and conclusion[5] == 'a':
            print('first error at 2')
            return (1)
        conclusion[6] = syllogism_deduction_fourth_value_n(first_formula, second_formula)
        conclusion[7] = syllogism_deduction_fourth_value_a(first_formula, second_formula)
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
        if solution == ["a", "u", "n", "a"]:
            return "All S are P,\nalso known as SaP"
        elif solution == ["a", "u", "u", "u"]:
            return "Some S are P,\nalso known as SiP"
        elif solution == ["n", "a", "a", "u"]:
            return "No S is P,\nalso known as SeP"
        elif solution == ["u", "u", "a", "u"]:
            return "Some S are no P,\nalso known as SoP"
        else:
            return ("No traditional\njudge!")

    # import pdb; pdb.set_trace()
    # first_formula = first_formula_rand()
    # second_formula = second_formula_rand()
    # result_contradiction_test = syllogism_contradiction_test(first_formula, second_formula)
    # if result_contradiction_test == 1:
    #    print('CONTRADICTION! FOLLOWING -CONCLUSION- IS NOT VALID!')
    # else:
    #    print('No contradiction.')

    def output2(self, my_text, my_text2):
        first_formula = my_text
        second_formula = my_text2
        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        solution = self.syllogism_solution(advice_premis_1, advice_premis_2)
        output_ = self.output(solution)
        return [output_, advice_premis_1, advice_premis_2, solution]

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

    # Callback for the checkbox
    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active.text = self.my_text_training_conclusion
        else:
            self.lbl_active.text = "OFF"

    def on_checkbox_Active_2(self, checkboxInstance, isActive):
        if isActive:
            self.lbl_active.text = self.advice_premises_and_conclusion
        else:
            self.lbl_active.text = "OFF"

    # def on_slider_value(self, widget):
     #   print("Slider: " + str(int(widget.value)))
        # self.slider_value_txt = str(int(widget.value))

    def __init__(self, **kwargs):
        super(RelativeLayout, self).__init__(**kwargs)
        with self.canvas:
            self.line = Line(width=2)
        self.bind(center=lambda *args: self.draw())
        self.add_widget(Label(text='Trainer', font_size= 30, size_hint=(.4, .2), pos_hint={'x': .3, 'y': .8}))
        print(self.pos_hint)

        judges_premis_one = ["MaP", "MeP", "MiP", "MoP", "PaM", "PeM", "PiM", "PoM"]
        x = random.randint(0, 7)
        first_formula = judges_premis_one[x]
        my_text = first_formula
        judges_premis_second = ["SaM", "SeM", "SiM", "SoM", "MaS", "MeS", "MiS", "MoS"]
        y = random.randint(0, 7)
        second_formula = judges_premis_second[y]
        my_text2 = second_formula
        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        function_output_list = self.output2(my_text, my_text2)
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

        label_first_premis = Label(text=my_text, font_size= 30, size_hint=(.3, .3), pos_hint= {"x": 0, "y": .7})
        label_second_premis = Label(text=my_text2, font_size= 30, size_hint=(.3, .3), pos_hint={'x': 0, 'y': .6})
        label_questionmark = Label(text='?', font_size= 30, size_hint=(.3, .3), pos_hint={'x': 0, 'y': .5})

        #label_advice = Label(text=my_text_training_conclusion, font_size= 25, size_hint=(.3, .3), pos_hint= {"x": .55, "y": .5})
        #self.add_widget(label_advice)

        # Add checkbox, Label and Widget
        self.add_widget(Label(text='Advice 1:', font_size= 20, size_hint=(.2, .2), pos_hint= {"x": .6, "y": .3}))
        self.add_widget(Label(text='Advice 2:', font_size= 20, size_hint=(.2, .2), pos_hint= {"x": .6, "y": .15}))

        self.active = CheckBox(active=False, size_hint=(.2, .2), pos_hint= {"x": .7, "y": .3})
        self.active_2 = CheckBox(active=False, size_hint=(.2, .2), pos_hint= {"x": .7, "y": .15})

        self.add_widget(self.active)
        self.add_widget(self.active_2)

        # Adding label to screen
        self.lbl_active = Label(text="OFF", font_size= 30, size_hint=(.4, .4), pos_hint= {"x": .5, "y": .55})
        self.add_widget(self.lbl_active)

        # Attach a callback
        self.active.bind(active=self.on_checkbox_Active)
        self.active_2.bind(active=self.on_checkbox_Active_2)



        self.add_widget(label_first_premis)
        self.add_widget(label_second_premis)
        self.add_widget(label_questionmark)

        self.button1 = Button(font_size= 25, size_hint=(.3, .2), pos_hint={'x': .1, 'y': .0})
        self.button2 = Button(font_size= 25, size_hint=(.3, .2), pos_hint={'x': .1, 'y': .2})
        self.button3 = Button(font_size= 25, size_hint=(.3, .2), pos_hint={'x': .1, 'y': .4})
        #self.buttons = [self.button1,self.button2,self.button3]
        self.add_widget(self.button1)
        self.add_widget(self.button2)
        self.add_widget(self.button3)
        #self.buttons = [Button() for _ in range(3)]
        self.buttons = [self.button1, self.button2, self.button3]
        correct_answer = random.randrange(len(self.buttons))
        print(correct_answer)


        print(function_output_list[3])
        button_text = function_output_list[0]

        for i, button in enumerate(self.buttons):
            if i == correct_answer:
                button.text = button_text
                button.bind(on_press=self.right_answer)
            else:
                conclusion_judges = ["All S are P,\nalso known as SaP", "Some S are P,\nalso known as SiP", "No S is P,\nalso known as SeP", "Some S are no P,\nalso known as SoP", "No traditional\njudge!"]
                conclusion_judges.remove(button_text)
                m = random.choice(conclusion_judges)
                button.text = m
                button.bind(on_press=self.wrong_answer)
        #self.add_widget(self.buttons)
        #self.right = right_answer()
        #self.wrong = wrong_answer()

        #def right_answer(self, button):
        #    self.button.text = "correct answer!"



        #print(output)
        #print("S ", solution, " P")
        #print('------------------------------------------------------------')
        #print('1. premis: ', first_formula[0], '-', first_formula[0], ' ', first_formula[1], '-', first_formula[1], ' ',
        #      first_formula[2], '-', first_formula[2], ' ', first_formula[3], '-', first_formula[3])
       # print('2. premis: ', second_formula[0], ' ', second_formula[1], ' ', second_formula[2], ' ', second_formula[3], ',',
       #       second_formula[0], ' ', second_formula[1], ' ', second_formula[2], ' ', second_formula[3])
       # print('------------------------------------------------------------')
       # print('conclusion:', solution[0], ' ', solution[1], ' ', solution[0], ' ', solution[1], ' ', solution[2], ' ',
       #       solution[3], ' ', solution[2], ' ', solution[3])
      #  print(' ')
      #  input("Exit with enter!")

    def on_button_click(self):
        print("Button clicked")
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    # import pdb; pdb.set_trace()



class ConclusionsScreen(Screen):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    text_input_str = StringProperty("foo")
    answer_true = "foo"
    random_answer1 = "foo"
    z = 'foo'
    my_text_training_conclusion = 'foo'

    def first_formula_values(self, first_formula):
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
        return (first_formula)

    def second_formula_values(self, second_formula):
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
        if solution == ["a", "u", "n", "a"]:
            return "\n\nAll S are P,\nalso known as SaP"
        elif solution == ["a", "u", "u", "u"]:
            return "\n\nSome S are P,\nalso known as SiP"
        elif solution == ["n", "a", "a", "u"]:
            return "\n\nNo S is P,\nalso known as SeP"
        elif solution == ["u", "u", "a", "u"]:
            return "\n\nSome S are no P,\nalso known as SoP"
        else:
            return ("\n\nNo traditional\njudge!")

    def output2(self, my_text, my_text2):
        first_formula = my_text
        second_formula = my_text2
        advice_premis_1 = self.first_formula_values(first_formula)
        advice_premis_2 = self.second_formula_values(second_formula)
        solution = self.syllogism_solution(advice_premis_1, advice_premis_2)
        output_ = self.output(solution)
        result_contradiction_test = self.syllogism_contradiction_test(advice_premis_1, advice_premis_2)
        return [output_, advice_premis_1, advice_premis_2, solution, result_contradiction_test]

    # import pdb; pdb.set_trace()



    def __init__(self,**kwargs):
        super (ConclusionsScreen,self).__init__(**kwargs)

        layout_hor = BoxLayout(orientation='horizontal')
        self.add_widget(layout_hor)

        layout = BoxLayout(orientation='vertical')
        layout_hor.add_widget(layout)

        layout_in_layout = BoxLayout(orientation='horizontal')
        layout.add_widget(layout_in_layout)

        self.first_formula = Label(text= 'First Formula: ', font_size= 20)
        layout_in_layout.add_widget(self.first_formula)

        self.first_formula = TextInput(multiline=False)
        layout_in_layout.add_widget(self.first_formula)

        layout_in_layout_2 = BoxLayout(orientation='horizontal')
        layout.add_widget(layout_in_layout_2)

        self.second_formula = Label(text= 'Second Formula: ', font_size= 20)
        layout_in_layout_2.add_widget(self.second_formula)

        self.second_formula = TextInput(multiline=False)
        layout_in_layout_2.add_widget(self.second_formula)

        self.conclusion_label = Label(text='Input Premise-one and Premis-two!', font_size= 20)
        layout_hor.add_widget(self.conclusion_label)

        self.button_calculate = Button(text="Calculate Conclusion!", font_size= 20)
        self.button_calculate.bind(on_press=self.click)
        layout.add_widget(self.button_calculate)

    def click(self,my_button2):

        my_text = self.first_formula.text
        first_formula = my_text
        my_text2 = self.second_formula.text
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
            self.conclusion_label.text = self.advice_premises_and_conclusion + function_output_list[0]



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


class TestApp(App):
    count_random_position = 0

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(RessourcesScreen(name='ressources'))
        sm.add_widget(TrainingScreen(name='training'))
        sm.add_widget(ConclusionsScreen(name='conclusions'))
        sm.add_widget(TransformationsScreen(name='transformations'))

        return sm

    # from your first class......



if __name__ == '__main__':
    TestApp().run()
