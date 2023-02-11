# class for bot playing
import random
from Player import *

class Bot(Player):
    def select_option(self):
        return random.choice(["paper", "stone", "scissors"])    