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
        #line win condition
        for i in range(1,4):
            #right line
            if -1<index[1]+i<7 and table[index[0]][index[1]+i] == elem:
                count += 1
                if count == 3:
                    return(1)
            #left line
            if -1<index[1]-i<7 and table[index[0]][index[1]-i] == elem:
                count += 1
                if count == 3:
                    return(1)
            else:
                count = 0
                break
        #digonal up left down right win condition
        for i in range(1,4):
            #up left
            if -1<index[0]-i<6 and -1<index[1]-i<7 and table[index[0]-i][index[1]-i] == elem:
                count += 1
                if count == 3:
                    return(1)
            #down right
            if -1<index[0]+i<6 and -1<index[1]+i<7 and table[index[0]+i][index[1]+i] == elem:
                count += 1
                if count == 3:
                    return(1)
            else:
                count = 0
                break
        #digonal up right down left win condition
        for i in range(1,4):
            #up right
            if -1<index[0]-i<6 and -1<index[1]+i<7 and table[index[0]-i][index[1]+i] == elem:
                count += 1
                if count == 3:
                    return(1)
            #down left
            if -1<index[0]+i<6 and -1<index[1]-i<7 and table[index[0]+i][index[1]-i] == elem:
                count += 1
                if count == 3:
                    return(1)
            else:
                count = 0
                break
        #tie
        for i in range(7):
            if " " in table[i]:
                return(0)
            else:
                return(2)
        return(0)