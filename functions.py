#srtings
def student(firstname, lastname):
    return firstname,lastname
firstname = input("enter firstname")
lastname = input("enter lasname")
result = student(firstname, lastname)
print(result)

# A simple Python function to check
# whether x is even or odd
def evenOdd( x ):
    if (x % 2 == 0):
        return "given number is even value"
    else:
        return "given number is odd value"

x = int(input("enter a number"))
result = evenOdd(x)
print(result)

#add function
def add(a,b):
    c=a+b
    return c
a = int(input("enter a number a"))
b = int(input("enter a number b"))
result = add(a,b)
print(result)


