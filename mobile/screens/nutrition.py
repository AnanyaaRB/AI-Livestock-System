import requests

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

        title = Label(
            text="NUTRITION ADVISORY",
            font_size="25sp",
            bold=True,
            size_hint=(1, None),
            height=55
        )
        self.add_widget(title)

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
                "Buffalo"
            ),
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.animal_spinner)

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

        self.status_label = Label(
            text="Enter livestock details",
            font_size="14sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(self.status_label)

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

        if animal == "Select Animal":
            self.status_label.text = (
                "Please select an animal"
            )
            return

        if not age:
            self.status_label.text = (
                "Please enter the animal age"
            )
            return

        if not weight:
            self.status_label.text = (
                "Please enter the animal weight"
            )
            return

        if purpose == "Select Purpose":
            self.status_label.text = (
                "Please select the purpose"
            )
            return

        self.status_label.text = (
            "Getting nutrition advice..."
        )

        try:
            # Backend uses lowercase animal names
            animal_name = animal.lower()

            # Connect to Flask nutrition endpoint
            url = f"http://127.0.0.1:5000/nutrition/{animal_name}"

            response = requests.get(
                url,
                timeout=10
            )

            if response.status_code != 200:
                self.status_label.text = (
                    "Backend request failed"
                )
                return

            nutrition_data = response.json()

            if not nutrition_data:
                self.status_label.text = (
                    "No nutrition data available"
                )
                return

            screen_manager = self.parent.parent

            result_screen = (
                screen_manager.get_screen(
                    "nutrition_result"
                )
            )

            result_screen.children[0].set_details(
                animal,
                age,
                weight,
                purpose,
                nutrition_data
            )

            screen_manager.current = (
                "nutrition_result"
            )

        except requests.exceptions.ConnectionError:

            self.status_label.text = (
                "Cannot connect to backend"
            )

        except requests.exceptions.Timeout:

            self.status_label.text = (
                "Backend request timed out"
            )

        except Exception as error:

            print("Nutrition error:", error)

            self.status_label.text = (
                "Unable to get nutrition advice"
            )

    def open_dashboard(self, instance):

        screen_manager = self.parent.parent

        screen_manager.current = "dashboard"