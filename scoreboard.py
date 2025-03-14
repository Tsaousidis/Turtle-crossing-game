
from turtle import Turtle

# Font settings for the scoreboard text
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT) # Display initial level

    def update_scoreboard(self):
        """Clears the previous level display and updates the scoreboard."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increments the level and updates the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_is_over(self):
        """Displays the 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
