def hello(name="Jose"):
    print("The hello() function has been executed")

    def greet():
        return "\t This is inside greet() function"
    def welcome():
        return "\t This is inside welcome() function"
    if name=="Jose":
        return greet
    else:
        return welcome

x = hello()

print(x)

print(x())