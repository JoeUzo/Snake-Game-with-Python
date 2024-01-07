from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

food = Food()
scoreboard = ScoreBoard()
game_is_on = True
snake_move = True


def esc():
    global game_is_on
    scoreboard.game_over()
    game_is_on = False


def space_bar():
    global snake_move
    if snake_move:
        return
    snake_move = True
    scoreboard.reset_score()
    snake.reset_snake()


def pause():
    global snake_move
    if game_is_on:
        if snake_move:
            snake_move = False
            scoreboard.pause()
        else:
            snake_move = True
            scoreboard.resume()


def reset_hi_scr():
    global game_is_on
    if snake_move:
        return
    player_choice = screen.textinput("Reset High Score ",
                                     f"Are you sure you want to reset high score: 'yes' or 'no' ").lower()
    if player_choice == "yes":
        scoreboard.reset_high_score()
    game_is_on = False


screen.onkeypress(esc, "Escape")
screen.onkeypress(space_bar, "space")
screen.onkey(pause, "p")
screen.onkey(reset_hi_scr, "r")


while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake_move:
        snake.move()
    if snake.head.distance(food) < 15:
        """to detect collision with food"""
        snake.grow()
        food.change_pos()
        scoreboard.write_score()
    if snake.out_of_bound() or snake.tail_collision():
        scoreboard.game_over()
        snake_move = False


screen.exitonclick()
