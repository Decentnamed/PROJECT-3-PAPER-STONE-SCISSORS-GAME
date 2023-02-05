#Class for typing by player

class Player:
    def __init__(self, name):
        self.name = name
        self.lifes = 3
        self.selected_option = ""
    
    def select_option(self):
        option = int(input("Type option: "))
        typed = False
        while(typed):
            if option == "paper":
                typed = True
                return option
            elif option == "stone":
                typed = True
                return option
            elif option == "scissors":
                typed = True
                return option
            else:
                wrong = "wrong type, try again"
                typed = False
                return wrong
    
    def lose_life(self):
        self.lifes -= 1

    def get_lifes(self):
        self.lifes