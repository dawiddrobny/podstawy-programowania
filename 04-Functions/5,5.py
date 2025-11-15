###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)

# Draw square at two locations
pen.penup()
pen.goto(-150, 100)
pen.pendown()
figures.draw_square(60, pen)
pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_square(60, pen)

# Draw triangle at two locations
pen.penup()
pen.goto(-150, -50)
pen.pendown()
figures.draw_triangle(80, pen)
pen.penup()
pen.goto(100, -50)
pen.pendown()
figures.draw_triangle(80, pen)

# Draw rectangle at two locations
pen.penup()
pen.goto(-150, -200)
pen.pendown()
figures.draw_rectangle(120, 60, pen)
pen.penup()
pen.goto(100, -200)
pen.pendown()
figures.draw_rectangle(120, 60, pen)


# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
