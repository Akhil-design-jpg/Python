def sum_all(*args):
    # use * for multiple arguments
    print(*args) # it will print result of every def, 3 - output it will do that for every call
    print(args) # (1, 2) - output it will do that for every call
    for i in  args:
        print(i * 2)
    return sum(args)

    

print(sum_all(1,2))
print(sum_all(1,2,3,4,5))
# print(sum_all(1,2,3,4,5,6,7,8))