from turtle import Turtle


class Scoreboard(Turtle):
    """
    The `Scoreboard` class represents the scoreboard in the Pong game.
    It displays the current score for both players and updates the score whenever a player scores a point.
    """

    def __init__(self):
        """Initializes the Scoreboard object."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the scoreboard and updates it with the current scores for both players."""
        self.clear()
        self.color("blue")
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.color("red")
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
        self.color("white")
        self.goto(0, 240)
        self.write("Score", align="center", font=("Courier", 20, "normal"))

    def l_point(self):
        """Increases the score for the left player by 1 and updates the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Increases the score for the right player by 1 and updates the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()
