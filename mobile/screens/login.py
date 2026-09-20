from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class LoginScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 35
        self.spacing = 12

        # Top spacing
        self.add_widget(
            Widget(
                size_hint_y=0.12
            )
        )

        # Main title
        title = Label(
            text="WELCOME BACK",
            font_size="30sp",
            bold=True,
            size_hint=(1, None),
            height=50
        )
        self.add_widget(title)

        # Subtitle
        subtitle = Label(
            text="Login to AI Livestock Advisory System",
            font_size="15sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(subtitle)

        # Email label
        email_label = Label(
            text="EMAIL",
            font_size="14sp",
            bold=True,
            size_hint=(1, None),
            height=30
        )
        self.add_widget(email_label)

        # Email input
        self.email_input = TextInput(
            hint_text="Enter your email",
            multiline=False,
            font_size="16sp",
            size_hint=(1, None),
            height=52
        )
        self.add_widget(self.email_input)

        # Password label
        password_label = Label(
            text="PASSWORD",
            font_size="14sp",
            bold=True,
            size_hint=(1, None),
            height=30
        )
        self.add_widget(password_label)

        # Password input
        self.password_input = TextInput(
            hint_text="Enter your password",
            password=True,
            multiline=False,
            font_size="16sp",
            size_hint=(1, None),
            height=52
        )
        self.add_widget(self.password_input)

        # Show / Hide password
        self.show_password_button = Button(
            text="SHOW PASSWORD",
            font_size="13sp",
            size_hint=(1, None),
            height=40
        )

        self.show_password_button.bind(
            on_press=self.toggle_password
        )

        self.add_widget(
            self.show_password_button
        )

        # Login button
        login_button = Button(
            text="LOGIN",
            font_size="18sp",
            bold=True,
            size_hint=(1, None),
            height=58
        )

        login_button.bind(
            on_press=self.open_dashboard
        )

        self.add_widget(login_button)

        # Status message
        self.status_label = Label(
            text="",
            font_size="14sp",
            size_hint=(1, None),
            height=35
        )

        self.add_widget(
            self.status_label
        )

        # Register button
        register_button = Button(
            text="DON'T HAVE AN ACCOUNT? REGISTER",
            font_size="14sp",
            size_hint=(1, None),
            height=45
        )

        register_button.bind(
            on_press=self.open_register
        )

        self.add_widget(
            register_button
        )

        # Back to home
        home_button = Button(
            text="BACK TO HOME",
            font_size="14sp",
            size_hint=(1, None),
            height=45
        )

        home_button.bind(
            on_press=self.open_home
        )

        self.add_widget(
            home_button
        )

        # Bottom spacing
        self.add_widget(
            Widget(
                size_hint_y=0.08
            )
        )

    def toggle_password(self, instance):

        if self.password_input.password:
            self.password_input.password = False
            self.show_password_button.text = (
                "HIDE PASSWORD"
            )
        else:
            self.password_input.password = True
            self.show_password_button.text = (
                "SHOW PASSWORD"
            )

    def open_dashboard(self, instance):

        email = self.email_input.text
        password = self.password_input.text

        if not email or not password:
            self.status_label.text = (
                "Please enter email and password"
            )
            return

        self.status_label.text = (
            "Login successful"
        )

        screen_manager = self.parent.parent
        screen_manager.current = "dashboard"

    def open_register(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "register"

    def open_home(self, instance):

        screen_manager = self.parent.parent
        screen_manager.current = "home"