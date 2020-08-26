# Import other Python stuff
import time
# Import kivy modules
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.input.factory import MotionEventFactory
from kivy.uix.button import Button


class SigninWindow(BoxLayout):
    # Initialization function
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    # Validates the user's username and password
    def validate_user(self):
        # Set values
        username = self.ids.username_field
        password = self.ids.password_field
        info = self.ids.info

        # convert to strings?
        username = username.text 
        password = password.text

        # Is the password/username blank?
        if username == '' or password == '':
            info.text = ("[color=#ff0000] Username or password required! [/color]")

        # Check for user accounts
        else: 
            # Is the username and password match the admin account login?
            if username == "admin" and password == "admin":
                info.text = ("[color=#00ff00] Welcome Admin! You have logged in! [/color]")

            # Is the user me?
            elif username == "Zyjin" and password == "gamer":
                info.text = ("[color=#00ff00] Welcome Nerd! You have logged in! [/color]")

            # Not a valid user
            else:
                info.text = '[color=#ff0000] Invalid Username and/or Password![/color]'
    

    
    # Popup creation function for exiting program
    def createExitPopup(self):
        content = Button(text="Really Exit?")
        popup = Popup(content=content, auto_dismiss = False, background = 'atlas://data/images/defaulttheme/button_pressed')

        # Exit the program after a short delay
        def exitProgram(self):
            quit()
        content.bind(on_press=exitProgram)
        popup.open()

    # Kivy doodoo popup
    def createKivyPopup(self):
        content = Button(text="Yes")
        popup = Popup(title="is Kivy Doodoo?", content=content, auto_dismiss = False)

        content.bind(on_press=popup.dismiss)
        popup.open()



# Signin must be the name of the signin.kv file
class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    # Create an instance of an app
    SigninApp().run()