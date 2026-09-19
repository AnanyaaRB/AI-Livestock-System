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
        self.add_widget(Widget(
            size_hint_y=0.15
        ))

        # App title
        title = Label(
            text="AI LIVESTOCK",
            font_size="30sp",
            bold=True,
            size_hint=(1, None),
            height=45
        )

        self.add_widget(title)

        # App subtitle
        subtitle = Label(
            text="ADVISORY SYSTEM",
            font_size="20sp",
            bold=True,
            size_hint=(1, None),
            height=35
        )

        self.add_widget(subtitle)

        # Welcome message
        welcome = Label(
            text=(
                "Welcome! Choose a service below"
            ),
            font_size="16sp",
            size_hint=(1, None),
            height=40
        )

        self.add_widget(welcome)

        # Small spacing
        self.add_widget(
            Widget(
                size_hint_y=None,
                height=10
            )
        )

        # Breed Selection button
        breed_button = Button(
            text="BREED SELECTION",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )

        breed_button.bind(
            on_press=self.open_breed_selection
        )

        self.add_widget(breed_button)

        # Nutrition Advisory button
        nutrition_button = Button(
            text="NUTRITION ADVISORY",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )

        nutrition_button.bind(
            on_press=self.open_nutrition
        )

        self.add_widget(nutrition_button)

        # Upload Image button
        upload_button = Button(
            text="UPLOAD LIVESTOCK IMAGE",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )

        upload_button.bind(
            on_press=self.open_upload
        )

        self.add_widget(upload_button)

        # History button
        history_button = Button(
            text="ANALYSIS HISTORY",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )

        history_button.bind(
            on_press=self.open_history
        )

        self.add_widget(history_button)

        # About button
        about_button = Button(
            text="ABOUT PROJECT",
            font_size="17sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )

        about_button.bind(
            on_press=self.open_about
        )

        self.add_widget(about_button)

        # Bottom spacing
        self.add_widget(
            Widget(
                size_hint_y=0.15
            )
        )

    def open_breed_selection(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "breed"

    def open_nutrition(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "nutrition"

    def open_upload(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "upload"

    def open_history(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "history"

    def open_about(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "about"