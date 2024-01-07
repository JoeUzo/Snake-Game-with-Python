from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.change_pos()

    def change_pos(self):
        x_cord = randint(-260, 260)
        y_cord = randint(-260, 260)
        self.goto(x_cord, y_cord)
