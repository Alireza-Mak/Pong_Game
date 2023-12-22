from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.starting_position = starting_position
        self.create_paddle()
        self.new_x = starting_position[0]
        self.new_y = starting_position[1]

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(self.starting_position)
        self.screen.update()

    def move_up(self):
        if self.ycor() < 230:
            self.new_y += 20
            self.goto((self.new_x, self.new_y))

    def move_down(self):
        if self.ycor() > -230:
            self.new_y -= 20
            self.goto((self.new_x, self.new_y))
