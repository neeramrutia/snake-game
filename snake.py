
from turtle import Turtle,Screen
screen=Screen()
pos=[(-30,0),(-10,0),(10,0)]
class Snake:
    
    allturtle=[]
    
    def __init__(self):
        self.createsnake()
        self.head=self.allturtle[0]
    def createsnake(self):
        for position in pos:
            self.addseg(position)
    def addseg(self,pos):
            timmy=Turtle(shape="square")
            timmy.color("white")
            timmy.penup()
            timmy.goto(pos)
            timmy.speed("slowest")
            self.allturtle.append(timmy)
            
    def extend(self):
        self.addseg(self.allturtle[-1].position())        

    def move(self):
            for i in range(len(self.allturtle)-1,0,-1):
                x=self.allturtle[i-1].xcor()
                y=self.allturtle[i-1].ycor()
                self.allturtle[i].goto(x,y)
            self.allturtle[0].forward(20)
    def up(self):
        self.allturtle[0].setheading(90)        
    def down(self):
        self.allturtle[0].setheading(270)        
    def left(self):
        self.allturtle[0].setheading(180)        
    def right(self):
        self.allturtle[0].setheading(0)   
    def reset(self):
        for i in self.allturtle:
            i.goto(1000,1000)
        self.allturtle.clear()
        self.createsnake()
        self.head=self.allturtle[0]         