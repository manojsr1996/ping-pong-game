from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.write(f'{self.l_score}:{self.r_score}', align='center', font=('courier', 30, 'normal'))

    def l_update_score(self):
        self.l_score += 1

