from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget


class ResultScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 15

        # Store uploaded image
        self.selected_image = None

        # Title
        title = Label(
            text="AI ANALYSIS RESULT",
            font_size="26sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(title)

        # Uploaded image
        self.result_image = Image(
            size_hint=(1, 0.35)
        )
        self.add_widget(self.result_image)

        # Animal type
        animal = Label(
            text="Animal Type: Cow",
            font_size="20sp",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(animal)

        # Breed
        breed = Label(
            text="Predicted Breed: Jersey",
            font_size="20sp",
            size_hint=(1, None),
            height=45
        )
        self.add_widget(breed)

        # Confidence
        confidence = Label(
            text="Confidence: 92%",
            font_size="18sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(confidence)

        # Explanation
        explanation = Label(
            text="The AI identified this livestock based on\n"
                 "visual characteristics from the uploaded image.",
            font_size="15sp",
            halign="center",
            size_hint=(1, None),
            height=60
        )
        self.add_widget(explanation)

        # Space
        self.add_widget(Widget())

        # Back to dashboard
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

    def set_image(self, image_path):

        # Store image path
        self.selected_image = image_path

        # Display uploaded image
        self.result_image.source = image_path
        self.result_image.reload()

    def open_dashboard(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "dashboard"