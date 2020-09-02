import numpy as np

class Table():
    table = ""

    def __init__(self):
        self.table = np.zeros((7,7), dtype=str)
        for i in range(7):
            for j in range(7):
                if i == 6:
                    self.table[i][j] = j + 1
                else:
                    self.table[i][j] = " "

    def set_table(self):
        index = ["",""]
        return(self.table, index)

    @classmethod
    def display_table(cls,table):
        print("")
        for i in range (7):
            print(table[i])
        print("")
        return
    
    @classmethod
    def table_update(cls,input, table, user):
        for i in range(5, -1, -1):
            if table[i][input-1] == " ":
                if user == 1:
                    table[i][input-1] = "O"
                    return(table)
                elif user == 2:
                    table[i][input-1] = "X"
                    return(table)