from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Main program - Kivy app to dynamically create labels."""

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        # List of names (data)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create a Label for each name in the list and add to the GUI."""
        for name in self.names:
            # Create a Label with the text as the name
            temp_label = Label(text=name, font_size=24)
            # Add the Label to the "main" BoxLayout
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
