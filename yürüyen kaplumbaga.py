import turtle
kalem=turtle.Turtle()
kalem.shape("turtle")
kalem.forward(100)
kalem.penup()
kalem.goto(0,100)
for i in range(10):
    kalem.dot()
    kalem.forward(25)
turtle.done()
