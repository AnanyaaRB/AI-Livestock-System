from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.widget import Widget


class BreedSelectionScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 15

        # Top spacing
        self.add_widget(Widget())

        # Title
        title = Label(
            text="BREED SELECTION",
            font_size="26sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(title)

        # Instructions
        instructions = Label(
            text="Select the type of livestock",
            font_size="17sp",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(instructions)

        # Animal selection
        self.animal_spinner = Spinner(
            text="Select Animal",
            values=(
                "Cow",
                "Goat",
                "Sheep",
                "Buffalo",
                "Pig"
            ),
            font_size="17sp",
            size_hint=(1, None),
            height=55
        )
        self.add_widget(self.animal_spinner)

        # Continue button
        continue_button = Button(
            text="CONTINUE",
            font_size="18sp",
            size_hint=(1, None),
            height=55
        )

        continue_button.bind(
            on_press=self.select_animal
        )

        self.add_widget(continue_button)

        # Status
        self.status_label = Label(
            text="Please select an animal",
            font_size="15sp",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(self.status_label)

        # Back button
        back_button = Button(
            text="BACK TO DASHBOARD",
            font_size="16sp",
            size_hint=(1, None),
            height=50
        )

        back_button.bind(
            on_press=self.open_dashboard
        )

        self.add_widget(back_button)

        # Bottom spacing
        self.add_widget(Widget())

    def select_animal(self, instance):

        animal = self.animal_spinner.text

        if animal == "Select Animal":

            self.status_label.text = (
                "Please select an animal"
            )

            return

        self.status_label.text = (
            f"Selected animal: {animal}"
        )

        print("Selected animal:", animal)

    def open_dashboard(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "dashboard"