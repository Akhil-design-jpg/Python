Animal_Name = input("Enter animal name: ").lower()
Animal_age_str = input('Enter animal age: ')
Animal_age = int(Animal_age_str)

if Animal_Name == "dog" and Animal_age <= 2:
    print("Puppy food")

elif Animal_Name == "cat" and Animal_age >= 5:
    print("Senior cat food")

else:
    print("Invalid name or age")
