from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

from screens.home import HomeScreen
from screens.login import LoginScreen


class LivestockApp(App):

    def build(self):

        # Create screen manager
        screen_manager = ScreenManager()

        # Create Home screen
        home_screen = Screen(name="home")
        home_screen.add_widget(HomeScreen())
        screen_manager.add_widget(home_screen)

        # Create Login screen
        login_screen = Screen(name="login")
        login_screen.add_widget(LoginScreen())
        screen_manager.add_widget(login_screen)

        return screen_manager


if __name__ == "__main__":
    LivestockApp().run()