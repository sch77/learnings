import turtle

def draw_square(my_turtle,cursor_color,cursor_shape,speed,distance):
    # window = turtle.Screen()
    # window.bgcolor("red")
    # puttu = turtle.Turtle()
    puttu = my_turtle
    puttu.shape(cursor_shape)
    puttu.color(cursor_color)
    puttu.speed(speed)
    puttu.forward(distance)


    for idx in range(0,3):
        puttu.right(90)
        puttu.forward(distance)


    window.exitonclick()


def draw_circle(my_turtle,cursor_color,cursor_shape,speed,circle_radius):
    puttu = my_turtle
    puttu.shape(cursor_shape)
    puttu.color(cursor_color)
    puttu.speed(speed)
    puttu.circle(circle_radius)
    # window.exitonclick()

window = turtle.Screen()
window.bgcolor("red")
my_turtle = turtle.Turtle()

draw_square(my_turtle,"yellow","circle",10,100)
draw_circle(my_turtle,"yellow","triangle",10,100)