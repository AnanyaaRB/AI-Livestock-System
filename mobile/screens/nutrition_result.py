from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class NutritionResultScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 15

        # Store submitted details
        self.animal = ""
        self.age = ""
        self.weight = ""
        self.purpose = ""

        # Title
        title = Label(
            text="NUTRITION RESULT",
            font_size="26sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(title)

        # Animal
        self.animal_label = Label(
            text="Animal: -",
            font_size="18sp",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(self.animal_label)

        # Age
        self.age_label = Label(
            text="Age: -",
            font_size="18sp",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(self.age_label)

        # Weight
        self.weight_label = Label(
            text="Weight: -",
            font_size="18sp",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(self.weight_label)

        # Purpose
        self.purpose_label = Label(
            text="Purpose: -",
            font_size="18sp",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(self.purpose_label)

        # Advisory placeholder
        advisory = Label(
            text=(
                "Nutrition recommendations will appear here\n"
                "after the AI backend is connected."
            ),
            font_size="16sp",
            halign="center",
            size_hint=(1, None),
            height=70
        )
        self.add_widget(advisory)

        # Space
        self.add_widget(Widget())

        # Back to nutrition
        back_button = Button(
            text="BACK TO NUTRITION",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        back_button.bind(
            on_press=self.open_nutrition
        )

        self.add_widget(back_button)

        # Dashboard button
        dashboard_button = Button(
            text="BACK TO DASHBOARD",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        dashboard_button.bind(
            on_press=self.open_dashboard
        )

        self.add_widget(dashboard_button)

    def set_details(
        self,
        animal,
        age,
        weight,
        purpose
    ):

        self.animal = animal
        self.age = age
        self.weight = weight
        self.purpose = purpose

        self.animal_label.text = (
            f"Animal: {animal}"
        )

        self.age_label.text = (
            f"Age: {age} months"
        )

        self.weight_label.text = (
            f"Weight: {weight} kg"
        )

        self.purpose_label.text = (
            f"Purpose: {purpose}"
        )

    def open_nutrition(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "nutrition"

    def open_dashboard(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "dashboard"