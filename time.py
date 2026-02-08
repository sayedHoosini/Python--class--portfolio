# This program calculates the current time in various formats using the time module.
import time

currentTime = time.time()
print("Current time in seconds since the epoch:", currentTime)
print("Current year:", time.localtime(currentTime).tm_year)
totalSeconds = int(currentTime)
currentMinutes = totalSeconds // 60
currentHours = currentMinutes // 60
print("Current hours:", currentHours)
print("Current minutes:", currentMinutes % 60)
print("Current seconds:", totalSeconds % 60)
print ("Time since epoch in days:", currentHours // 24)
print("Current day of the week:", (currentHours // 24 + 4) % 7)
print("Current day of the month:", (currentHours // 24) % 30)
print("Current month:", (currentHours // 24) % 12)
print("Current year:", 1970 + currentHours // 24 // 365)
# The above code calculates the current time in seconds since the epoch, the current year, hours, minutes, seconds, days since the epoch, day of the week, day of the month, month, and year using the time module.