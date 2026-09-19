from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class DashboardScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 15

        # Top spacing
        self.add_widget(Widget())

        # Title
        title = Label(
            text="DASHBOARD",
            font_size="28sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(title)

        # Welcome message
        welcome = Label(
            text="Welcome to AI Livestock Advisory System",
            font_size="16sp",
            halign="center",
            size_hint=(1, None),
            height=50
        )
        self.add_widget(welcome)

        # Breed Selection
        breed_button = Button(
            text="BREED SELECTION",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        breed_button.bind(
            on_press=self.open_breed_selection
        )

        self.add_widget(breed_button)

        # Nutrition Advisory
        nutrition_button = Button(
            text="NUTRITION ADVISORY",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        nutrition_button.bind(
            on_press=self.open_nutrition
        )

        self.add_widget(nutrition_button)

        # Upload Image
        upload_button = Button(
            text="UPLOAD LIVESTOCK IMAGE",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        upload_button.bind(
            on_press=self.open_upload
        )

        self.add_widget(upload_button)

        # History
        history_button = Button(
            text="HISTORY",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        history_button.bind(
            on_press=self.open_history
        )

        self.add_widget(history_button)

        # About
        about_button = Button(
            text="ABOUT",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        about_button.bind(
            on_press=self.open_about
        )

        self.add_widget(about_button)

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