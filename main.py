import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.title("Turtle crossing the road")

    player = Player()
    car_manager = CarManager()
    scoreboard = Scoreboard()

    # Listen for key presses to move paddles
    screen.listen()
    screen.onkeypress(player.go_up, "Up")
    screen.onkeypress(player.go_down, "Down")

    game_over = False
    while not game_over:
        time.sleep(0.1)
        screen.update()

        car_manager.create_car()
        car_manager.move_cars()

        # Detect collision with car
        for car in car_manager.all_cars:
            if car.distance(player) < 20:
                game_over = True
                scoreboard.game_is_over()
        
        # Detect succesful crossing
        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()
    
    screen.exitonclick()

if __name__ == "__main__":
    main() # Start the game