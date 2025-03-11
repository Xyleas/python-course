#*
# Project Planning
#
# 1. Definition
#       A. Create a turtle that can move in four directions.
#       B. Have an end goal.
#       C. Have visual feedback when we reach the goal.
#
# 2. Design
#
#   Diagram
#       We are going to have a rectangular playspace, with orange land on the left and a strip of blue ocean on the right. The goal will be for the green baby turtle in the middle to make it's way to the ocean. Once we reach the ocean, it will pop up some text that says "You Win!"
#
#   Code Flow
# 
#   Start
#       Background color orange
#       Draw blue ocean
#       Move turtle to starting position
#       Move key pressed?
#           Yes
#               Move the turtle
#               Have we reached the goal?
#                   Yes
#                       Hide turtle
#                       Write "YOU WIN!"
#                       End
#           No
#               GoTo Move key pressed?
#
#   Pseudocode
#       START
#           Set the background color to ORANGE
#           Draw the ocean
#           Move the turtle to starting position
#           
#           Pressed MOVE key?
#               Move turtle in that direcion
#
#               Have we reached the goal?
#                   Hide the turtle and disable controls
#                   Write "YOU WIN!" on-screen
#                   END
#
# 3. Implimentation
#       vvvSEE CODE BELOWvvv
#
# 4. Evaluation
#
# 5. Improvement
#   TODO: TBD
#
# *#

from turtle import *

move_distance = 20
speed(0)

# Create the beach.
bgcolor("#D269E1") # Hex code for a sand-ish orange.

# Draw ocean.
penup()
goto(100, 200)
pendown()

color("blue")

begin_fill()
goto(300, 200)
goto(300, -200)
goto(100, -200)
goto(100, 200)
end_fill()

# Set turtle at starting position
penup()
goto(-200, 0)
shape("turtle")
color("green")

def move_right():
    setheading(0)
    forward(move_distance)
    check_goal()

def move_up():
    setheading(90)
    forward(move_distance)
    check_goal()

def move_left():
    setheading(180)
    forward(move_distance)
    check_goal()
def move_down():
    setheading(270)
    forward(move_distance)
    check_goal()

# Called when we move the turtle
def check_goal():
    if xcor() >= 100:
        hideturtle()
        color("white")
        write("YOU WIN!")
        # Disable turtle
        onkey(None, "Right")
        onkey(None, "Up")
        onkey(None, "Left")
        onkey(None, "Down")

# Key press events
onkey(move_right, "Right")
onkey(move_up, "Up")
onkey(move_left, "Left")
onkey(move_down, "Down")

# Listen for key presses.
listen()

done()

