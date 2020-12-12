
import colorgram  # import colorgram to extract color from images
import turtle
import random

# Below part is used to extract colors from any image using colorgram

# colors = colorgram.extract('hirst.jpg', 30)    # extracting 6 colors from the given image
# colorsRGB = []

# for color in colors:
#     colorsRGB.append((color.rgb.r,color.rgb.g,color.rgb.b))  # make a tuple extracting RGB values from colors extracted
# print(colorsRGB)


# These colors were generated from colorgram and removed the whites from the list
screen = turtle.Screen()

myColorList = [(236, 212, 109), (25, 108, 188), (229, 143, 78), (119, 91, 54), (219, 57, 85), (240, 119, 151), (144, 167, 184), (111, 100, 195), (73, 124, 109), (188, 49, 91), (212, 9, 28), (140, 179, 8), (35, 187, 106), (235, 46, 35), (108, 175, 136), (30, 54, 121), (193, 177, 231), (136, 221, 
152), (8, 173, 186), (121, 210, 241), (86, 31, 35), (35, 41, 83), (237, 161, 179), (176, 28, 26), (80, 34, 32), (240, 168, 158)]

screen.colormode(255)  # set color mode to 255
screen.title("Hirst's Dot Painting")

# paint 10*10 rows of dots of different color. Each dot should be 20 in size and spaced apart by 50.
tim = turtle.Turtle()

tim.speed('fast')
tim.hideturtle()
tim.penup()
tim.backward(240)
tim.right(90)   # we can also use setheading for these computations
tim.forward(240)
tim.setheading(0)

def draw(): # this function will draw 10 dots in one line
    for _ in range(10):
        color = random.choice(myColorList)  # get random color
        tim.dot(20, color)
        tim.forward(50)

for _ in range(10):  # this loop sets the pointer to starting of above line
    draw()
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    # tim.right(180)
    tim.setheading(0)
screen.exitonclick()