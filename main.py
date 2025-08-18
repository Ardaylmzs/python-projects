from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from poison import Poison
import time


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
position_snake = [(0 ,0),(-20 , 0) , ( -40 , 0)]

new_segment = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()
poison = Poison()
result = snake.remove()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.color , "space")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    elif snake.head.distance(poison) < 15:
        if result =="game over" and len(snake.segments) == 3:
            scoreboard.game_over()
            game_is_on = False
            break
        poison.refreshs()
        snake.remove()
        scoreboard.decrease_scoreboard()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.mainloop()