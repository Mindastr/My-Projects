import turtle
from datetime import datetime

screen = turtle.Screen()
screen.bgcolor("#111111")
screen.title("Analog Clock")
screen.setup(width=700, height=700)
screen.tracer(0)

face = turtle.Turtle()
face.hideturtle()
face.speed(0)
face.color("white")
face.pensize(3)

hour_hand = turtle.Turtle()
hour_hand.hideturtle()
hour_hand.speed(0)
hour_hand.pensize(8)
hour_hand.color("white")

minute_hand = turtle.Turtle()
minute_hand.hideturtle()
minute_hand.speed(0)
minute_hand.pensize(5)
minute_hand.color("#00ffcc")

second_hand = turtle.Turtle()
second_hand.hideturtle()
second_hand.speed(0)
second_hand.pensize(2)
second_hand.color("#ff5555")

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.speed(0)
text_turtle.color("white")


def draw_clock_face():
    face.clear()
    face.penup()
    face.goto(0, -180)
    face.pendown()
    face.circle(180)

    for i in range(12):
        face.penup()
        face.goto(0, 0)
        face.setheading(90 - i * 30)
        face.forward(150)
        face.pendown()
        face.forward(18)


def draw_hand(hand, length, angle):
    hand.clear()
    hand.penup()
    hand.goto(0, 0)
    hand.setheading(90 - angle)
    hand.pendown()
    hand.forward(length)


def draw_time_text(h, m, s):
    text_turtle.clear()
    text_turtle.penup()
    text_turtle.goto(0, -230)
    text_turtle.write(
        f"{h:02d}:{m:02d}:{s:02d}",
        align="center",
        font=("Arial", 20, "bold")
    )


def update_clock():
    now = datetime.now()

    h = now.hour
    m = now.minute
    s = now.second

    draw_clock_face()
    draw_hand(hour_hand, 80, (h % 12) * 30 + m * 0.5)
    draw_hand(minute_hand, 120, m * 6)
    draw_hand(second_hand, 150, s * 6)
    draw_time_text(h, m, s)

    screen.update()
    screen.ontimer(update_clock, 1000)


update_clock()
turtle.done()