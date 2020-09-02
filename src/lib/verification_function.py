class Verification:
    @classmethod
    def verification_table(cls,input, table):
        for i in range(5, -1, -1):
            if table[i][input-1] == " ":
                return True
        print("This column is full.")
        return (False)
    
    @classmethod
    def verification_game_end(cls, table, user):
        if user == 1:
            elem = "O"
        elif user == 2:
            elem = "X"

        count = 0
        #column win condition
        for j in range (7):
            for i in range(5, -1, -1):
                if table[i][j] == elem:
                    count += 1
                    if count == 4:
                        print("a")
                        return(1)
                else:
                    count = 0
        
        count = 0
        #line win condition
        for i in range (7):
            for j in range(7):
                if table[i][j] == elem:
                    count += 1
                    if count == 4:
                        print("b")
                        return(1)
                else:
                    count = 0

        count = 0
        #diagonal north est win condition
        for j in range (4):
            for i in range(5, 2, -1):
                for k in range(4):
                    if table[i-k][j+k] == elem:
                        count += 1
                        if count == 4:
                            print("c")
                            return(1)
                    else:
                        count = 0
        
        count = 0
        #diagonal south est win condition
        for j in range (4):
            for i in range(3):
                for k in range(4):
                    if table[i+k][j+k] == elem:
                        count += 1
                        if count == 4:
                            print("d")
                            return(1)
                    else:
                        count = 0

        return(0)