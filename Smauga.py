from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class MyNotyApp(App):
    def build(self):
        return LoginScreen()

class LoginScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.name_input = TextInput(hint_text='Enter your name')
        self.age_input = TextInput(hint_text='Enter your age')

        login_button = Button(text="Login", on_press=self.login)

        self.add_widget(Label(text='Welcome to Smauga!', font_size='20sp'))
        self.add_widget(self.name_input)
        self.add_widget(self.age_input)
        self.add_widget(login_button)

    def login(self, instance):
        # Retrieve user input
        user_name = self.name_input.text
        user_age = self.age_input.text

        # Example of a welcome message using the entered name and age
        welcome_message = f"Welcome, {user_name}! As a {user_age}-year-old, Peepi is here to assist you."
        print(welcome_message)

        # Call the next screen or functionality here
        # Example: self.manager.current = 'main_screen'

if __name__ == "__main__":
    MyNotyApp().run()
