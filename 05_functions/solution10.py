# recursive funtion to create a factorial of a number

#  Basic method
# def factorial(Number):
#     result = 1
#     for num in range(Number,0,-1):
#         result *= num
#     print(result)

# factorial(5)

# Recursive method

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))