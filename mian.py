from Player import *
from Bot import *
from Game import *



player = Player("Dawid")
bot = Bot("Bot")
game = Game(player, bot)

game.start()
