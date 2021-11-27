from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed('slow')
        self.y_jump = 10
        self.x_jump = 10

    def move(self):
        new_x = self.xcor() + self.x_jump
        new_y = self.ycor() + self.y_jump
        self.goto(new_x, new_y)

    def y_move(self):
        self.y_jump *= -1
        self.move()

    def x_move(self):
        self.x_jump *= -1
        self.move()

    def opposite(self):
        self.goto(0, 0)
        self.x_jump *= -1
        self.move()



