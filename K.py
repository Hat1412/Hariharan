from kivy.app import App
from kivy.uix.gridlayout import GridLayout

# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.button import Button
from kivy.uix import *


class GRID(GridLayout):
    def __init__(self, **kwargs):
        super(GRID, self).__init__(**kwargs)
        self.cols = 2
        l = [
            label.Label(text="Name"),
            textinput.TextInput(multiline=False),
            # Label(text="Age"),
            # TextInput(multiline=False),
        ]
        for i in l:
            self.add_widget(i)


class Myapp(App):
    def build(self):
        return GRID()


if __name__ == "__main__":
    Myapp().run()
