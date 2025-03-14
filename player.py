
from turtle import Turtle

# Constants for player movement and positioning
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        """Moves the player upwards by a fixed distance."""
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        """Moves the player downwards by a fixed distance."""
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        """Resets the player's position to the starting point."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Checks if the player has reached the finish line."""
        return self.ycor() > FINISH_LINE_Y 