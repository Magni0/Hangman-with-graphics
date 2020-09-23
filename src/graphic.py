import turtle
import time

screen = turtle.Screen()
t = turtle.Turtle()

# this class is responsible for drawing the hangman
class HangManGraphic:
    def setup():
        # window settings
        t.hideturtle()
        t.color('white')
        turtle.bgcolor('black')

        # pen placement
        t.penup()
        t.right(180)
        t.forward(100)
        t.left(90)
        t.forward(250)

        HangManGraphic.platform()

    def platform():
        # left platform leg
        t.pendown()
        t.forward(100)
        t.right(180)
        t.forward(50)
        t.right(45)
        t.forward(70)

        # pen placement (for right platform leg)
        t.penup()
        t.right(45)
        t.forward(400)

        # right platform leg
        t.pendown()
        t.right(90)
        t.forward(100)
        t.right(180)
        t.forward(50)
        t.left(45)
        t.forward(70)

        # platform top
        t.right(135)
        t.forward(50)
        t.back(450)
        t.forward(350)
        t.left(90)
        t.forward(500)
        t.back(50)
        t.left(45)
        t.forward(70)
        t.left(45)
        t.back(50)
        t.forward(250)

        # rope
        t.left(90)
        t.forward(100)

    def head():
        t.right(90)
        t.forward(8)
        t.circle(25)
        t.penup()
        t.left(90)
        t.forward(50)

    def chest():
        t.pendown()
        t.forward(100)

    def l_arm():
        t.back(80)
        t.left(45)
        t.forward(70)
        t.back(70)
        t.right(45)

    def r_arm():
        t.right(45)
        t.forward(70)
        t.back(70)
        t.left(45)
        t.forward(80)

    def l_leg():
        t.left(30)
        t.forward(90)
        t.back(90)
        t.right(30)
        
    def r_leg():
        t.right(30)
        t.forward(90)
        t.back(90)
        t.right(60)

        t.penup()
        t.forward(200)
        t.write('YOU LOSE :(')
        print('you lose :(')

    def refresh_screen():
        time.sleep(3)
        t.reset()