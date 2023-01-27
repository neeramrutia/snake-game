from turtle import Turtle
import random
color=["red","cyan","white","yellow","green"]
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 
        self.color(random.choice(color))
        self.speed("fastest")
        self.refresh()  
    def refresh(self):
        x=random.randint(-275,275)
        y=random.randint(-275,275)
        self.color(random.choice(color))
        self.goto(x,y)
