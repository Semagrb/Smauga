from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from peepi import Peepi

class MainScreen(BoxLayout):
    def __init__(self, user_name, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = "vertical"

        welcome_label = Label(text=f"Welcome, {user_name}!", font_size='20sp')
        advice_button = Button(text="Get Advice", on_press=self.get_advice)

        self.add_widget(welcome_label)
        self.add_widget(advice_button)

    def get_advice(self, instance):
        advice = Peepi.get_advice()
        print(advice)
