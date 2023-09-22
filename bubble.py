from turtle import Turtle

class Bubble(Turtle):
    def __init__(self):
        super().__init__()
        self.len = 1
        self.wid = 1
        self.hideturtle()
        self.penup()
        self.shape('circle')
        self.pencolor("red")
        self.color("blue")
        self.showturtle()
        self.shapesize(stretch_wid=self.wid, stretch_len=self.len)
        self.place = 0

    def inflate(self, x, y):
        # 4 MAX
        self.wid *= 1.1
        self.len *= 1.1
        if self.wid < 4 and self.len < 4:
            self.shapesize(stretch_wid=self.wid, stretch_len=self.len)

    def determineplace(self, places):
        for place in places:
            if self.position() == places[place]:
                self.place = place

    def forward(self):
        self.goto(self.xcor() + 100, self.ycor())
        self.place += 1

    def backward(self):
        self.goto(self.xcor() - 100, self.ycor())
        self.place -= 1