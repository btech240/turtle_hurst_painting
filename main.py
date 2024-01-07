import random
import turtle as t
from turtle import Screen

# import colorgram

# # Extract Colors from image using colorgram library, then saved and added to color_list
# colors = colorgram.extract('./image.jpg', 8)

# # Create list of colors
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

color_list = [(215, 158, 75), (189, 176, 33), (235, 70, 31), (181, 45, 67), (217, 227, 220), (156, 31, 44),
              (68, 35, 56), (121, 164, 196), (232, 209, 104), (193, 71, 40), (215, 63, 110), (56, 49, 107), (218, 129, 164)]

# Create Screen
screen = Screen()
# Set color mode
t.colormode(255)
# Create turtle object
tim = t.Turtle()
# Set shape
tim.shape("circle")

# Set title for window
t.title("Hurst Dot Art")

# Move pen to bottom left
tim.speed(0)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.pendown()
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)

    # If we have placed 10 dots, direct turtle to move up and then reset to starting position of row
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


# KEEP AT BOTTOM OF CODE - exits the app on click
screen.exitonclick()
