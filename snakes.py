import turtle
import time
import random
delay = 0.1

#score
score = 0
high_score = 0
#screen setup

win = turtle.Screen()
win.title("snake game")
win.bgcolor("white")
win.setup(width=600,height=600)
win.tracer(0)  #turns off screen updates

#snake head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.goto(0,0)
head.penup()
head.direction = "stop"
#snake food
food =turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []
#PEN
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:0  High Score:0",align="center",font=("Courier",24,"normal"))

#function

def go_up():
    if head.direction != "down":
        head.direction="up"
def go_down():
    if head.direction !="up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def fo_right():
    if head.direction !="left":
        head.direction = "right"



def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y -20)

    if  head.direction == "right":
        x = head.xcor()
        head.setx(x +20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

 #keyboard binding

win.listen()
win.onkeypress(go_up,"w")
win.onkeypress(go_down,"s")
win.onkeypress(go_left,"a")
win.onkeypress(fo_right,"d")



#main loop
while True:
    win.update()

    # check for collision with the bordar
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(0.5)
        head.goto(0,0)
        head.direction= "stop"


        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        #clear segments
        segments.clear()

        #update score
        score = 0
        pen.clear()
        pen.write("Score:{} High score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    #checking the collusion
    if head.distance(food) < 20:
        #move the food to random direction
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a new segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #shorten the delay
        delay -=0.001

        #increase the score
        score += 10
        if score>high_score:
            high_score = score
        pen.clear()
        pen.write("Score:{} High score:{}".format(score,high_score),align="center", font = ("Courier",24,"normal"))

    # move the end segment first in reverse order
    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #move segment 0 to where the head is
    if len(segments)> 0 :
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            #hide the segment
            for segment in segments:
                segment.goto(1000,1000)

             #clear the segment
            segments.clear()

            #update score
            score = 0
            pen.clear()
            pen.write("Score:{} High score:{}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)

win.mainloop()