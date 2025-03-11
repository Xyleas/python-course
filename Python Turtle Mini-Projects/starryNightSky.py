#*
# Project Planning
#
# 1. Definition
#       A. Create a star system on a black background.
#       B. Do so using randomness for the star size and position. 
#       C. Use a for loop to generate a large amount of stars.
#
# 2. Design
#
#   Diagram
#           Black background w/ a variety of stars.
#
#   Code Flow
#
#   Start
#   Set background color to black.
#   Has 100 stars been drawn?
#   Yes
#       End
#   No
#   Randomize star position.
#   Randomize star size.
#   Draw star.
#   Go to "Has 100 stars been drawn?"
#
#   Pseudocode
#
#   START
#   Set background color to BLACK
#   Repeat 100 times
#       Generate random star position.
#       Generate random star size.
#       Draw star.
#   END
#
# 3. Implimentation
#       vvvSEE CODE BELOWvvv
#
# 4. Evaluation
#
# 5. Improvement
#   TODO: Add a few colorful planets. Make the stars twinkle.
#
# *#

from turtle import *
from random import *


speed(0)
bgcolor("black") # Criteria A. Create a star system on a black background.
hideturtle()

width = window_width()
height = window_height()

# Draws a star at the given position. Criteria B. Do so using randomness for the star size and position. 
def draw_star(xpos, ypos):
    # Set a random size for the star.
    size = randrange(10,100)
    # Go to the desired position.
    penup()
    goto(xpos,ypos)
    pendown()
    # Draw the star.
    dot(size, "white")

for x in range(100): # Criteria C. Use a for loop to generate a large amount of stars.
    # Create a random X and Y position.
    xpos = randrange(round(-width/2),round(width/2)) # Round here, as randrange requires integers, not floats.
    ypos = randrange(round(-height/2),round(height/2))
    # Draw the star at the position.
    draw_star(xpos,ypos)

done()