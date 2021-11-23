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
    is_going = snakes.tail_is_contact()
    eat = snake_food.is_food_eat(snakes.head)
    if eat:
        snakes.extend()
        scoreboard.clear()
        scoreboard.increase_score()
    is_going = snakes.snake_boundary(snake_position)


scoreboard.game_over()

screen.exitonclick()
