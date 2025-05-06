movie_str = input("Enter you age to get movie ticket: ")
age = int(movie_str)
Price_adult = 12
Price_children = 8
day = ("Enter which day you want to book a ticket: ")
enter_day = input(day)
Total_dis_A = Price_adult - 2
Total_dis_C = Price_children - 2
if age >= 18 and enter_day == "Wednesday":
    print("Ticket price for adults: 12$")
    print("Wednesday Discount- $2")
    print("Total amount: $",Total_dis_A)
elif age<18 and enter_day == "Wednesday":
    print("Ticket price for children: 8$")
    print("Wednesday Discount- 2$")
    print("Total amount: $",Total_dis_C)

else:
    print("No discount on either days")


# Short form
# age = 26

# day = "Wednesday"

# price = 12 if age >= 18 else 8
# print(price)
# Discount = True, price - 2 if day == "Wednesday" else False
# print(Discount)