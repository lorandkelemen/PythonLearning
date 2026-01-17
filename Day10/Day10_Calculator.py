#implement calculator with 4 ops
#asks for 1st nr then op then 2nd nr then continue or print result

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculate(first_nr, second_nr):
    first_nr = int(input("enter first number"))
    op = input("what operation would you like to do?:\n+\n-\n/\n*\n")
    second_nr = int(input("enter second number"))
    result = 0

    if op == "+":
        result = add(first_nr, second_nr)
    elif op == "-":
        result = subtract(first_nr, second_nr)
    elif op == "*":
        result = multiply(first_nr, second_nr)
    elif op == "/":
        result = divide(first_nr, second_nr)

    return print(f"The result is {result}")
calculate(1,2)



