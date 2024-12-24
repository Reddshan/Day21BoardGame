from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.penup()
        self.color("white")
        self.x_move=10
        self.y_move=-10
        self.movespeed=0.1
        #self.goto(0,0)

    def move_cr(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    def bounce_y(self):
        #ballang=self.heading()
        #print(ballang)
        self.y_move*=-1
        self.movespeed*=0.9
        #self.tiltangle(290)
        #self.setheading(ballang + 90)
        #self.move_cr()
    def bounce_x(self):
        self.x_move*=-1
        self.movespeed *= 0.9
    def reset_pos(self):
        self.goto(0,0)
        self.bounce_x()
        self.movespeed=0.1