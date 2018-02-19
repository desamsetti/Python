def my_addition_function(arg1,arg2):
    print(arg1+arg2)


my_addition_function(1,2)



def add_num(num1,num2):
    return num1+num2

print(add_num(2,3))


def is_prime(num):
    for n in range(2,num):
        if num%n==0:
            print("The number is not prime")
            break
        else:
            print("The number is prime")
            break


is_prime(5)