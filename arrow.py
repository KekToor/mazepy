from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import *


class Arrow(Widget):
    arrow_w = NumericProperty(0)
    arrow_h = NumericProperty(0)
    x = NumericProperty(0)
    y = NumericProperty(0)

    def __init__(self, arrow_w, arrow_h, x, y, **kwargs):
        super(Arrow, self).__init__(**kwargs)
        self.arrowW = arrow_w
        self.arrowH = arrow_h
        self.posX = x
        self.posY = y

    def draw(self):
        with self.canvas:
            Image(source='./arrow.png', pos=(self.posX + (0.1 * self.arrowW), self.posY + (0.1 * self.arrowH)), size=(0.8*self.arrowW, 0.8*self.arrowH))



        