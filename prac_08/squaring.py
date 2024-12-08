"""
CP1404/CP5632 Practical
Kivy GUI program to square a number
Modified to include layout and color changes
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Lindsay Ward'


class SquareNumberApp(App):
    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (400, 150)
        self.title = "Square Number"
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self, value):
        """ Handle calculation (button press), output result to label widget """
        try:
            result = float(value) ** 2
            self.root.ids.output_label.text = str(result)
        except ValueError:
            self.root.ids.output_label.text = "Invalid input!"


SquareNumberApp().run()
