import turtle
turtle.bgcolor('white')
t= turtle.Turtle()
color=['red','dark red']
for number in range(450):
    t.forward(number+1)
    t.left(30)
    t.right(89)
    t.pencolor(color[number%2])
    turtle.done()