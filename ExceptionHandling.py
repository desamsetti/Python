def askint():
    while True:
        try:
            val = int(input("Please enter an integer : "))
        except:
            print("Looks like you didn't enter an integer")
            continue
        else:
            print("Correct, that is an integer!")
        finally:
            print("Finally block executed!")
        print(val)

askint()