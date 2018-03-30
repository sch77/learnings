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
    puttu.right(100)


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

count = 0

while count < 100:
    draw_square(my_turtle,"yellow","circle",10,100)
    count = count + 1

# draw_square(my_turtle,"yellow","circle",10,100)
# draw_square(my_turtle,"yellow","circle",10,100)


window.exitonclick()

#draw_circle(my_turtle,"yellow","triangle",10,100)
