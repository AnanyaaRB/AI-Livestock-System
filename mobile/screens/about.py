from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView


class AboutScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 25
        self.spacing = 10

        # Title
        title = Label(
            text="ABOUT",
            font_size="28sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )

        self.add_widget(title)

        # Scrollable content
        scroll_view = ScrollView(
            size_hint=(1, 1)
        )

        content = BoxLayout(
            orientation="vertical",
            spacing=15,
            padding=10,
            size_hint_y=None
        )

        content.bind(
            minimum_height=content.setter("height")
        )

        # Project name
        project_title = Label(
            text=(
                "AI-Powered Livestock Breed Selection\n"
                "and Nutrition Advisory System"
            ),
            font_size="21sp",
            bold=True,
            halign="center",
            size_hint_y=None,
            height=90
        )

        content.add_widget(project_title)

        # Description
        description = Label(
            text=(
                "This application helps livestock owners "
                "with breed selection and nutrition-related "
                "advisory using Artificial Intelligence."
            ),
            font_size="16sp",
            halign="center",
            size_hint_y=None,
            height=100
        )

        content.add_widget(description)

        # Features
        features = Label(
            text=(
                "MAIN FEATURES\n\n"
                "• Livestock image upload\n"
                "• AI-based breed analysis\n"
                "• Breed selection support\n"
                "• Nutrition advisory\n"
                "• Analysis history\n"
                "• Mobile-friendly interface"
            ),
            font_size="16sp",
            halign="left",
            size_hint_y=None,
            height=220
        )

        content.add_widget(features)

        # Technologies
        technologies = Label(
            text=(
                "TECHNOLOGIES\n\n"
                "Python\n"
                "Kivy\n"
                "Socket Programming\n"
                "Artificial Intelligence\n"
                "SymPy"
            ),
            font_size="16sp",
            halign="left",
            size_hint_y=None,
            height=190
        )

        content.add_widget(technologies)

        # Team
        team = Label(
            text=(
                "PROJECT TEAM\n\n"
                "Ananyaa – Frontend / Kivy\n"
                "Dharshanaa – Backend / AI\n"
                "Thariha Shri – Testing"
            ),
            font_size="16sp",
            halign="left",
            size_hint_y=None,
            height=150
        )

        content.add_widget(team)

        # Project purpose
        purpose = Label(
            text=(
                "PROJECT PURPOSE\n\n"
                "To provide a simple digital platform "
                "that can assist livestock owners in "
                "making informed breed and nutrition "
                "decisions."
            ),
            font_size="16sp",
            halign="center",
            size_hint_y=None,
            height=130
        )

        content.add_widget(purpose)

        scroll_view.add_widget(content)

        self.add_widget(scroll_view)

        # Back button
        back_button = Button(
            text="BACK TO DASHBOARD",
            font_size="16sp",
            size_hint=(1, None),
            height=55
        )

        back_button.bind(
            on_press=self.open_dashboard
        )

        self.add_widget(back_button)

    def open_dashboard(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "dashboard"