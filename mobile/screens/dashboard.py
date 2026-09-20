from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class DashboardScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 12

        # Top spacing
        self.add_widget(
            Widget(size_hint_y=0.10)
        )

        # Title
        title = Label(
            text="AI LIVESTOCK",
            font_size="30sp",
            bold=True,
            size_hint=(1, None),
            height=45
        )
        self.add_widget(title)

        subtitle = Label(
            text="ADVISORY SYSTEM",
            font_size="20sp",
            bold=True,
            size_hint=(1, None),
            height=35
        )
        self.add_widget(subtitle)

        welcome = Label(
            text="Welcome! Choose a service below",
            font_size="16sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(welcome)

        self.add_widget(
            Widget(
                size_hint_y=None,
                height=10
            )
        )

        # Breed Selection
        breed_button = Button(
            text="BREED SELECTION",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )
        breed_button.bind(
            on_press=lambda instance: self.change_screen("breed")
        )
        self.add_widget(breed_button)

        # Nutrition
        nutrition_button = Button(
            text="NUTRITION ADVISORY",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )
        nutrition_button.bind(
            on_press=lambda instance: self.change_screen("nutrition")
        )
        self.add_widget(nutrition_button)

        # Upload
        upload_button = Button(
            text="UPLOAD LIVESTOCK IMAGE",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )
        upload_button.bind(
            on_press=lambda instance: self.change_screen("upload")
        )
        self.add_widget(upload_button)

        # History
        history_button = Button(
            text="ANALYSIS HISTORY",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )
        history_button.bind(
            on_press=lambda instance: self.change_screen("history")
        )
        self.add_widget(history_button)

        # About
        about_button = Button(
            text="ABOUT PROJECT",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )
        about_button.bind(
            on_press=lambda instance: self.change_screen("about")
        )
        self.add_widget(about_button)

        self.add_widget(
            Widget(size_hint_y=0.10)
        )

    def change_screen(self, screen_name):
        print("Opening screen:", screen_name)

        # Walk up the widget tree until ScreenManager is found
        widget = self

        while widget.parent is not None:
            widget = widget.parent

            if hasattr(widget, "current"):
                widget.current = screen_name
                print("Changed to:", screen_name)
                return

        print("ERROR: ScreenManager not found")