# power calculator (x^n) without using ** or build- in function
# prompt the user for input
x = float(input("Enter the base (x): "))
n = int(input( "Enter the exponent ( n >= 0): "))
# initialize result
result = 1
# Multiply x by itself n times
for i in range (n):
    result *= x
# display the result
print(f"{x} raised to the power of {n} is {result}")