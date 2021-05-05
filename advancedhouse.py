import turtle
wn = turtle.Screen();
wn.bgcolor("cyan")

alex = turtle.Turtle();
alex.shape('turtle');
alex.shapesize(1);
alex.color('brown');
alex.speed(100);
alex.setpos(-100,-50);
alex.hideturtle()

alex.begin_fill(); # wall
alex.forward(200);
alex.left(90);
alex.forward(100);
alex.left(90);
alex.forward(200);
alex.left(90);
alex.forward(100);
alex.left(90);
alex.end_fill();
alex.penup();

alex.pd;
alex.begin_fill(); # roof
alex.color('green');
alex.setpos(-150, 50)
alex.goto(0,100)
alex.goto(150,50)
alex.goto(-150, 50)
alex.end_fill()

alex.begin_fill(); # L window
alex.color('white')
alex.setpos(-80, 0)
alex.goto(-40, 0)
alex.goto(-40, 20)
alex.goto(-80, 20)
alex.goto(-80, 0)
alex.end_fill()

alex.begin_fill()  # M window
alex.color('white')
alex.setpos(-20, 0)
alex.goto(20, 0)
alex.goto(20, 20)
alex.goto(-20, 20)
alex.goto(-20, 0)
alex.end_fill()

alex.begin_fill() # R window
alex.color('white')
alex.setpos(80, 0)
alex.goto(40, 0)
alex.goto(40, 20)
alex.goto(80, 20)
alex.goto(80, 0)
alex.end_fill()

alex.setpos(-100, 40)  # shelter
alex.begin_fill()
alex.color('brown')
alex.goto(-140, 32)
alex.goto(-140, 30)
alex.goto(-100, 30)
alex.goto(-100, 40)
alex.end_fill()

alex.setpos(-135, 30)  # pillar
alex.setheading(0)
alex.begin_fill()
alex.color('brown')
for i in range(2):
    alex.forward(3)
    alex.right(90)
    alex.forward(60)
    alex.right(90)
alex.end_fill()

alex.setpos(-140, -30)  # veranda
alex.setheading(0)
alex.begin_fill()
alex.color('brown')
for i in range(2):
    alex.forward(50)
    alex.right(90)
    alex.forward(20)
    alex.right(90)
alex.end_fill()

alex.setpos(-150, -51) # Bushes
alex.left(45)
alex.begin_fill()
alex.color('lime')
for i in range(7):
    alex.forward(30)
    alex.right(90)
    alex.forward(30)
    alex.left(90)
alex.goto(-150, -51)
alex.end_fill()

alex.setpos(250,250) # Sun
alex.color('yellow')
alex.pd()
for i in range(300):
    alex.forward(i)
    alex.left(i)

input();
