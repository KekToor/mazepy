from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty, ListProperty
from kivy.core.window import Window
from kivy.vector import Vector

squareArray = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1 ,0 ,1 ,1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,1 ,1 ,1],
    [2,0,0,0,1,0,0,0,0,1,1,0,1,1,1,1,0,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,1,1,1,1,1,0,0,0,1,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1],
]

window_width = 1280
window_height = 720
count_width = 20
count_height = 12


class MazeGame(Widget):
    default_width = NumericProperty(window_width / 20)
    default_height = NumericProperty(window_height / 12)

    def __init__(self):
        self.x = 0
        self.y = 0