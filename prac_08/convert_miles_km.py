from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934

class MilesConverterApp(App):
    result = StringProperty()

    def build(self):
        self.result = "0.0 km"
        return Builder.load_file('convert_miles_km.kv')

    def handle_convert(self):
        self.result = self.convert_miles()

    def handle_increment(self, change):
        try:
            miles = int(self.root.ids.input_miles.text)
        except ValueError:
            miles = 0
        miles += change
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def convert_miles(self):
        try:
            miles = float(self.root.ids.input_miles.text)
            return f"{miles * MILES_TO_KM:.3f} km"
        except ValueError:
            return "0.0 km"

MilesConverterApp().run()