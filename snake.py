from turtle import Turtle
from score import Score
from Food import Food

positions = [(0, 0), (20, 0), (40, 0)]
BOTTOM = 270
UP = 90
LEFT = 180
RIGHT = 360

class Snake:
    def __init__(self):
        self.segments = []
        for pos in positions:
            new_turtle = Turtle()
            new_turtle.shape('square')
            new_turtle.color('white')
            new_turtle.pu()
            new_turtle.goto(pos)
            new_turtle.speed('normal')
            self.segments.append(new_turtle)
        self.head = self.segments[-1]
        self.is_dead = 0

    def move(self):
        for i in range(0,len(self.segments)-1):
            current = self.segments[i]
            next_one = self.segments[i+1]
            current.goto(next_one.pos())
        self.head.forward(20)


    def go_up(self):
        if self.head.heading() != BOTTOM:
            self.head.setheading(UP)

    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(BOTTOM)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def distance_food(self,food: Food,scores: Score):
        if self.head.distance(food.pos()) < 20:
            new_turtle = Turtle()
            new_turtle.shape('square')
           
            color = 'white'
            new_turtle.color(color)
            new_turtle.pu()
            new_turtle.goto(self.segments[0].pos())
            self.segments.insert(0,new_turtle)
            self.head = self.segments[-1]
            food.food_pos()
            scores.write_score(10)

    def distance_self(self,scores: Score):
        for segment in self.segments:
            if segment != self.head and self.head.pos() == segment.pos():
                self.is_dead = 1
                scores.write_score(-1)

    def distance_wall(self,scores: Score):
        if (self.head.xcor() > 290 or
        self.head.xcor() < -290 or
        self.head.ycor() > 290 or
        self.head.ycor() < -290):
            self.is_dead = 1
            scores.write_score(-1)

    def reset(self):

        for segment in self.segments:
            segment.goto(1000, 1000) 
        self.segments.clear()

       
        for pos in positions:
            new_turtle = Turtle()
            new_turtle.shape('square')
            new_turtle.color('white')
            new_turtle.pu()
            new_turtle.goto(pos)
            new_turtle.speed('normal')
            self.segments.append(new_turtle)
        self.head = self.segments[-1]

       
        self.is_dead = 0