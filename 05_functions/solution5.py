# default_Name = "Akhil"
# Name1 = input("Enter your name")

# def greet(Name):
#     if Name1.strip() == "":
#         print("Hola",default_Name)
#     else:
#         print("Hola",Name)

# greet(Name1)


def greet(User = 'akhil'):
    return 'Hola '+User+" !"

print(greet('chai'))
print(greet())