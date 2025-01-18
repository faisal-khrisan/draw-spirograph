from turtle import Turtle, Screen
import random

def set_color():
    """This function creates and returns a random color."""
    R = random.random()
    G = random.random()
    B = random.random()
    return (R, G, B)


fas = Turtle()
screen = Screen()
fas.speed("fastest")
fas.pensize(2)
fas.hideturtle()

def draw_spirograph(gap_size):
    """Draws a spirograph with the specified gap size."""
    for _ in range(int(360 / gap_size)):
        fas.pencolor(set_color())  # Use random color
        fas.circle(100)
        fas.setheading(fas.heading() + gap_size)

# Call the function to draw
draw_spirograph(5)
screen.mainloop()
