from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class HomeScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 40
        self.spacing = 20

        # Top spacing
        self.add_widget(Widget())

        # App title
        title = Label(
            text="AI LIVESTOCK\nADVISORY SYSTEM",
            font_size="28sp",
            bold=True,
            halign="center"
        )
        self.add_widget(title)

        # Description
        description = Label(
            text="AI-powered livestock breed selection\n"
                 "and nutrition advisory system",
            font_size="17sp",
            halign="center"
        )
        self.add_widget(description)

        # Space
        self.add_widget(Widget())

        # Get Started button
        start_button = Button(
            text="GET STARTED",
            font_size="18sp",
            size_hint=(1, None),
            height=60
        )

        start_button.bind(on_press=self.open_login)

        self.add_widget(start_button)

        # Supported animals
        animals = Label(
            text="Supports: Cow • Goat • Sheep • Buffalo • Pig",
            font_size="14sp",
            halign="center"
        )
        self.add_widget(animals)

        # Bottom spacing
        self.add_widget(Widget())

    def open_login(self, instance):

        # Get the ScreenManager
        screen_manager = self.parent.parent

        # Move to Login screen
        screen_manager.current = "login"
