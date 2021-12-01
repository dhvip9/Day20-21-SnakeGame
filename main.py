from turtle import Screen
from Snake import Snakes
from food import Food
from score import Score
import time


screen = Screen()
screen.title("SnakeGame")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Score()
snake_food = Food()
snakes = Snakes()

screen.listen()
screen.onkey(snakes.right, "Right")
screen.onkey(snakes.left, "Left")
screen.onkey(snakes.up, "Up")
screen.onkey(snakes.down, "Down")

is_going = True
while is_going:
    screen.update()
    time.sleep(0.1)
    snake_position = snakes.move()

    # For contacting Tail
    for segment in snakes.tail:
        if snakes.head.distance(segment) < 10:
            scoreboard.reset()
            snakes.reset()

    if snake_food.is_food_eat(snakes.head):
        snakes.extend()
        scoreboard.increase_score()

    if not snakes.snake_boundary(snake_position):
        scoreboard.reset()
        snakes.reset()

    snakes.tail = snakes.snake_segment[2:]

scoreboard.game_over()

screen.exitonclick()
