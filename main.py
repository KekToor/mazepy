from kivy.config import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from game import MazeGame
from square import Square

window_width = 1280
window_height = 720


class CanvasScreen(Screen):
    def start_game(self):
        try:
            if not self.manager.playing[0]:
                self.manager.models[0] = None
            if not self.manager.playing[1]:
                self.manager.models[1] = None
            self.game = MazeGame(self.manager.models)
        except:
            self.manager.models = [None, None]
            self.game = MazeGame(self.manager.models)

        self.add_widget(self.game)
        self.game.draw()



class MazeApp(App):
    def build(self):
        sm = ScreenManager()
        canvas_screen = CanvasScreen(name='canvas')
        sm.add_widget(canvas_screen)
        canvas_screen.start_game()
        Config.set('graphics', 'width', window_width)
        Config.set('graphics', 'height', window_height)
        Config.set('graphics', 'resizable', False)
        Config.set('graphics', 'maxfps', '60')
        Config.write()
        Window.size = (window_width, window_height)

        return sm


if __name__ == '__main__':
    MazeApp().run()
