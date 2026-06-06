from turtle import Turtle,Screen
import time
from snake import Snake
screen = Screen()
screen.tracer(0)
screen.setup(height = 600,width = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
screen.onkey(snake.move_left,"x")
screen.onkey(snake.move_right,"d")

screen.exitonclick()
