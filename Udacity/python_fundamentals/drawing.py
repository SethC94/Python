#import libraries
import turtle

def draw_square(some_image):
    for i in range(0,4):
        some_image.forward(135)
        some_image.left(90)
def draw_art():
    window = turtle.Screen()
    window.bgcolor("grey")
    seth = turtle.Turtle()
    seth.shape("circle")
    seth.color("purple")
    seth.speed(20)
    for i in range(0,35):
        draw_square(seth)
        seth.right(10)

    window.exitonclick()
draw_art()
