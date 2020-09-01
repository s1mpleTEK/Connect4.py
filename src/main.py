from table.table_function import Table as T

def main():
    try:
        table = T().set_table()
        T().display_table(table)
    except (EOFError, InterruptedError, KeyboardInterrupt):
        exit()

if __name__ == "__main__":
    main()