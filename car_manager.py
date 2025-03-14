
import random
from turtle import Turtle

# Constants for car properties and speed settings
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []  
        self.car_speed = STARTING_MOVE_DISTANCE 
        
    def create_car(self):
        """Creates a new car with a random chance and adds it to the car list."""
        random_chance = random.randint(1, 6) # Controls the frequency of car creation
        if random_chance == 1: # Only create a car in 1 out of 6 iterations
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        """Moves all cars to the left based on their current speed."""
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """Increases car speed to make the game more challenging."""
        self.car_speed += MOVE_INCREMENT