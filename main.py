from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


def pre_race_positioning():
    y_cord = -100
    for color in colors:
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_cord)
        all_turtles.append(new_turtle)
        y_cord += 50

pre_race_positioning()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# sam = Turtle(shape="turtle")
# # sam.shape("turtle")
# sam.color("chartreuse")
# sam.penup()
# sam.goto(x=-225, y=-50)
# # sam.pendown()
# sam.forward(50)

# bob = Turtle()

# sam.color("chartreuse")
# sam.color("red")

# for i in range(10):
#     active_turtle = random.choice([sam, bob])
#     active_turtle.forward(20)


screen.exitonclick()