try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Strings can't be squared")


try:
    x = 5
    y = 0
    z = x/y
except:
    print("Error due to division by zero")
finally:
    print("All Done")


def ask():
    while True:
        try:
            val = int(input("Input an integer : "))
        except:
            print("An error occured! Please try again!")
            continue
        else:
            break
    print("Thank you, you number squared is : ", val ** 2)


ask()
