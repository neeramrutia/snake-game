from turtle import Turtle
file=open("data.txt",mode="r+")
contents=file.read()
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sc=0
        self.highscore=int(contents)
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.write(arg=f"SCORE={self.sc}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
        
        
    def updatescore(self):
        self.sc+=1 
        self.clear()   
        self.write(arg=f"SCORE={self.sc}  High Score: {self.highscore}",align="center",font=("Arial",20,"normal"))

    def reset(self):
        if self.sc>self.highscore:
            self.highscore=self.sc
            file.seek(0)
            file.truncate()
            file.write(f"{self.sc}")
        self.sc=0
        self.updatescore()
    def endgame(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER",align="center",font=("Arial",20,"normal"))