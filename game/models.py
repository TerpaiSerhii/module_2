import random

class BasePlayer:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def update_score(self, delta):
        self.score += delta

class Player(BasePlayer):
    pass

class Computer(BasePlayer):
    def __init__(self):
        super().__init__("Комп'ютер")
