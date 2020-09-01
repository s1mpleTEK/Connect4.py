if __name__ == "__main__":
    try:
        print("hello word.")
    except (EOFError, InterruptedError, KeyboardInterrupt):
        exit()