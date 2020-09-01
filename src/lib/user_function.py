class User():
    user = ["","",""]

    def __init__(self):
        self.user = [input("Player 1 enter your name: "),
                    input("Player 2 enter your name: "),
                    1]
    
    def set_user(self):
        return(self.user)