from calendar import c
from re import I
from turtle import Turtle, Screen
import math

timmy = Turtle()
print(timmy) 

def movePen(timmy, x, y):
    timmy.penup()
    timmy.setposition(x, y)
    timmy.pendown()

def movePenX(timmy, x):
  timmy.penup()
  timmy.setx(x) 
  timmy.pendown()

def movePenY(timmy, y):
  timmy.penup()
  timmy.sety(y)
  timmy.pendown()

def positionAlongCircle(x, y, radius, angle):
  radians = math.radians(angle)
  return [x + (radius*math.sin(radians)),
            y + (radius*math.cos(radians))]
#This function is use for to draw ears whiskers around the circle

def ring(col, rad):
    timmy.fillcolor(col)
    timmy.begin_fill()
    timmy.circle(rad)
    timmy.end_fill()

window = Screen()

def draw_cat():
    timmy.shape("turtle") 
    timmy.color("black")
    timmy.speed(3)
    timmy.pensize(10)
    movePenY(timmy, -150)
    timmy.circle(150)
    noseMouthOffset = -15
    movePenY(timmy, -20 + noseMouthOffset)
    timmy.circle(20)
    movePen(timmy, -100, -20 + noseMouthOffset)
    timmy.right(90)
    timmy.circle(50, 180)
    timmy.left(180)
    timmy.circle(50, 180)
    eyeSpacingX = 30
    eyePosY = 40
    eyeRadius = 30
    movePen(timmy, eyeSpacingX, eyePosY)
    timmy.right(180)
    timmy.circle(eyeRadius, -180)
    movePen(timmy, -eyeSpacingX, eyePosY)
    timmy.circle(eyeRadius, 180)
    movePen(timmy, -20, -60 + noseMouthOffset)
    timmy.circle(20, 180)
    earBeginAngle = 25
    earSize = 85
    earWidth = 22
    positionA =  (0, 0, 150, earBeginAngle)
    movePen(timmy, positionA[0], positionA[1])

    positionB = positionAlongCircle(0, 0, 150 + earSize, earBeginAngle + earWidth)
    timmy.setposition(positionB[0], positionB[1])

    positionC = positionAlongCircle(0, 0, 150, earBeginAngle + earWidth * 2)
    timmy.setposition(positionC[0], positionC[1])

# Left ear

    positionA = positionAlongCircle(0, 0, 150, -earBeginAngle)
    movePen(timmy, positionA[0], positionA[1])

    positionB = positionAlongCircle(0, 0, 150 + earSize, -earBeginAngle + -earWidth)
    timmy.setposition(positionB[0], positionB[1])

    positionC = positionAlongCircle(0, 0, 150, -earBeginAngle + -earWidth * 2)
    timmy.setposition(positionC[0], positionC[1])

    whiskerLength = 180
    movePen(timmy, 50, -15)
    timmy.setheading(0)
    timmy.forward(whiskerLength)

    movePen(timmy, 50, 0)
    timmy.left(5)
    timmy.forward(whiskerLength)

# Left whiskers

    movePen(timmy, -50, -15)
    timmy.setheading(180)
    timmy.forward(whiskerLength)

    movePen(timmy, -50, 0)
    timmy.left(-5)
    timmy.forward(whiskerLength)

    window.exitonclick()
#exitonclick() was created to end program.

def draw_panda():
    timmy.up()
    timmy.setpos(-35, 95)
    timmy.down
    ring('black', 15)
 
# Draw second ear
    timmy.up()
    timmy.setpos(35, 95)
    timmy.down()
    ring('black', 15)
 
##### Draw face #####
    timmy.up()
    timmy.setpos(0, 35)
    timmy.down()
    ring('white', 40)
 
##### Draw eyes black #####
 
# Draw first eye
    timmy.up()
    timmy.setpos(-18, 75)
    timmy.down
    ring('black', 8)
 
# Draw second eye
    timmy.up()
    timmy.setpos(18, 75)
    timmy.down()
    ring('black', 8)
 
##### Draw eyes white #####
 
# Draw first eye
    timmy.up()
    timmy.setpos(-18, 77)
    timmy.down()
    ring('white', 4)
 
# Draw second eye
    timmy.up()
    timmy.setpos(18, 77)
    timmy.down()
    ring('white', 4)
 
##### Draw nose #####
    timmy.up()
    timmy.setpos(0, 55)
    timmy.down
    ring('black', 5)
 
