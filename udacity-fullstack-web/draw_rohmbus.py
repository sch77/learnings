import turtle

# Draws Rhombus shape
def draw_rohmbus(turtle):
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)

# Draws a pattern using the Rhombus
window = turtle.Screen()
window.bgcolor("red")
my_turtle = turtle.Turtle()
my_turtle.color("yellow")
my_turtle.shape("turtle")
my_turtle.speed(10)

for i in range(1,37):
    draw_rohmbus(my_turtle)
    my_turtle.right(100)
my_turtle.right(90)
my_turtle.forward(400)

window.exitonclick()



