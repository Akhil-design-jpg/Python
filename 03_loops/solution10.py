import time

wait_time = 1 # all in seconds
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt: ",attempts + 1,"- Wait time: ",wait_time,"Seconds please wait")
    wait_time *= 2 
    attempts += 1
    time.sleep(wait_time)


# input_str = "434344@!#!@#"
# reversed_str = ""
# reversed_str2 = ""

# for reverse in input_str:
#     print(reverse)
#     reversed_str = reversed_str + reverse
#     reversed_str2 = reverse + reversed_str2
# print(reversed_str)
# print(reversed_str2)

# const = {'a':1,'b':2}

# for i in const.values():
#     print(i)

#     print(type(i))

# for i in const.keys():
#     print(type(i))
    
#     print(i)




# n1 = 1,2,3,4
# n2 = (1,2,3,4)
# n3 = {1,2,3,4}
# n4 = '{}'
# # print(type(n4))
# # n2 = 1234
# # print(type(n3))
# print(type(n1))
# print(type(n2))
# # print(type(n2))
# print(n1 is n2)
# print(id(n1))
# print(id(n2))
# print(id(n1) is id (n2)) # check if n1 and n2 point to the same object
# print(id(n1) == id (n2)) # This correctly compares memory addresses
