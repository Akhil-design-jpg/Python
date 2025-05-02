print('hello')


def chai(n):
    print(n)

chai(4)


chai_one = "lemon tea"
chai_two = "ginger tea"
chai_three = "masala chai"


def percent_calculate(number,whole):
    percentage = (number/whole)*100
    return f"{percentage:.2f}%"
# f to give answer in float(decimal)
# 2f - 2 float (2 decimal units)
result = percent_calculate(20,200)
print(result)