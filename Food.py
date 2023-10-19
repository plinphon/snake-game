from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self,fruit):
        super().__init__()
        if fruit:
            self.shape(fruit)
        else:
            self.color('blue')
            self.shape('circle')
        self.pu()

    def food_pos(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def refresh(self, new_fruit=None):
       
        if new_fruit:
            self.shape(new_fruit)
        else:
            self.color('blue')
            self.shape('circle')

       
        self.food_pos()