from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from screens.home import HomeScreen
from screens.login import LoginScreen
from screens.register import RegisterScreen
from screens.dashboard import DashboardScreen


class LivestockApp(App):

    def build(self):

        # Create screen manager
        screen_manager = ScreenManager()

        # Home screen
        home_screen = Screen(name="home")
        home_screen.add_widget(HomeScreen())
        screen_manager.add_widget(home_screen)

        # Login screen
        login_screen = Screen(name="login")
        login_screen.add_widget(LoginScreen())
        screen_manager.add_widget(login_screen)

        # Register screen
        register_screen = Screen(name="register")
        register_screen.add_widget(RegisterScreen())
        screen_manager.add_widget(register_screen)

        # Dashboard screen
        dashboard_screen = Screen(name="dashboard")
        dashboard_screen.add_widget(DashboardScreen())
        screen_manager.add_widget(dashboard_screen)

        return screen_manager


if __name__ == "__main__":
    LivestockApp().run()