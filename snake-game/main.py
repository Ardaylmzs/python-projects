from turtle import Screen ,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from poison import Poison
from tkinter import messagebox
import time




screen = Screen()
turtle = Turtle()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
position_snake = [(0 ,0),(-20 , 0) , ( -40 , 0)]

start_count = 0
new_segment = []
snake = Snake()
food = Food()
scoreboard = Scoreboard()
poison = Poison()
result = snake.remove()
game_is_on = False

messagebox.showinfo("key control",
                    "key instructor : game start ➡️ 's' ,"
                    "game pause ➡️ 'p' , game quit ➡️ 'q' , "
                    "change snake's color ➡️ 'space'")

def game_pause():
    global start_count,game_is_on
    game_is_on = False
    start_count = 0
def finish_game():
    global game_is_on
    game_is_on = False
    screen.bye()

def game_start():
    global game_is_on,start_count
    start_count += 1
    if start_count == 1:
        game_is_on = True
        food.refresh()
        poison.refreshs()
        scoreboard.goto(0 ,265)
        scoreboard.update_scoreboard()
        if len(snake.segments)  < 3:
            scoreboard.clear()
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
                    game_is_on = False
                    start_count = 0
                    scoreboard.game_over()
                    snake.reset()
                    break
                poison.refreshs()
                snake.remove()
                scoreboard.decrease_scoreboard()

            if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
                scoreboard.reset()
                snake.reset()
            for segment in snake.segments:
                if segment == snake.head:
                    pass
                elif snake.head.distance(segment) < 10:
                   scoreboard.reset()
                   snake.reset()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.color , "space")
screen.onkey(game_pause ,"p")
screen.onkey(game_start,"s")
screen.onkey(finish_game ,"q")

screen.mainloop()