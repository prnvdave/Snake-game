from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


    def game_over(self):
        self.home()
        self.clear()
        self.color("RED")
        self.write(f"Game Over!  your score is {self.score}",align="center", font={("Times new roman", 30, )})