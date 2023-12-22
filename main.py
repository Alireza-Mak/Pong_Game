from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen_width = 800
screen_height = 600
screen.setup(width=screen_width, height=screen_height)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

LEFT_PADDLE_POSITION = (-350, 0)
RIGHT_PADDLE_POSITION = (350, 0)
left_paddle = Paddle(LEFT_PADDLE_POSITION)
right_paddle = Paddle(RIGHT_PADDLE_POSITION)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_up, "W")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(left_paddle.move_down, "S")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")


end_game = False
while not end_game:
    screen.update()
    ball.move()
    if (right_paddle.distance(ball) < 50 and ball.xcor() > 330) or (left_paddle.distance(ball) < 50 and ball.xcor()
                                                                    < -330):
        ball.paddle_bound()
    elif ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            ball.reset_game()
            scoreboard.paddle_left_win()
        else:
            ball.reset_game()
            scoreboard.paddle_right_win()
        if scoreboard.check_game_status() == 10:
            end_game = True
    elif ball.ycor() > 285 or ball.ycor() < -280:
        ball.wall_bound()


screen.exitonclick()
