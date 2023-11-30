'''
Напишіть програму, де клас «геометричні фігури» (Figure) містить властивість color
з початковим значенням white і метод для зміни кольору фігури,
а його підкласи «овал» (Oval) і «квадрат» (Square) містять методи __init__ для
завдання початкових розмірів об'єктів при їх створенні.
'''

class Figure:
    def __init__(self):
        self._color = 'White'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color

class Oval(Figure):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side



