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
        return(self.table)

    def display_table(self,table):
        for i in range (7):
            print(table[i])
        return