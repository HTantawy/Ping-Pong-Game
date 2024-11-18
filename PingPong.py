

import turtle

wind = turtle.Screen() # initilizing screen
wind.title("Ping Pong Game By Hussein") # setting title 
wind.bgcolor("Black") # setting background color
wind.setup(width=800,height=600) # setting height and width of the screen
wind.tracer(0)# stops window from updating 

# first racket
racket1 = turtle.Turtle()
racket1.speed(0)
racket1.shape("square")
racket1.color("magenta")
racket1.shapesize(stretch_wid=5, stretch_len=1)
racket1.penup()
racket1.goto(-350, 0)

# second racket
racket2 = turtle.Turtle()
racket2.speed(0)
racket2.shape("square")
racket2.color("blue")
racket2.shapesize(stretch_wid=5, stretch_len=1)
racket2.penup()
racket2.goto(350, 0)

# the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 2.5
ball.dy = 2.5

# score
score1 = 0
score2 = 0

score = turtle.Turtle()
score.speed(0)
score.color("brown")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player 1 : 0 Player 2 : 0", align="center", font=("Courier",24,"bold"))



#functions for game
def racket1_up(): 
     y = racket1.ycor() # set the coordinate of y 
     y += 20 # set the y to increment along the axis by 20
     racket1.sety(y) # set the y of the first racket to the new racket

def racket1_down():
     y = racket1.ycor()
     y -= 20 # set the y to decrement along the axis by 20
     racket1.sety(y) 

def racket2_up():
     y = racket2.ycor()
     y += 20
     racket2.sety(y)

def racket2_down():
     y = racket2.ycor()
     y -= 20
     racket2.sety(y)               
# Keyboard bindings
wind.listen()
wind.onkeypress(racket1_up,"h") # when pressing h the function racket_1 is invoked 
wind.onkeypress(racket1_down,"u")    
wind.onkeypress(racket2_up,"w") 
wind.onkeypress(racket2_down,"s") 
 
# main game loop
while True:
     wind.update() # updates the game every round it runs

     #move the ball
     ball.setx(ball.xcor() + ball.dx) # ball starts at 0 and it position itself + 2.5 times along the x axis 
     ball.sety(ball.ycor() + ball.dy) # ball starts at 0 and it position itself + 2.5 times along the y axis 

            
     #border check
     if ball.ycor() >290:
          ball.sety(290)
          ball.dy *= -1 

     if ball.ycor() <-290:
          ball.sety(-290)
          ball.dy *= -1      

     if ball.xcor() > 390:
          ball.goto(0,0)
          ball.dx *= -1
          score1+= 1
          score.clear()
          score.write("Player 1 : {} Player 2 : {}" .format(score1,score2), align="center", font=("Courier",24,"bold"))     

     if ball.xcor() < -390:
          ball.goto(0,0)
          ball.dx *= -1  
          score2 += 1
          score.clear()
          score.write("Player 1 : {} Player 2 : {}" .format(score1,score2), align="center", font=("Courier",24,"bold"))    

    
    # collion of ball and racket
     if (ball.xcor() > 340 and ball.xcor() < 350 ) and (ball.ycor() < racket2.ycor() + 40 and ball.ycor() > racket2.ycor() -40 ):
        ball.setx(340)
        ball.dx *= -1
     
     if  (ball.xcor() <-340 and ball.xcor() > -350 ) and (ball.ycor() < racket1.ycor() + 40 and ball.ycor() > racket1.ycor() -40 ):
        ball.setx(-340)
        ball.dx *= -1
 
     

 