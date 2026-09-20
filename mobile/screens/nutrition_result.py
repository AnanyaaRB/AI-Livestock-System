from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class NutritionResultScreen(BoxLayout):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 12

        self.animal = ""
        self.age = ""
        self.weight = ""
        self.purpose = ""

        self.feed = ""
        self.water = ""
        self.supplements = ""

        title = Label(
            text="NUTRITION RESULT",
            font_size="26sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(title)

        self.animal_label = Label(
            text="Animal: -",
            font_size="18sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.animal_label)

        self.age_label = Label(
            text="Age: -",
            font_size="18sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.age_label)

        self.weight_label = Label(
            text="Weight: -",
            font_size="18sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.weight_label)

        self.purpose_label = Label(
            text="Purpose: -",
            font_size="18sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.purpose_label)

        self.feed_label = Label(
            text="Feed: -",
            font_size="16sp",
            halign="left",
            size_hint=(1, None),
            height=55
        )
        self.add_widget(self.feed_label)

        self.water_label = Label(
            text="Water: -",
            font_size="16sp",
            halign="left",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(self.water_label)

        self.supplements_label = Label(
            text="Supplements: -",
            font_size="16sp",
            halign="left",
            size_hint=(1, None),
            height=55
        )
        self.add_widget(self.supplements_label)

        self.add_widget(
            Widget()
        )

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
        purpose,
        nutrition_data
    ):

        self.animal = animal
        self.age = age
        self.weight = weight
        self.purpose = purpose

        self.feed = nutrition_data.get(
            "feed",
            "Not available"
        )

        self.water = nutrition_data.get(
            "water",
            "Not available"
        )

        self.supplements = nutrition_data.get(
            "supplements",
            "Not available"
        )

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

        self.feed_label.text = (
            f"Feed: {self.feed}"
        )

        self.water_label.text = (
            f"Water: {self.water}"
        )

        self.supplements_label.text = (
            f"Supplements: {self.supplements}"
        )

    def open_nutrition(self, instance):

        screen_manager = self.parent.parent

        screen_manager.current = "nutrition"

    def open_dashboard(self, instance):

        screen_manager = self.parent.parent

        screen_manager.current = "dashboard"