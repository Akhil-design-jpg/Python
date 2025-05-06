Password = input('Enter your password: ')
pass_length = len(Password)

if pass_length < 6:
    print(pass_length)
    print("Weak password")
elif 6 <= pass_length <= 10:
    print(pass_length)
    print("Medium length")
else:
    print(pass_length)
    print("Strong password")