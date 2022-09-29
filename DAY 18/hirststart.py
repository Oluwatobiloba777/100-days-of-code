
# This is the code to get the rgb color values from the hirst image
# import colorgram
#
# rgbColor = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     newColor = (r, g, b)
#     rgbColor.append(newColor)
#
# print(rgbColor)
import turtle as img
import random


img.colormode(255)
image = img.Turtle()
image.hideturtle()
image.penup()
image.speed("fastest")

newColorList = [
                (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
                (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
                (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
                (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
                (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)
                ]

image.setheading(225)
image.forward(300)
image.setheading(0)
for i in range(1,101):
    image.dot(20, random.choice(newColorList))
    image.forward(50)

    if i % 10 == 0:
        image.setheading(90)
        image.forward(50)
        image.setheading(180)
        image.forward(500)
        image.setheading(0)


screen = img.Screen()
screen.exitonclick()