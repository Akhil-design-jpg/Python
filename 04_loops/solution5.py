# Non repeated character
input_string = "TeeteracadAcdacGg"

for char in input_string:
    print(char)
    if input_string.lower().count(char) == 1:
        print("Answer is: ",char)
        break