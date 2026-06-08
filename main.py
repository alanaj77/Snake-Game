from turtle import Screen,Turtle
import time
import  random
from snake import Snake
from food  import Food
from score import Score

screen = Screen()
screen.tracer(0)
screen.setup(height = 600,width = 600)
SCREEN_SIZE = 289
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()

snake = Snake()
food = Food()
score_board = Score()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

x_cord = snake.head.xcor()
y_cord = snake.head.ycor()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect food collision
    if snake.head.distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        snake.create_segment()

        score_board.update_score()

    # detect wall collision
    if snake.head.xcor() > SCREEN_SIZE or snake.head.ycor() > SCREEN_SIZE or snake.head.xcor() < -SCREEN_SIZE or snake.head.ycor() < -SCREEN_SIZE:
        game_is_on = False
        score_board.game_over()

    #detect collision with snake tail
    for segment in snake.segments[1:]:
         if segment.distance(snake.head) < 10:
            game_is_on = False
            score_board.game_over()







screen.exitonclick()
