# Find the sum of integers from 1 to 10, from 20 to 37, and
# from 35 to 49, respectively.
'''sum1 = sum(range(1, 11))
sum2 = sum(range(20, 38))
sum3 = sum(range(35, 50))
print ("sum from 1 to 10:", sum1)
print ("sum from 20, 37:", sum2)
print ("sum from 35, 50:", sum3)'''


# for loop 
n = int(input("Enter an integer:"))
if n == 0:
    factorial = 1
else:
    factorial = 1
    for i in range(1, n+1):
        factorial = factorial * i
print(factorial)

