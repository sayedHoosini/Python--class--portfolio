# Slope of a line between two points (x1, y1) and (x2, y2)
# input values from users
x1 = float(input("Enter x-coordinate for Point 1: "))
y1 = float(input("Enter y-coordinate for Point 1: "))
x2 = float(input("Enter x-coordinate for Point 2: "))
y2 = float(input("Enter y-coordinate for Point 2: "))

if x2 - x1 == 0:
    slope = None  # Undefined slope (vertical line)
else:
    slope = (y2 - y1) / (x2 - x1)
print("The slope of the line that connects two points (" + str(x1) + "," +str(y1) + ") and (" + str(x2) + "," +str(y2) + ") is " + format(slope, ".5f"))
