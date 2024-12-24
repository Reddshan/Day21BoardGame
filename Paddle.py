from turtle import Turtle,Screen
class Paddle(Turtle):
    def __init__(self,xpos,y_pos):
        super().__init__()
        #scr=Screen()

        self.shape("square")
        self.color("white")

        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        #self.hideturtle()
        self.setpos(xpos,y_pos)
        #self.showturtle()
    def moveup(self):
        self.penup()
        new_y=self.ycor()+20
        #self.setheading(90)
        self.goto(self.xcor(),new_y)
    def movedown(self):
        self.penup()
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)

        #self.setheading(270)
        #self.forward(20)
