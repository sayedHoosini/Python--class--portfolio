def factorial(n):
    # function return n factorial
    if n == 0:
        fact = 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact = fact*i
    return fact

def test():
    num = int(input('Enter an integer:'))
    print (f' The factorial of {num} is {factorial(num)}')

test()



