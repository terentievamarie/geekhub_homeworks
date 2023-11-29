"""
1. Напишіть програму, де клас «геометричні фігури» 
(Figure) містить властивість color з 
початковим значенням white і 
метод для зміни кольору фігури, а його підкласи «овал» 
(Oval) і «квадрат» (Square) містять методи __init__ для
завдання початкових розмірів об'єктів при їх створенні.
"""


class Figure:
    def __init__(self):
        self.color = 'white'

    def change_color(self, other_color):
        self.color = other_color

    def __str__(self):
        return f"The color of this figure: {self.color}"


class Oval(Figure):
    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width
    
    def __str__(self):
        return f"Figure: Oval, height : {self.height}, width: {self.width}"


class Square(Figure):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def __str__(self):
        return f"Figure : Square, side: {self.side}"


figure = Figure()
figure.change_color('black')
print(figure.color)
print(figure)

oval = Oval(13, 15)
print(oval.color)
print(oval)

square = Square(5)
square.change_color('green')
print(square.color)
print(square)
 