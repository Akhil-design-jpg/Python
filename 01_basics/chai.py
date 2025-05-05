from hello import chai

chai("Ginger tea")

x = [x**2 for x in range(11)]
print(x)

y = []

for string in x:
    y.append(str(string))
print(y)

for final in y:
    print(final)
    print(type(final))