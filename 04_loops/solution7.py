while True:
    number_str = input("Enter the number: ")
    number = int(number_str)

    if 1<= number <= 10:
        print("Correct number")
        break
    else:
        print("Enter correct number")
        continue