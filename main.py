from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("snake")


snake=Snake()
food=Food()
scoreboard=Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")



gameison=True

while gameison:
      screen.update()
      time.sleep(0.1)
      snake.move()
      if snake.head.distance(food)<15:
            food.refresh()
            snake.extend()
            scoreboard.updatescore()
      if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
            # gameison=False
            # scoreboard.endgame() 
            scoreboard.reset()
            snake.reset()
      for i in range(3,len(snake.allturtle)):
            if snake.head.distance(snake.allturtle[i])<10:
                  # gameison=False
                  # scoreboard.endgame()
                  scoreboard.reset()
                  snake.reset()

screen.exitonclick()
