from kivy.app import app
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class GameScreen(Widget):
    pass

class LanguageLearnerApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    LanguageLearnerApp().run()