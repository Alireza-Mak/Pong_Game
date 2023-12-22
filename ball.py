from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 0.1
        self.y = 0.1
        self.speed = 1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def wall_bound(self):
        self.y *= -1

    def paddle_bound(self):
        self.x *= -self.speed
        self.speed += 0.1

    def reset_game(self):
        self.goto(0, 0)
        self.speed = 1
        self.x *= -(0.1 / abs(self.x))
        self.y *= -(0.1 / abs(self.y))
