from turtle import Screen
import time
import  random
from snake import Snake
from food  import Food
screen = Screen()
screen.tracer(0)
screen.setup(height = 600,width = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

snake = Snake()
food = Food()


screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        snake.create_segment()




screen.exitonclick()
