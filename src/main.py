from lib.table_function import Table as T
from lib.user_function import User as U

def main():
    try:
        user = U().set_user()
        table = T().set_table()
        T().display_table(table)
        print(user)
    except (EOFError, InterruptedError, KeyboardInterrupt):
        exit()

if __name__ == "__main__":
    main()