#The program calculate the volume of the sphere and calculate and display it on the monitor rounded to 2 digits after the decimal point.



import math
# prompt the user to enter the radius of a sphere
radius = float(input("Enter the radius of the sphere: "))
# calculate the volume of the sphere
volume = 4/3 * math.pi * radius**3
# Display the volume of the sphere
volume = round(volume, 2)
print(f"The volume of the sphere of radius {radius} is {volume,2}")