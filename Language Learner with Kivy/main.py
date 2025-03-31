from kivy.app import app
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty
from kivy.core.window import Window

Window.clearcolor = (1,1,1,1)
Window.size = (400,600)

class ProgressBar(Widget):
    pass

class ImageBox(Widget):
    pass

class GameScreen(Widget):
    pass

class LanguageLearnerApp(App):
    def build(self):
        game_screen = GameScreen()
        return GameScreen()

if __name__ == '__main__':
    LanguageLearnerApp().run()