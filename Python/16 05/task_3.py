import turtle

def draw_complex_ornament(n):
    screen = turtle.Screen()
    screen.bgcolor("black")

    t = turtle.Turtle()
    t.speed(0)
    t.pensize(1)

    colors = ["red", "blue", "green", "purple", "orange", "cyan"]
    angle = 360 / n
    radius = 20

    for i in range(n):
        t.color(colors[i % len(colors)])
        t.penup()
        t.goto(0, -radius)
        t.pendown()
        t.circle(radius)

        t.penup()
        t.goto(0, 0)
        t.right(angle)
        t.forward(8)
        t.right(20)

        radius += 6

    t.hideturtle()
    turtle.done()

draw_complex_ornament(20)