##### Draw mouth #####
    timmy.up()
    timmy.setpos(0, 55)
    timmy.down()
    timmy.right(90)
    timmy.circle(5, 180)
    timmy.up()
    timmy.setpos(0, 55)
    timmy.down()
    timmy.left(360)
    timmy.circle(5, -180)
    timmy.hideturtle()

def draw_dog():
    timmy.pencolor("tan1")
    timmy.color("tan1")
    timmy.pensize(3)
    timmy.penup()
    timmy.setheading(90)
    timmy.goto(30,-30)
    timmy.pendown()
    timmy.begin_fill()
    timmy.circle(45,180)
    timmy.right(90)
    timmy.goto(-45,-30)
    timmy.circle(35,190)
    timmy.setheading(0)
    timmy.forward(55)
    timmy.penup()
    timmy.setheading(0)
    timmy.pendown()
    timmy.circle(35,170)
    timmy.penup()
    timmy.end_fill()

#Create the tongue of the dog
    timmy.pencolor("DeepPink1")
    timmy.color("Pink")
    timmy.setheading(270)
    timmy.goto(-10,-90)
    timmy.right(60)
    timmy.pendown()
    timmy.begin_fill()
    timmy.forward(15)
    timmy.left(60)
    timmy.forward(10)
    timmy.circle(10,180)
    timmy.forward(10)
    timmy.left(60)
    timmy.forward(15)
    timmy.end_fill()

#line on the tongue
    timmy.pensize(1)
    timmy.pencolor("DeepPink")
    timmy.goto(-13,-90)
    timmy.setheading(270)
    timmy.forward(17)
    timmy.circle(4,180)
    timmy.penup()
    timmy.left(90)
    timmy.forward(8)
    timmy.goto(-13,-107)
    timmy.setheading(270)
    timmy.left(180)
    timmy.pendown()
    timmy.circle(4,-180)



#right ear
    timmy.penup()
    timmy.goto(42,-45)
    timmy.pencolor("black")
    timmy.color("sienna")
    timmy.setheading(0)
    timmy.pendown()
    timmy.begin_fill()
    timmy.forward(10)
    timmy.left(60)
    timmy.circle(35,145)
    timmy.end_fill()

#left ear
    timmy.penup()
    timmy.goto(-70,-45)
    timmy.pendown()
    timmy.setheading(180)
    timmy.begin_fill()
    timmy.forward(10)
    timmy.left(-240)
    timmy.circle(35,-145)
    timmy.end_fill()
    timmy.penup()


#eyes
    timmy.pencolor("black")
    timmy.color("black")
    timmy.goto(-5,-45)
    timmy.setheading(270)
    timmy.pendown()
    timmy.begin_fill()
    timmy.circle(10,180)
    timmy.forward(5)
    timmy.circle(10,180)
    timmy.forward(5)
    timmy.end_fill()
    timmy.penup()

    timmy.pencolor("black")
    timmy.color("black")
    timmy.goto(-45,-45)
    timmy.setheading(270)
    timmy.pendown()
    timmy.begin_fill()
    timmy.circle(10,180)
    timmy.forward(5)
    timmy.circle(10,180)
    timmy.forward(5)
    timmy.end_fill()
    timmy.penup()

# Inner white dots in the eye
    timmy.color("white")
    timmy.goto(-2,-44)
    timmy.begin_fill()
    timmy.circle(6)
    timmy.end_fill()

    timmy.color("white")
    timmy.goto(-40,-44)
    timmy.begin_fill()
    timmy.circle(6)
    timmy.end_fill()

#Nose of the dog
    timmy.color("black")
    timmy.goto(-25,-75)
    timmy.begin_fill()
    timmy.circle(10)
    timmy.end_fill()
    timmy.goto(-14,-73)
    timmy.color("white")
    timmy.begin_fill()
    timmy.circle(2)
    timmy.end_fill()
    timmy.goto(-20,-73)
    timmy.color("white")
    timmy.begin_fill()
    timmy.circle(2)
    timmy.end_fill()
    timmy.goto(-17,-77)
    timmy.color("white")
    timmy.begin_fill()
    timmy.circle(2)
    timmy.end_fill()
    timmy.hideturtle()
    timmy.done()


draw_thing = input("DO you want to draw a (c) cat, (p) panda, (d) dog: ")

if draw_thing == 'c':
    window.bgcolor("brown4") 
    draw_cat()
elif draw_thing == 'p':
    window.bgcolor("blue3") 
    draw_panda()
elif draw_thing == 'd':
    window.bgcolor("black") 
    draw_dog()
     




my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()