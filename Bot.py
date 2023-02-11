# class for bot playing
import random
from Player import *

#Class for Bot inherit from Player class
class Bot(Player):
    # overload method
    def select_option(self):
        return random.choice(["paper", "stone", "scissors"])    