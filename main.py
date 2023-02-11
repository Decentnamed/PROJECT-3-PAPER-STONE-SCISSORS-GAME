from Player import *
from Bot import *
from Game import *
import random

player = Player("Dawid")
bot = Bot("Bot")
game = Game(player, bot)

if __name__ == "__main__":
    game.start()
