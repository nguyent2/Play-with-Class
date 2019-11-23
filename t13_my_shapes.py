######################################################################
# Author: Thy H. Nguyen     
# Username: nguyent2             
#
# Assignment: T13: Intro to Classes
#
# Purpose:  Demonstrate the collaboration between classes, such as using a point to create a rectangle
######################################################################
# Acknowledgements:
#
# Original code created by Dr. Scott Heggen

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import t13_shape as shape       # notice the different ways we can import, and how that changes how we use it below
from t13_point import Point             # same as above...
import random
import turtle


def main():
    """
    Draws different shapes, size increased by a sequence, randomly colored using the turtle library.
    The code demonstrates interactions between classes, such as the use of a Point
    object to create a Shape object.

    :return: None
    """
    wn = turtle.Screen()
    wn.colormode(255)

        # a point object at an (x, y) coordinate

    for i in range(100):
        # a point object at an (x, y) coordinate
        p = Point(-75000, - 75000)

        # a shape object which starts at the point defined above
        shapes = shape.Shape(p, 5+i,50+i)

        # calls the draw_shape method of the Shape object
        shapes.draw_shape(random.randrange(255), random.randrange(255), random.randrange(255))

    # calls the draw_shape method of the Shape object

    wn.exitonclick()


if __name__ == "__main__":
    main()
