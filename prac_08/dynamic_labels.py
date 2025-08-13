from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana"]

    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in self.names:
            self.root.ids.main.add_widget(Label(text=name))
        return self.root

DynamicLabelsApp().run()