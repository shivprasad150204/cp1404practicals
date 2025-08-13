from kivy.app import App
from kivy.lang import Builder

KV = 'squaring.kv'

class SquaringApp(App):
    def build(self):
        self.root = Builder.load_file(KV)
        return self.root

    def handle_calculate(self):
        try:
            number = int(self.root.ids.input_number.text)
            self.root.ids.output_label.text = str(number ** 2)
        except ValueError:
            self.root.ids.output_label.text = '0'

SquaringApp().run()