import time
from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = Scoreboard()



screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect the collision with the food

    if snake.head.distance(food) <15:
        food.refresh()
        snake.expand()
        scoreBoard.increase_score()

    #colliiso wit wall
    if snake.head.xcor() > 280 or snake.head.ycor() >280 or snake.head.ycor() < - 280 or snake.head.xcor() < -280:
        is_game_on = False
        scoreBoard.game_over()

    #collision with tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreBoard.game_over()















screen.exitonclick()


