from bubble import Bubble
import time
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Bubble Sort")
xcors = [x * 100 + 50 for x in range(-3, 3)]
y = -100

places = {num+1: (xcors[num], -100) for num in range(6)}
print(places)



bubbles = [Bubble() for _ in range(6)]




bubble_repository = []





for i, bubble in enumerate(bubbles):
    bubble.goto(xcors[i], y)
    bubble.onclick(bubble.inflate)
    bubble.determineplace(places)

for bubble in bubbles:
    bubble_repository.append({"Bubble": bubble,
                              "Initial_coords": bubble.position(),
                              "Initial_place": bubble.place})

def getbubble(coordinates):
    for object in bubble_repository:
        if object["Bubble"].position() == coordinates:
            return object["Bubble"]


def swap(bubble1, bubble2):
    bubble1.forward()
    bubble2.backward()


def run():
    for place in places:
        bubble1 = getbubble(places[place])
        if not place == 6:
            bubble2 = getbubble(places[place + 1])
            if bubble1.len > bubble2.len:
                swap(bubble1, bubble2)

def order_is_final():
    for place in places:
        if place == 6:
            break
        if getbubble(places[place]).len > getbubble(places[place + 1]).len:
            return False
    return True

def play(x, y):
    while order_is_final() == False:
        run()

bg = Turtle()
bg.shape("circle")
bg.shapesize(stretch_len=3, stretch_wid=3)

button = Turtle()
button.shape("circle")
button.shapesize(stretch_len=2.5, stretch_wid=2.5)
button.color("red")

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.goto(-280, 200)
writer.write("1. Click on a blue bubble to inflate it. Inflate the bubbles \nto different sizes."
             " \n\n2. Click the red button to run the algorithm. \n"
             "Bubbles will be sorted from left (smallest) to right (largest). ", font=('Courier', 14, 'normal'))


button.onclick(play)









screen.mainloop()