from lib.table_function import Table as T
from lib.user_function import User as U
from lib.verification_function import Verification as V

def main():
    try:
        user = U().set_user()
        table = T().set_table()
        T.display_table(table[0])
        while 1:
            print(user[user[2]-1],"'s turn:", end=" ")
            if user[2] == 1:
                print("O")
            else:
                print("X")
            table = U().user_interaction(table[0], user[2])
            game_end = V.verification_game_end(table[0], user[2], table[1])
            T.display_table(table[0])
            if game_end == 1:
                print(user[user[2]-1]," win the game.")
                return(0)
            elif game_end == 2:
                print("Tie.")
                return(0)
            user[2] = U().user_change(user[2])
    except (EOFError, InterruptedError, KeyboardInterrupt):
        exit()

if __name__ == "__main__":
    main()