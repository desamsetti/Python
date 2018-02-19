def vol(rad):
    return (4/3)*(3.14)*(rad*rad*rad)
print(vol(5))


#Function to check whether a number is in given range
def ran_check(num,low,high):
    count = low
    for num in range(low,high+1):
        count=count+1
        if num==count:
            return True
        else:
            return False



print(ran_check(4,2,6))


def ran_bool1(num,low,high):
    return num in range(low,high+1)



#def ran_bool(num,low,high):
def ran_check(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False

print(ran_bool1(1,2,10))




#Count the number of Uppercase letters and Lower case letters
def up_low(s):
    countUpper=0
    countLower=0
    l = [letter for letter in s]

    for x in l:
        if x.isupper():
            countUpper = countUpper+1
        elif x.islower():
            countLower = countLower+1
    print(l)
    print("The number of Uppercase letters are :",countUpper)
    print("The number of Lowercase letters are :",countLower)


up_low("HeyHelloHowAreYou")


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')




def unique_list(l):
    return set(l)


def unique_list1(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return a





print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))




def multiply(numbers):
    #product = numbers[0]
    product = 1
    for l in numbers:
        product*=l
    print(product)

multiply([1,2,3,-4])


def palindrome(s):
    s=s.replace(' ','')
    count =0
    x = s
    x = x[::-1]
    print(x)
    length = len(x)
    while count < length:
        count=count+1
        if s[count] == x[count]:
            return True
        else:
            return False



print(palindrome("madam"))



def palindrome1(s):
    s=s.replace(' ','')
    return s==s[::-1]

print(palindrome1("nurses run"))




import string
def ispanagram(str1,alphabet=string.ascii_lowercase):
    alphaset=set(alphabet)
    return alphaset <= set(str1.lower())