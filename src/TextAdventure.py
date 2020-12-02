import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

Builder.load_file('Display.kv')
Builder.load_file('Game.kv')


class MenuScreen(Screen):
    pass


class GameScreen(Screen):
    pass


sm = ScreenManager(transition=FadeTransition())
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(GameScreen(name='game'))


class Main(App):
    def build(self):
        return sm


if __name__ == "__main__":
    Main().run()
