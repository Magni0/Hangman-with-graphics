import turtle
import time


screen = turtle.Screen()
t = turtle.Turtle()


# this class is responsible for drawing the hangman
class HangManGraphic:

    """combines diffrent methods to draw a hangman"""

    def setup():

        """sets up for HangManGraphic.platform"""

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

        """draws a hanman platform"""

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

        """draws a circle for a head"""

        t.right(90)
        t.forward(8)
        t.circle(25)
        t.penup()
        t.left(90)
        t.forward(50)

    def chest():

        """draws a straight line at 270 degrees
        for 100px
        """

        t.pendown()
        t.forward(100)

    def l_arm():

        """draws a straight line at 225 degrees
        for a length of 70px
        """

        t.back(80)
        t.left(45)
        t.forward(70)
        t.back(70)
        t.right(45)

    def r_arm():

        """draws a straight line at 315 degrees
        for a length of 70px
        """

        t.right(45)
        t.forward(70)
        t.back(70)
        t.left(45)
        t.forward(80)

    def l_leg():

        """draws a straight line at 240 degrees
        for a length of 90px
        """

        t.left(30)
        t.forward(90)
        t.back(90)
        t.right(30)

    def r_leg():

        """draws a straight line at 300 degrees
        for a length of 90px
        """

        t.right(30)
        t.forward(90)
        t.back(90)
        t.right(60)

        t.penup()
        t.forward(200)
        t.write('YOU LOSE :(')
        print('you lose :(')

    def refresh_screen():

        """delays for 3 seconds the resets turtle screen"""

        time.sleep(3)
        t.reset()
