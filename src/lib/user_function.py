import re

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdir)

from verification_function import Verification as V
from table_function import Table as T

class User():
    user = ["","",""]

    def set_user(self):
        self.user = [input("Player 1 enter your name: "),
                    input("Player 2 enter your name: "),
                    1]
        return(self.user)
    
    def user_interaction(self, table, user):
        selec = input("Select the raw where you want to play: ")
        if len(selec) == 1 and bool(re.match('^[1-7]*$', selec))==True:
            if V.verification_table(int(selec), table):
                return(T.table_update(int(selec), table, user))
            else:
                return(self.user_interaction(table, user))
        else:
            print("wrong input")
            return(self.user_interaction(table, user))

    def user_change(self, user):
        switch={1:2, 2:1}
        return switch.get(user)