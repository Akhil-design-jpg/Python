Distance_str = input('Enter distance you want to cover: ')
Distance = int(Distance_str)

if Distance < 3:
    print("Walk")
elif 3<= Distance<= 15:
    print("Bike")
else:
    print("Car")