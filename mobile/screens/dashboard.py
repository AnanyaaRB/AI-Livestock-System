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

        # Breed Selection button
        breed_button = Button(
            text="BREED SELECTION",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )
        self.add_widget(breed_button)

        # Nutrition button
        nutrition_button = Button(
            text="NUTRITION ADVISORY",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )
        self.add_widget(nutrition_button)

        # Upload button
        upload_button = Button(
            text="UPLOAD LIVESTOCK IMAGE",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        upload_button.bind(on_press=self.open_upload)

        self.add_widget(upload_button)

        # History button
        history_button = Button(
            text="HISTORY",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )
        self.add_widget(history_button)

        # About button
        about_button = Button(
            text="ABOUT",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )
        self.add_widget(about_button)

    def open_upload(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "upload"