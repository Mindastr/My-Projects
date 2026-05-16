import math
import turtle


def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def draw_star(t, size, outline="black", fill="yellow"):
    t.color(outline, fill)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()


def draw_star_at(t, x, y, size, outline="gold", fill="gold"):
    move_to(t, x, y)
    t.setheading(90)
    draw_star(t, size, outline, fill)


def draw_circle(t, x, y, radius, color):
    move_to(t, x, y - radius)
    t.color(color, color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def prepare_screen(bgcolor="white", width=800, height=650):
    screen = turtle.Screen()
    screen.bgcolor(bgcolor)
    screen.setup(width=width, height=height)
    return screen


def draw_slide_5():
    """Slide 5: filling an area."""
    prepare_screen("white")
    leonardo = turtle.Turtle()
    leonardo.shape("turtle")
    leonardo.speed(5)

    move_to(leonardo, -80, 90)
    draw_star(leonardo, 170, "black", "black")
    leonardo.hideturtle()


def draw_slide_6():
    """Slide 6: filled star with user size."""
    screen = prepare_screen("white")
    leonardo = turtle.Turtle()
    leonardo.shape("turtle")
    leonardo.speed(5)
    leonardo.pensize(2)

    size = screen.numinput("Star size", "What is the size of star?", default=120, minval=20, maxval=250)
    if size is None:
        size = 120
    size = int(size)

    move_to(leonardo, -size // 2, size // 2)
    leonardo.setheading(0)
    leonardo.color("black", "yellow")

    angle = 120
    leonardo.begin_fill()
    for _ in range(5):
        leonardo.forward(size)
        leonardo.right(angle)
        leonardo.forward(size)
        leonardo.right(72 - angle)
    leonardo.end_fill()
    leonardo.hideturtle()


def draw_slide_7():
    """Slide 7: modified European Union flag."""
    prepare_screen("#001f5b", 800, 600)
    leonardo = turtle.Turtle()
    leonardo.shape("turtle")
    leonardo.speed(0)

    leonardo.pensize(1)
    size = 26
    radius = 95
    center_x = 0
    center_y = 0

    for i in range(12):
        angle = math.radians(90 - i * 30)
        x = center_x + math.cos(angle) * radius
        y = center_y + math.sin(angle) * radius
        draw_star_at(leonardo, x - size / 2, y + size / 2, size, "#d6a300", "#d6a300")

    leonardo.hideturtle()


def draw_slide_9():
    """Slide 9: Euler spiral Christmas tree with a few ornaments."""
    prepare_screen("snow", 750, 700)
    leonardo = turtle.Turtle()
    leonardo.shape("turtle")
    leonardo.speed(0)
    leonardo.pencolor("green4")
    leonardo.fillcolor("lawngreen")
    leonardo.pensize(3)

    move_to(leonardo, 0, -180)
    leonardo.left(17.4)

    leonardo.begin_fill()
    i = -1530
    second_start = None
    while i <= 1530:
        i += 2.5
        leonardo.forward(3)
        leonardo.right(abs(i) + 91.22)
        if i == 0:
            second_start = leonardo.position()
            leonardo.right(160)
    leonardo.end_fill()
    end_point = leonardo.position()

    ornaments = [
        (0, -180, "red"),
        (second_start[0], second_start[1], "gold"),
        (end_point[0], end_point[1], "dodgerblue")
    ]
    for x, y, color in ornaments:
        draw_circle(leonardo, x, y, 8, color)

    leonardo.hideturtle()


print("=== LAB WORK: TURTLE DRAWINGS ===")
print("1 - Slide 5: filling an area")
print("2 - Slide 6: filled star")
print("3 - Slide 7: modified European Union flag")
print("4 - Slide 9: Euler spiral Christmas tree")
print("=================================")

choice = input("Enter task number (1-4): ")

if choice == "1":
    draw_slide_5()
elif choice == "2":
    draw_slide_6()
elif choice == "3":
    draw_slide_7()
elif choice == "4":
    draw_slide_9()
else:
    print("Wrong choice. Restart the program and enter a number from 1 to 4.")

if choice in ["1", "2", "3", "4"]:
    turtle.mainloop()
