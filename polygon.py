# Name polygon.
# Purpose: Draw a polygon using a turtle.
DEBUG=False
#
import turtle
myturtle = turtle.Turtle()


def polygon(t,sides, length, arc):
#  polygon function to draw an arc using the turtle module
#  t is the turtle window
#   sides is the number of sides on this polygon
#  length is the length of each side in pixels
    for x in range(arc):      # Loop
        t.fd(length)           # Draw a line, length is in pixels
        t.rt(360/sides)        # Turn to the right.
        if DEBUG:
           print(t.position())     # output the position to the main window

# Main loop

sides = 360     # There are 360 sides to this polygon
length = 1      # each side of the polygon is 1 pixel
arc=270         # Draw 270 sides which in this case will be 270 degrees.
                #
polygon(myturtle, sides, length, arc)
raw_input("Pres Enter to exit")

