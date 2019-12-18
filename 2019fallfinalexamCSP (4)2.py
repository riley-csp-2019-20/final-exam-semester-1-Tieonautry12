#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Tieon Autry
#Date
#12/18/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle
tiger = trtl.Turtle()



#movement functions
#making the turtle move and trying to make it 0```clear from the screen
def tiger_up():
    tiger.setheading(90)
    tiger.forward(10)

def tiger_down():
    tiger.setheading(270)
    tiger.forward(10)

def tiger_left():
    tiger.setheading(180)
    tiger.forward(10)

def tiger_right():
    tiger.setheading(0)
    tiger.forward(10)

def tiger_clear():
    tiger.clear()
    
def tiger_smallershape():
    tiger.shapesize("3")
    
def tiger_largersize():
    tiger.shapesize("7")




#color/drawing functions
#Making the turtle color and shape and size
tiger.color("blue")
tiger.begin_fill()
if tiger.filling():
    tiger.pensize()
else:
     tiger.pensize()
tiger.penup()
tiger.pendown()
tiger.shapesize()
tiger.shape("square")



#create screen
wn = trtl.Screen()

#bind to keypresses
#Making the turtle move with the arrow keys
wn.onkeypress(tiger_up, "Up")
wn.onkeypress(tiger_down, "Down")
wn.onkeypress(tiger_left, "Left")
wn.onkeypress(tiger_right, "Right")
wn.onkeypress(tiger_clear, "space")
wn.onkeypress(tiger_smallershape, "o")
wn.onkeypress(tiger_largersize, "p")
#listen
wn.listen()

#mainloop
wn.mainloop()