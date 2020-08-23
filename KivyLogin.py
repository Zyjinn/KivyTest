# Basic Kivy imports
import kivy
from kivy.app import App
from kivy.uix.label import Label
# More Kivy Imports for login
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
# Import box layout
from kivy.uix.boxlayout import BoxLayout
# Require Kivy
kivy.require("1.10.1")

# Displays the layout of the application
class LoginUI(App):
    
    def build(self):
        self.title = "login ui"
        return Login()

# The meat of the code
class Login(GridLayout):
    
    # Function for the login button
    # Print's the username and password as verification that the function works
    def loginBtn(self, instance):
        print(f'{self.username.text}' + ',' + f'{self.password.text}')

    # Create a popup when login is pressed
    def createPopUp(self, title, msg):
        username = self.username
        box = BoxLayout(orientation= 'vertical', padding = (10))
        box.add_widget(Label(text= msg))
        btnOk = Button(text = "Ok")

        box.add_widget(btnOk)

        popup = Popup(title=title, title_size = 50, title_align = "center", content= box, size_hint=(None, None), size = (300, 200), auto_dismiss = True)

        btnOk.bind(on_press = popup.dismiss)
        popup.open()

    # Logs the user in if the "Enter" key is pressed
    def on_keyboard_down(self, instance, keyboard, keycode, text, modifiers):
        if keycode == 40: # Or 36 or 40?
            self.loginBtn(instance)
            username = self.username
            loginMsg = str(username) + "Logged in!"
            self.createPopUp("Success", loginMsg)

    # Initialization function
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set number of cols to 1
        self.cols = 1

        # Set window size to 500x300
        Window.size = (500, 300)

        # Create header Example Widget
        self.add_widget(Label(text="Login UI Example"))

        # Create Username widget
        self.add_widget(Label(text="Username"))
        self.username = TextInput(multiline=False, write_tab=False)
        self.username.focus=True
        self.add_widget(self.username)

        # Create Password widget
        self.add_widget(Label(text="Password: "))
        self.password = TextInput(multiline=False, write_tab=False, password=True)
        self.add_widget(self.password)

        # Create a button
        self.connect = Button(text="login")
        self.connect.bind(on_press=self.loginBtn)
        self.add_widget(self.connect)

        Window.bind(on_key_down=self.on_keyboard_down)
        
# Main
if __name__ == "__main__":
    LoginUI().run()
