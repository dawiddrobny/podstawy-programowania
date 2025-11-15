import turtle


def draw_square(side_length, pen):
    for i in range(4):
        pen.forward(side_length)
        pen.right(90)


def draw_triangle(side_length, pen):
    for i in range(3):
        pen.forward(side_length)
        pen.right(120)


def draw_rectangle(width, height, pen):
    for i in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
