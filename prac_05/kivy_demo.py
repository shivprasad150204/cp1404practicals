from kivy.app import App
from kivy.lang import Builder

class SimpleKivyApp(App):
    def build(self):
        self.title = "Kivy UI Demo"
        return Builder.load_file('kivy_layout.kv')

SimpleKivyApp().run()
