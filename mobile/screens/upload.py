import os

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

from plyer import filechooser


class UploadScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 15

        # Store selected image path
        self.selected_image = None

        # Title
        title = Label(
            text="UPLOAD LIVESTOCK IMAGE",
            font_size="24sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(title)

        # Instructions
        instructions = Label(
            text="Choose a clear image of the livestock",
            font_size="16sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(instructions)

        # Image preview
        self.preview = Image(
            size_hint=(1, 0.50)
        )
        self.add_widget(self.preview)

        # Choose image button
        choose_button = Button(
            text="CHOOSE IMAGE",
            font_size="18sp",
            size_hint=(1, None),
            height=55
        )

        choose_button.bind(
            on_press=self.choose_image
        )

        self.add_widget(choose_button)

        # Continue button
        continue_button = Button(
            text="CONTINUE",
            font_size="18sp",
            size_hint=(1, None),
            height=55
        )

        continue_button.bind(
            on_press=self.process_image
        )

        self.add_widget(continue_button)

        # Status
        self.status_label = Label(
            text="No image selected",
            font_size="14sp",
            size_hint=(1, None),
            height=40
        )

        self.add_widget(self.status_label)

    def choose_image(self, instance):

        # Open operating system file picker
        filechooser.open_file(
            on_selection=self.image_selected,
            filters=[
                "*.png",
                "*.jpg",
                "*.jpeg"
            ]
        )

    def image_selected(self, selection):

        if not selection:

            self.status_label.text = (
                "No image selected"
            )

            return

        # Get selected image path
        image_path = selection[0]

        # Check file
        if not os.path.isfile(image_path):

            self.status_label.text = (
                "Invalid image file"
            )

            return

        # Store selected image
        self.selected_image = image_path

        # Display preview
        self.preview.source = image_path
        self.preview.reload()

        self.status_label.text = (
            "Image selected successfully"
        )

        print("Selected image:", image_path)

    def process_image(self, instance):

        # Check whether image is selected
        if not self.selected_image:

            self.status_label.text = (
                "Please choose an image first"
            )

            return

        print("Image ready for AI analysis:")
        print(self.selected_image)

        # Get ScreenManager
        screen_manager = self.parent.parent

        # Get ResultScreen
        result_screen = screen_manager.get_screen("result")

        # Send selected image to ResultScreen
        result_screen.children[0].set_image(
            self.selected_image
        )

        # Open Result screen
        screen_manager.current = "result"