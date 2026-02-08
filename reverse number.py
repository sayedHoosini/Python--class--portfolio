# This program takes a four-digit integer as input and prints the digits in reverse order.
number = int(input("Enter a four-digit integer: "))
print(number % 10)
print((number // 10) % 10)
print((number // 100) % 10)
print((number // 1000) % 10)


