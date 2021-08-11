import turtle as t

window = t.Screen()

tarta = t.Turtle()

#retangulo

# drawing first side
tarta.forward(100)  # Forward turtle by l units
tarta.left(90)  # Turn turtle by 90 degree

# drawing second side
tarta.forward(120)  # Forward turtle by w units
tarta.left(90)  # Turn turtle by 90 degree

# drawing third side
tarta.forward(100)  # Forward turtle by l units
tarta.left(90)  # Turn turtle by 90 degree

# drawing fourth side
tarta.forward(120)  # Forward turtle by w units
tarta.left(90)  # Turn turtle by 90 degree

window.exitonclick()