import time
from turtle import Turtle,Screen
from Paddle import Paddle
from Ball import Ball
from scoreBoard import Scoreboard
CUSTOM_SHAPE=[(360,0),(380,0),(460,100),(480,100)]

scr=Screen()
scr.setup(width=800,height=600)
scr.bgcolor('black')
scr.title("Pong_Game")
scr.tracer(0)
#scr.register_shape("custom", CUSTOM_SHAPE)

pad1= Paddle(350,0)
pad2=Paddle(-350,0)
ball=Ball()
sor=Scoreboard()
#ball.move_cr()
#pad.shape("custom")
scr.listen()
scr.onkey(pad1.moveup,"Up")
scr.onkey(pad1.movedown,"Down")
scr.onkey(pad2.moveup,"w")
scr.onkey(pad2.movedown,"s")
game_is_on=True
factor=0.9
time.sleep(0.1)
while game_is_on:
    time.sleep(ball.movespeed)
    scr.update()
    ball.move_cr()
    ### detects collosion with wall

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()


    #### detect collision with paddle
    if ball.distance(pad1)<50 and  ball.xcor()>320 or ball.distance(pad2)<50 and ball.xcor()<-320:
        factor=factor*0.1
        ball.bounce_x()
    ### if right paddle misses
    if ball.xcor()>380:
        ball.reset_pos()
        sor.l_point()
        ### left paddle misses
    if ball.xcor()<-380:
        ball.reset_pos()
        sor.r_point()

# turlst=scr.turtles()
#
# for tur in turlst:
#     tur.shape("turtle")
#     tur.color('white')



scr.exitonclick()
