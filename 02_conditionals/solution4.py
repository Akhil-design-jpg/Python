Fruit_Name = input("Enter fruit Name: ").lower()
print('Color Should be between Green, Yellow and Brown')
Color = input('Enter Fruit color: ').lower()

if Color == 'green':
    print("Unripe")
elif Color == 'yellow':
    print("Ripe")
elif Color == "brown":
    print("Overripe")
else:
    print("Invalid Color")