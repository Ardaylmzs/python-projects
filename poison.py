from turtle import Turtle
import random
class Poison(Turtle):

    def __init__(self ):
        super().__init__()
        self.speed("fastest")
        self.refreshs()
        self.poison()

    def poison(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("red")
        self.refreshs()

    def refreshs(self):
        randoms_x = random.randint(-280, 280)
        randoms_y = random.randint(-280, 280)
        self.goto(randoms_x, randoms_y)