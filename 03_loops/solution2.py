n = input("Enter how many numbers you want: ")
numbers = int(n)
sum_even = 0

for i in range(1,numbers+1):
    # print(i)
    # if i % 2 == 0:
    #     print(sum_even + 1)
    if i % 2 == 0:
            sum_even += i

print(sum_even)