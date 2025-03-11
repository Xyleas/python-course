#*
# Project Planning
#
# 1. Definition
#   A. Be able to detect inputs.
#   B. Require multiple inputs to pop the balloon.
#   C. Utilize variables, conditions, and functions.
#
# 2. Design
#
#   Code Flow
#   A. Start
#   B. Draw balloon
#   C. Up key pressed
#   D. Balloon at max size?
#   E1. Yes
#       F1. Clear balloon
#       G1. Write "POP!"
#       H1. End
#   E2. No
#       F2. Increase balloon size
#       G2. Draw balloon
#       H2. Go to B.
#
#   Pseudocode
#
#   Start
#   Draw the balloon
#   Has the key been pressed?
#       Has the balloon reached max size?
#           Clear the balloon
#           Write "POP!"
#       If not
#       Increase the balloon size
#       Draw the balloon
#   End
#
# 3. Implimentation
#       vvvSEE CODE BELOWvvv
#
# 4. Evaluation
#   Criteria 1. Detect inputs.
#   Criteria 2. Require multiple inputs to pop the balloon.
#   Criteria 3. Utilize variables, conditions, and functions.
#
# 5. Improvement
#   TODO: We can do things like change the color of the balloon after each Pop. We could make the interval that the sizes pop different each time, giving it some replayability.
#
# TODO: Let's get good about doing this within our code comments. 
# *#

from turtle import *

diameter = 40 # Criteria 3. Utiliza variables, conditions, and functions.
pop_diameter = 100

def draw_balloon():
    color("pink")
    dot(diameter)

def inflate_balloon():
    global diameter 
    diameter = diameter + 10
    draw_balloon()

    if diameter >= pop_diameter: # Criteria 2. Require multiple inputs to pop the balloon.
        clear()
        diameter = 40
        write("POP!")

draw_balloon()

onkey(inflate_balloon, "Up") # Criteria 1. Detect inputs.
listen()
done()