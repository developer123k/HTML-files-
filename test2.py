import turtle
turtle.Screen()
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.hideturtle()
i = 0
while i < 5:
    turtle.forward(200)
    turtle.left(72)
    i = i + 1
turtle.end_fill()
turtle.mainloop()