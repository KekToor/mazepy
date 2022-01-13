from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.graphics import *


class Square(Widget):
    x = NumericProperty(0)
    y = NumericProperty(0)
    width = NumericProperty(0)
    height = NumericProperty(0)

    def __init__(self, width, height, color, x, y, **kwargs):
        super(Square, self).__init__(**kwargs)
        self.x = x
        self.y = y
        self.color = get_color_from_hex(color)
        self.width = width
        self.height = height

    def draw(self):
        with self.canvas:
            Color(self.color[0], self.color[1], self.color[2])
            Rectangle(pos=(self.x, self.y), size=(self.width, self.height))

