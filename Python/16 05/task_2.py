import turtle

def draw_square_spiral():
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("green")

    length = 20
    for _ in range(25):
        t.forward(length)
        t.right(90)
        length += 10

    t.hideturtle()


def draw_diagonal_zigzag():
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("purple")

    t.penup()
    t.goto(-200, 0)
    t.pendown()

    step = 40
    for i in range(12):
        if i % 2 == 0:
            t.goto(t.xcor() + step, t.ycor() + step)
        else:
            t.goto(t.xcor() + step, t.ycor() - step)

    t.hideturtle()


def draw_comb_pattern():
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("orange")

    t.penup()
    t.goto(-200, -100)
    t.pendown()

    for _ in range(10):
        t.goto(t.xcor(), t.ycor() + 40)
        t.goto(t.xcor() + 30, t.ycor())
        t.goto(t.xcor(), t.ycor() - 40)
        t.goto(t.xcor() + 30, t.ycor())

    t.hideturtle()


# choose one or comment/uncomment what you need
draw_square_spiral()
# draw_diagonal_zigzag()
# draw_comb_pattern()

turtle.done()