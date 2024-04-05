import turtle
turtle.Screen
turtle.speed(5)
turtle.begin_fill()
turtle.fillcolor("blue")
turtle.hideturtle()
i = 0 
while i < 360:
    turtle.forward(1)
    turtle.left(1)
    i += 1
turtle.end_fill()
turtle.mainloop