"""
A classic Pong game implementation using Python's Turtle graphics module.

Methods
-------
run()
Starts the game loop and handles game events.

"""
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
import winsound


class PongGame:
    """A class representing pong game."""

    def __init__(self):
        """
        Initializes the PongGame object by setting up the game screen,
        creating the paddle, ball, scoreboard, and separation line objects,
        and registering the event handlers.
        """

        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=800, height=600)
        self.screen.title("Pong")
        self.screen.tracer(0)

        self.r_paddle = Paddle((350, 0), "red")
        self.l_paddle = Paddle((-350, 0), "blue")
        self.ball = Ball()
        self.scoreboard = Scoreboard()

        self.screen.onkeypress(self.r_paddle.go_up, "Up")
        self.screen.onkeypress(self.r_paddle.go_down, "Down")
        self.screen.onkeypress(self.l_paddle.go_up, "w")
        self.screen.onkeypress(self.l_paddle.go_down, "s")
        self.screen.listen()

        self.separation_line = Turtle()
        self.separation_line.goto(0, 220)
        self.separation_line.color("white")
        self.separation_line.goto(0, -280)
        self.separation_line.hideturtle()

    def run(self):
        """
        Starts the Pong game loop and handles game events such as ball movement,
        paddle collision, and score tracking.
        """
        game_is_on = True
        while game_is_on:
            time.sleep(self.ball.move_speed)
            self.screen.update()
            self.ball.move()

            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                self.ball.bounce_y()
                winsound.Beep(200, 50)

            if (self.ball.distance(self.r_paddle) < 60 and self.ball.xcor() > 320) or \
                    (self.ball.distance(self.l_paddle) < 60 and self.ball.xcor() < -320):
                self.ball.bounce_x()
                winsound.Beep(200, 50)

            # Detect R paddle misses
            if self.ball.xcor() > 380:
                self.ball.reset_position()
                self.scoreboard.l_point()
                winsound.PlaySound('score.wav', winsound.SND_ASYNC)

            # Detect L paddle misses
            if self.ball.xcor() < -380:
                self.ball.reset_position()
                self.scoreboard.r_point()
                winsound.PlaySound('score.wav', winsound.SND_ASYNC)

        self.screen.exitonclick()


if __name__ == "__main__":
    pong = PongGame()
    pong.run()
