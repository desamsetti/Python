x = 0

while x < 10:
    print("X is currently:  ",x)
    x+=1
else:
    print("All done")


x = 0

while x < 10:
    print("X is currently:  ",x)
    print("X is still less than 10, adding 1 to x")
    x+=1
    if x==3:
        print("Hey x equals 3!")
    else:
        print("Continuing...")
        continue