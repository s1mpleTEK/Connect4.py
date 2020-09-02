class Verification:
    @classmethod
    def verification_table(cls,input, table):
        for i in range(5, -1, -1):
            if table[i][input-1] == " ":
                index = [i, input-1]
                return(index)
        print("This column is full.")
        return (False)
    
    @classmethod
    def verification_game_end(cls, table, user, index):
        if user == 1:
            elem = "O"
        elif user == 2:
            elem = "X"
        count = 0

        #column win condition
        for i in range(1,4):
            if 0<index[0]+i<=5 and table[index[0]+i][index[1]] == elem:
                count += 1
                if count == 3:
                    return(1)
            else:
                count = 0
                break

        #line right win condition
        for i in range(1,4):
            if 0<=index[1]+i<=6 and table[index[0]][index[1]+i] == elem:
                count += 1
                if count == 3:
                    return(1)
            else:
                count = 0
                break
         #line left win condition
        for i in range(1,4):
            if 0<=index[1]-i<=6 and table[index[0]][index[1]-i] == elem:
                count += 1
                if count == 3:
                    return(1)
            else:
                count = 0
                break

        
        return(0)