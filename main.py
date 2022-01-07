from kivy.app import App
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
from game import MazeGame
from square import Square

window_width = 1280
window_height = 720


class CanvasScreen(Screen):
    def __init__(self, name):
        super().__init__()
        self.game = MazeGame()
        self.game.draw()

    # def start_game(self):
    #     try:
    #         # if not self.manager.playing[0]:
    #         #     self.manager.models[0] = None
    #         # if not self.manager.playing[1]:
    #         #     self.manager.models[1] = None
    #
    #     except:
    #         self.manager.models = [None, None]

        self.add_widget(self.game)
        self.game.start()


class MazeApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(CanvasScreen(name='canvas'))

        Config.set('graphics', 'width', window_width)
        Config.set('graphics', 'height', window_height)
        Config.set('graphics', 'resizable', False)
        Config.write()
        Window.size = (window_width, window_height)

        return sm


if __name__ == '__main__':
    MazeApp().run()
