import random
import time
from turtle import Screen, Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


def go_up():
    jam.setheading(90)
    jam.forward(10)


def score_update():
    scoreboard.clear()
    scoreboard.write(f"Level {level}", False, "center", ("Arial", 10, "bold"))


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

screen.tracer(0)

jam = Turtle()
jam.shape("turtle")
jam.color("green")
jam.setheading(90)
jam.penup()
jam.goto(0, -270)

scoreboard = Turtle()
level = 1
scoreboard.hideturtle()
scoreboard.goto(-270, 250)
scoreboard.pencolor("white")
score_update()


screen.listen()
screen.onkey(go_up, "Up")

flag = True
car_list = []
speed_of_car = 5
while flag:
    time.sleep(0.1)
    screen.update()
    number = random.randint(1, 6)
    if number == 1:
        car = Turtle()
        car.shape("square")
        car.penup()
        car.color(random.choice(COLORS))
        new_y = random.randint(-190, 200)
        car.goto(405, new_y)
        car_list.append(car)
    for i in car_list:
        i.backward(speed_of_car)

    for car in car_list:
        if jam.distance(car) < 20:
            flag = False
            game_over = Turtle()
            game_over.hideturtle()
            game_over.pencolor("white")
            game_over.write("GAME OVER", False, "center", ("Arial", 10, "bold"))

    if jam.ycor() > 290:
        level += 1
        score_update()
        jam.goto(0, -270)

screen.exitonclick()
