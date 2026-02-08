# condtional statement 1
i =  int(input("Enter a number: "))
if i  % 5 == 0:
    print(f'{i} is divisible by 5')
else:
    print(f'{i} is NOT divisible by 5')

print("this is the end")


# condtional statement 2
i =  int(input("Enter a number: "))
if i  % 2 == 0:
    print(f'{i} is even')
else:
    print(f'{i} is odd')

print("this is the end")


# condtional statement 3
i =  int(input("Enter a number: "))
if i  % 5 == 0:
    print(f'{i} is divisible by 5')
else:
    print(f'{i} % 5 is {i%5} 5')
    print(f' So {i} is NOT divisible by 5')

print("this is the end")

import math
# condtional statement 4

radius = float(input("Enter the the radius:"))

if radius >= 0:
    area = math.pi * radius**2
    print(f'The area  for circle of radius {radius} is {area}')
else:
    print(f'{radius} is an invalid radius')



# condtional statement  write a program that give passing and filling score to student 5

score = float(input("Enter the student's score: "))

if score >= 70:
    print(f'The student with a score of {score} has passed.')
else:
    print(f'The student with a score of {score} has failed.')
