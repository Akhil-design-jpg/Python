userAge_str = input("Enter the age of user: ")

userAge = int(userAge_str)

if userAge <= 13:
    print("Child")

elif 13<=userAge<=19:
     print("Teenager")

elif 20<=userAge<=59:
     print("Adult")

else: 
     print("Senior")