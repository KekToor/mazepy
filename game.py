from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.vector import Vector
from kivy.animation import Animation

from square import Square
from arrow import Arrow

squareArray = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
    [2, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
]


class MazeGame(Widget):
    width = NumericProperty(1280)
    height = NumericProperty(720)
    count_width = NumericProperty(20)
    count_height = NumericProperty(12)
    fps = NumericProperty(60)


    def __init__(self, models, **kwargs):
        super(MazeGame, self).__init__(**kwargs)
        self.default_width = int(self.width / self.count_width)
        self.default_height = int(self.height / self.count_height)
        self.colors = ['#FFFFFF', '#000000', '#00FF00', '#FF0000']
        self.squares = []
        for i in range(0, self.count_width):
            for j in range(0, self.count_height):
                self.squares.append(Square(self.default_width, self.default_height, self.colors[squareArray[j][i]], i * self.default_width, self.height - ((j+1) * self.default_height)))
        for square in self.squares:
            self.add_widget(square)

        Clock.schedule_interval(self.draw(), 1 / self.fps)

    def draw(self):
        for square in self.squares:
            square.draw()
        val = 2

        for index, row in enumerate(squareArray):
            if val in row:
                arrow = Arrow(self.default_width, self.default_height, (row.index(val)) * self.default_width, self.height - ((index+1) * self.default_height))
                print(arrow.arrowW, arrow.arrowH, arrow.posX, arrow.posY)
                self.add_widget(arrow)
                arrow.draw()
                arrow.arrowW = arrow.arrowW + (2 * self.default_width)
                print(arrow.arrowW)
                arrow.draw()
                arrow.arrowW = arrow.arrowW + (2 * self.default_width)
                print(arrow.arrowW)
                arrow.draw()
                print(f'{index}, {row.index(val)}')

    def update(self, dt):




