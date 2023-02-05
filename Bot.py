# class for bot playing
import random

class Bot:
    def __init__(self, name):
        self.name = name
        self.lifes = 3
        self.options = {1 : "paper", 2 : "stone", 3 : "scissors"}
        self.shuffled_option = ""

    def shuffle(self):
        number = random.randint(1, 3)
        if number == 1:
            self.shuffled_option = self.options[1]
            return self.shuffled_option
        elif number == 2:
            self.shuffled_option = self.options[2]
            return self.shuffled_option
        else:
            self.shuffled_option = self.options[3]
            return self.shuffled_option
    
    def lose_life(self):
        self.lifes -= 1

    def get_lifes(self):
        self.lifes

    def get_currentopt(self):
        self.shuffled_option
    