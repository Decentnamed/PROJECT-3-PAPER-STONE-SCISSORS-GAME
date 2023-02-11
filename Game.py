# Class for game
from Player import *
from Bot import *

# Class Game
class Game():
    def __init__(self, player = Player(name=""), bot = Bot(name="")):
        self.player = player
        self.bot = bot
        self.round = 0

    # start the game
    def start(self):
        print(" ---- GAME STARTS ----")
        print(" Game has 6 rounds, after that you can continue or stop.")
        print("===================================")
        game_rounds = 6
        while True:
            self.round += 1
            print(f"* Round {self.round}")
            option_player = self.player.select_option()
            option_bot = self.bot.select_option()
            self.check_round_winner(option_player, option_bot)
            game_rounds -= 1
            if game_rounds <= 0:
                if not self.game_continue():
                    break

    # check round winner                
    def check_round_winner(self, player_option, bot_option):
        if player_option == bot_option:
            print("TIE, no points were given out...\n")
        elif(player_option == 'paper' and bot_option == "stone") or (player_option == "stone" and bot_option == "scissors") or (player_option == "scissors" and bot_option == "paper"):
            self.player.add_score()
            print(f"{self.player.get_name()} wins the round!!!\n")
        else:
            self.bot.add_score()
            print(f"{self.bot.get_name()} wins the round!!!\n")

    # check game winner
    def check_game_winner(self, points_player, points_bot):
        if points_player == points_bot:
            print("WINNER: TIE, congratulations for both players!!!")
        elif points_player > points_bot:
            print(f"WINNER: {self.player.get_name()}, congratulations!!!")
        else:
            print(f"WINNER: {self.bot.get_name()}, congratulations!!!")

    # continue the game
    def game_continue(self):
        continue_game = input("Do You want to continue the game? [T/N]: ")
        if continue_game == "N":
            print("===================================")
            print(f"{self.player.get_name()} has {self.player.get_score()} points")
            print(f"{self.bot.get_name()} has {self.bot.get_score()} points")
            self.check_game_winner(self.player.get_score(), self.bot.get_score())
            print(" ---- GAME END -------")
            return False
        return True

