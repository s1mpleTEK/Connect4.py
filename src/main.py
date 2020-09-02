from lib.table_function import Table as T
from lib.user_function import User as U

def main():
    try:
        user = U().set_user()
        table = T().set_table()
        T.display_table(table)
        while 1:
            print(user[user[2]-1],"'s turn")
            table = U().user_interaction(table, user[2])
            user[2] = U().user_change(user[2])
            T.display_table(table)
    except (EOFError, InterruptedError, KeyboardInterrupt):
        exit()

if __name__ == "__main__":
    main()