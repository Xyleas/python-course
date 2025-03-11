from turtle import *

# Set the stage.
bgcolor("black")

# Make the orange planet.
begin_fill()
color("orange")
circle(60)
end_fill()

# Move forward.
penup()
forward(100)
pendown()

# Make the grey planet.
color("grey")
begin_fill()
circle(20)
end_fill()

# Move forward.
penup()
forward(80)
pendown()

# Make the red planet.
color("red")
begin_fill()
circle(20)
end_fill()

# Move forward.
penup()
forward(90)
pendown()

# Make the green planet.
color("green")
begin_fill()
circle(30)
end_fill()

done()