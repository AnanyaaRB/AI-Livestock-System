from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class HistoryScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 25
        self.spacing = 10

        # Title
        title = Label(
            text="ANALYSIS HISTORY",
            font_size="26sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )

        self.add_widget(title)

        # Information message
        info = Label(
            text="Your previous livestock analysis results",
            font_size="15sp",
            size_hint=(1, None),
            height=40
        )

        self.add_widget(info)

        # Scroll area
        scroll_view = ScrollView(
            size_hint=(1, 1)
        )

        # History container
        history_layout = GridLayout(
            cols=1,
            spacing=10,
            padding=10,
            size_hint_y=None
        )

        history_layout.bind(
            minimum_height=history_layout.setter(
                "height"
            )
        )

        # Temporary empty-history message
        empty_label = Label(
            text=(
                "No analysis history available yet.\n\n"
                "Your breed and nutrition analyses "
                "will appear here."
            ),
            font_size="16sp",
            halign="center",
            size_hint_y=None,
            height=120
        )

        history_layout.add_widget(
            empty_label
        )

        scroll_view.add_widget(
            history_layout
        )

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