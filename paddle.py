from turtle import Screen, Turtle


class Paddle(Turtle):
    """A Paddle class that represents a paddle object in a Pong game."""

    def __init__(self, position, color):
        """Initializes the Paddle object with the given position, color, and screen."""
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.screen = Screen()

    def go_up(self):
        """Moves the paddle up by a fixed amount if it's not at the top of the screen."""
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down by a fixed amount if it's not at the bottom of the screen."""
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
