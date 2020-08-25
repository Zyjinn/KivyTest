# Import
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class SigninWindow(BoxLayout):
    pass

class SigninApp(App):
    def build(self):
        return SigninWindow()

if __name__ == "__main__":
    # Create an instance of an app
    SigninApp().run()