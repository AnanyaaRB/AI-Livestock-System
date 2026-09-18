from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class RegisterScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"
        self.padding = 40
        self.spacing = 15

        # Top spacing
        self.add_widget(Widget())

        # Title
        title = Label(
            text="REGISTER",
            font_size="28sp",
            bold=True,
            size_hint=(1, None),
            height=60
        )
        self.add_widget(title)

        # Name
        name_label = Label(
            text="Name",
            font_size="16sp",
            size_hint=(1, None),
            height=35
        )
        self.add_widget(name_label)

        self.name_input = TextInput(
            hint_text="Enter your name",
            multiline=False,
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.name_input)

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
            hint_text="Create a password",
            password=True,
            multiline=False,
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.password_input)

        # Confirm Password
        confirm_label = Label(
            text="Confirm Password",
            font_size="16sp",
            size_hint=(1, None),
            height=35
        )
        self.add_widget(confirm_label)

        self.confirm_input = TextInput(
            hint_text="Confirm your password",
            password=True,
            multiline=False,
            size_hint=(1, None),
            height=50
        )
        self.add_widget(self.confirm_input)

        # Register button
        register_button = Button(
            text="REGISTER",
            font_size="18sp",
            size_hint=(1, None),
            height=55
        )

        register_button.bind(on_press=self.register_user)

        self.add_widget(register_button)

        # Login option
        login_label = Label(
            text="Already have an account? Login",
            font_size="14sp",
            size_hint=(1, None),
            height=40
        )
        self.add_widget(login_label)

        # Bottom spacing
        self.add_widget(Widget())

    def register_user(self, instance):

        # Temporary registration logic
        # Real registration will be handled by the backend later.

        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_input.text

        if not name or not email or not password or not confirm_password:
            print("Please fill in all fields")

        elif password != confirm_password:
            print("Passwords do not match")

        else:
            print("Registration successful")