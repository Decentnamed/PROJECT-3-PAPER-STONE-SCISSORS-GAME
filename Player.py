#Class for typing by player

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    # method for option select by Player
    def select_option(self):
        while True:
            option = input(f"{self.name}, Type option: paper, stone, scissors: ")
            if option == "paper":
                return option
            elif option == "stone":
                return option
            elif option == "scissors":
                return option
            else:
                print("wrong type, try again")

    def add_score(self):
        self.score += 1

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score
                
