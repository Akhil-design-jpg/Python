number = 5
rev = 1
# for num in range(10,0,-1):
#     rev = num * rev
# print(rev)

# using while

while number > 0:
    # rev = rev * number
    # number = number - 1
    rev  *=  number
    number -= 1
print(rev)