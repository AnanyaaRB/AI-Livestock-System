from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 40
        self.spacing = 15

        # Top spacing
        self.add_widget(Widget())

        # Title
        title = Label(
            text="LOGIN",
            font_size="28sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(title)

        # Email
        email_label = Label(
            text="Email",
            font_size="16sp",
            size_hint=(1, None),
            height=35
        )
        self.add_widget(email_label)

        self.email_input = TextInput(
            hint_text="Enter your email",
            multiline=False,
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.email_input)

        # Password
        password_label = Label(
            text="Password",
            font_size="16sp",
            size_hint=(1, None),
            height=35
        )
        self.add_widget(password_label)

        self.password_input = TextInput(
            hint_text="Enter your password",
            password=True,
            multiline=False,
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.password_input)

        # Login button
        login_button = Button(
            text="LOGIN",
            font_size="18sp",
            size_hint=(1, None),
            height=55
        )

        # Connect Login button to Dashboard
        login_button.bind(on_press=self.open_dashboard)

        self.add_widget(login_button)

        # Register option
        register_label = Label(
            text="Don't have an account? Register",
            font_size="14sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(register_label)

        # Bottom spacing
        self.add_widget(Widget())

    def open_dashboard(self, instance):

        # Get the ScreenManager
        screen_manager = self.parent.parent

        # Move to Dashboard
        screen_manager.current = "dashboard"