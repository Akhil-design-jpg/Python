import math

Leap_year_str = input("Enter leap year: ")
Leap_year = int(Leap_year_str)

if math.floor(Leap_year % 400 == 0):
    print('Leap year divisible by 400, 4 & 100')
    print(Leap_year)
elif math.floor(Leap_year % 4 == 0) and math.floor(Leap_year % 400 != 0):    
    print("Leap year")
    print(Leap_year)
else:
    print("Not a leapyear")


