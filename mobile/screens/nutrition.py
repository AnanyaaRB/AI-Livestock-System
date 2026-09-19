from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput


class NutritionScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 10

        # Title
        title = Label(
            text="NUTRITION ADVISORY",
            font_size="25sp",
            bold=True,
            size_hint=(1, None),
            height=55
        )
        self.add_widget(title)

        # Animal type
        animal_label = Label(
            text="Animal Type",
            font_size="16sp",
            size_hint=(1, None),
            height=30
        )
        self.add_widget(animal_label)

        self.animal_spinner = Spinner(
            text="Select Animal",
            values=(
                "Cow",
                "Goat",
                "Sheep",
                "Buffalo",
                "Pig"
            ),
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.animal_spinner)

        # Age
        age_label = Label(
            text="Age (months)",
            font_size="16sp",
            size_hint=(1, None),
            height=30
        )
        self.add_widget(age_label)

        self.age_input = TextInput(
            hint_text="Enter age",
            multiline=False,
            input_filter="int",
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.age_input)

        # Weight
        weight_label = Label(
            text="Weight (kg)",
            font_size="16sp",
            size_hint=(1, None),
            height=30
        )
        self.add_widget(weight_label)

        self.weight_input = TextInput(
            hint_text="Enter weight",
            multiline=False,
            input_filter="float",
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.weight_input)

        # Purpose
        purpose_label = Label(
            text="Purpose / Production Stage",
            font_size="16sp",
            size_hint=(1, None),
            height=30
        )
        self.add_widget(purpose_label)

        self.purpose_spinner = Spinner(
            text="Select Purpose",
            values=(
                "Growth",
                "Milk Production",
                "Meat Production",
                "Breeding",
                "Maintenance"
            ),
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.purpose_spinner)

        # Get advice button
        advice_button = Button(
            text="GET NUTRITION ADVICE",
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )

        advice_button.bind(
            on_press=self.get_advice
        )

        self.add_widget(advice_button)

        # Status
        self.status_label = Label(
            text="Enter livestock details",
            font_size="14sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.status_label)

        # Back button
        back_button = Button(
            text="BACK TO DASHBOARD",
            font_size="15sp",
            size_hint=(1, None),
            height=45
        )

        back_button.bind(
            on_press=self.open_dashboard
        )

        self.add_widget(back_button)

    def get_advice(self, instance):

        animal = self.animal_spinner.text
        age = self.age_input.text
        weight = self.weight_input.text
        purpose = self.purpose_spinner.text

        # Validate animal
        if animal == "Select Animal":

            self.status_label.text = (
                "Please select an animal"
            )

            return

        # Validate age
        if not age:

            self.status_label.text = (
                "Please enter the animal age"
            )

            return

        # Validate weight
        if not weight:

            self.status_label.text = (
                "Please enter the animal weight"
            )

            return

        # Validate purpose
        if purpose == "Select Purpose":

            self.status_label.text = (
                "Please select the purpose"
            )

            return

        # Get ScreenManager
        screen_manager = self.parent.parent

        # Get Nutrition Result screen
        result_screen = (
            screen_manager.get_screen(
                "nutrition_result"
            )
        )

        # Send details to result screen
        result_screen.children[0].set_details(
            animal,
            age,
            weight,
            purpose
        )

        # Open result screen
        screen_manager.current = (
            "nutrition_result"
        )

    def open_dashboard(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "dashboard"