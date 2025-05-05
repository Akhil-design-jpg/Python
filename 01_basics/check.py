import pyperclip as pc 
from functools import reduce

text1 = 100

pc.copy(text1)

text2 = int(pc.paste())

print("Text copied to clipboard",text2)
print(type(text2))

a = [1,2,3,4,5]

b = reduce(lambda acc, x: acc + [str(x)], a, [])
print(b)

c = []

for x in a:
    c.append(str(x))

print(c)

print(c is b)