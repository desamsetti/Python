def new_decorator(func):
    def wrap_func():
        print("Code here, before executing the func()")
        func()
        print("Code here will execute after the func()")

    return wrap_func

@new_decorator
def func_needs_decorator():
    print("This function needs a decorator!")


func_needs_decorator = new_decorator(func_needs_decorator)

print(func_needs_decorator())




