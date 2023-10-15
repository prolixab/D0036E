# Write a function called draw_rect that takes a Turtle object and a Rectangle and uses the Turtle to draw the Rectangle.
# See Chapter 4 for examples using Turtle objects.
# Write a function called draw_circle that takes a Turtle and a Circle and draws the Circle.
import turtle


class Rectangle:
    def __init__(self, x, y, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


def draw_rect(x, y, turtle, rectangle):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    turtle.fd(rectangle.height)
    turtle.rt(90)
    turtle.fd(rectangle.width)
    turtle.rt(90)
    turtle.fd(rectangle.height)
    turtle.rt(90)
    turtle.fd(rectangle.width)
    return


def draw_circle(x, y, turtle, circle):
    turtle.penup()
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()
    turtle.circle(circle.radius)
    return


bob = turtle.Turtle()
rect = Rectangle(50, 50, 50, 20)
circ = Circle(30)
draw_rect(15, 15, bob, rect)
draw_circle(70, 70, bob, circ)
turtle.mainloop()
