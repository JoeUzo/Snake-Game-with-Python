from turtle import Turtle

MOVE_DISTANCE = 20
LIMITS = (300, -300)
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.segments = []
        self.n = 2
        self.odd_even = 1
        self.x = 30
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")

    def create_snake(self):
        for n_ in range(self.n):
            new_turtle = Turtle(shape="square")
            new_turtle.color("green")
            new_turtle.penup()
            new_turtle.setx(self.x)
            self.x -= 20
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def out_of_bound(self):
        if self.head.xcor() >= LIMITS[0] or self.head.ycor() >= LIMITS[0]:
            return True
        if self.head.xcor() <= LIMITS[1] or self.head.ycor() <= LIMITS[1]:
            return True

    def grow(self):
        new_turtle = Turtle(shape="square")
        if (self.odd_even % 2) == 0:
            new_turtle.color("green")
        else:
            new_turtle.color("yellow")
        new_turtle.penup()
        xy = self.segments[-1].pos()
        new_turtle.goto(xy)
        self.segments.append(new_turtle)
        self.odd_even += 1

    def tail_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 5:
                return True

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(10000, 10000)
        self.segments.clear()
        self.n = 2
        self.x = 30
        self.odd_even = 1
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")
