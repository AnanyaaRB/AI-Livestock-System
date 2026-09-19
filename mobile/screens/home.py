from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class HomeScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 35
        self.spacing = 15

        # Top spacing
        self.add_widget(
            Widget(
                size_hint_y=0.18
            )
        )

        # Main title
        title = Label(
            text="AI LIVESTOCK",
            font_size="32sp",
            bold=True,
            halign="center",
            size_hint=(1, None),
            height=50
        )

        self.add_widget(title)

        # Subtitle
        subtitle = Label(
            text="ADVISORY SYSTEM",
            font_size="23sp",
            bold=True,
            halign="center",
            size_hint=(1, None),
            height=45
        )

        self.add_widget(subtitle)

        # Project description
        description = Label(
            text=(
                "AI-powered livestock breed selection\n"
                "and nutrition advisory system"
            ),
            font_size="17sp",
            halign="center",
            size_hint=(1, None),
            height=75
        )

        self.add_widget(description)

        # Space
        self.add_widget(
            Widget(
                size_hint_y=0.12
            )
        )

        # Feature information
        features = Label(
            text=(
                "Breed Selection  •  Nutrition Advice\n"
                "Image Analysis  •  Analysis History"
            ),
            font_size="14sp",
            halign="center",
            size_hint=(1, None),
            height=55
        )

        self.add_widget(features)

        # Get Started button
        start_button = Button(
            text="GET STARTED",
            font_size="19sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )

        start_button.bind(
            on_press=self.open_login
        )

        self.add_widget(start_button)

        # Supported animals
        animals = Label(
            text=(
                "Supports: Cow • Goat • Sheep • "
                "Buffalo • Pig"
            ),
            font_size="14sp",
            halign="center",
            size_hint=(1, None),
            height=45
        )

        self.add_widget(animals)

        # Bottom spacing
        self.add_widget(
            Widget(
                size_hint_y=0.18
            )
        )

    def open_login(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "login"
