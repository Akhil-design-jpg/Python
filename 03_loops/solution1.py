numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_num_Count = 0
for num in numbers:
    if num > 0:
        positive_num_Count += 1
print("Final count of Positive number is: ",positive_num_Count)

# positive_num_count will go from 0 to 6 when it checks the number inside list of Numbers
# 1 -> Count 1, -2 -> Count still 1 , 3 -> Count 2 and so onn