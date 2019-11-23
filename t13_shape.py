######################################################################
# Author: Thy H. Nguyen     
# Username: nguyent2           
#
# Assignment: T13: Intro to Classes
#
#
# Purpose: A class for creating rectangles. Collaborates with the Points class
######################################################################
# Acknowledgements:
#
# Much of the code is originally from: http://openbookproject.net/thinkcs/python/english3e/

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle

class Shape:
    """
    A class to manufacture Shape objects.
    """

    def __init__(self, start_point, num_sides, side_length):
        """
         Initialize the shape at the start_point, with ns number of sides, sl length of each side

        :param start_point: a Point object representing the start point of the shape
        :param num_sides: the number of sides of the shape
        :param side_length: the length of each side of the shape
        """
        self.start_point = start_point          # A Point object to hold the start_point
        self.num_sides = num_sides
        self.side_length = side_length

    def draw_shape(self, r=0, g=0, b=0):  # black is the default color
        """
        Instantiates a Turtle object and draws the Shape on the Screen
        Notice the turtle is implemented differently here than in the Point class,
        as a demonstration of the many ways in which we can implement the same thing.

        :param r: the red channel
        :param g: the green channel
        :param b: the blue channel
        :return: None
        """
        turtles= turtle.Turtle()
        turtles.speed(0) # Makes the turtle speed up
        turtles.color(r, g, b)
        turtles.showturtle()
        turtles.penup()
        turtles.pendown()

        # draws the Shape to the screen

        for i in range(self.num_sides):
            turtles.forward(self.side_length)
            turtles.left(360/(self.num_sides))
        turtles.hideturtle()
# end class
