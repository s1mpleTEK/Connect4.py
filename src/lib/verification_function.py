class Verification:
    @classmethod
    def verification_table(cls,input, table):
        for i in range(5, -1, -1):
            if table[i][input-1] == " ":
                return True
        print("This raw is full")
        return (False)
    
    @classmethod
    def verification_game_end(cls, table, user):
        count = 0
        if user == 1:
            elem = "O"
        elif user == 2:
            elem = "X"
        for j in range (7):
            for i in range(5, -1, -1):
                if table[i][j] == elem:
                    count += 1
                    if count == 4:
                        return(1)
                else:
                    count = 0

        return(0)