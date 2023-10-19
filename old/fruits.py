import random
from turtle import Turtle




class Fruits:
    food = Turtle()
    def __init__(self,filename):
        self.food.speed(0)
        if filename:
            self.food.shape(filename)
        else:
            self.food.shape("circle")
            self.food.color("red")
        self.food.penup()
        self.food.goto(0, random.randint(-280,280))
        self.fruit_pos = self.food.position()

    def re_position(self):
        self.food.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.fruit_pos = self.food.position()
