from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivy.graphics import *


class Square(Widget):
    def __init__(self, width, height, color, x, y):
        self.x = x
        self.y = y
        self.color = get_color_from_hex(color)
        self.width = width
        self.height = height

    def draw(self):
        with self.canvas:
            Color(self.color)
            Rectangle(pos=(self.x, self.y), size=(self.width, self.height))

