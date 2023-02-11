# Class for game
from Player import *
from Bot import *

class Game():
    def __init__(self, player = Player(name=""), bot = Bot(name="")):
        self.player = player
        self.bot = bot
        self.rounds = 0

    def start(self):
        print(" ---- GAME STARTS ----")
        while True:
            self.rounds += 1
            print(f"Round {self.rounds}")
            option_player = self.player.select_option()
            option_bot = self.bot.select_option()
            self.check_winner(option_player, option_bot)
            if not self.game_continue():
                break


    def check_winner(self, player_option, bot_option):
        if player_option == bot_option:
            print("TIE, no points were given out...")
        elif(player_option == 'paper' and bot_option == "stone") or (player_option == "stone" and bot_option == "scissors") or (player_option == "scissors" and bot_option == "paper"):
            self.player.add_score()
            print(f"{self.player.get_name()} wins the round!!!")
        else:
            self.bot.add_score()
            print(f"{self.bot.get_name()} wins the round!!!")

    def game_continue(self):
        continue_game = input("Do You want to continue the game? [T/N]: ")
        if continue_game == "N":
            print("===================================")
            print(f"{self.player.get_name()} has {self.player.get_score()} points")
            print(f"{self.bot.get_name()} has {self.bot.get_score()} points")
            print(" ---- GAME END -------")
            return False
        return True

