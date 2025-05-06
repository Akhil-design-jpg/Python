input_str = "Python"

reversed_str = ""

for reverse in input_str:
    reversed_str = reverse + reversed_str
print(reversed_str)


# Initial:        reversed_str = ""
# Iteration 1:    reverse = 'P'   → reversed_str = 'P'
# Iteration 2:    reverse = 'y'   → reversed_str = 'y' + 'P' = 'yP'
# Iteration 3:    reverse = 't'   → reversed_str = 't' + 'yP' = 'tyP'
# Iteration 4:    reverse = 'h'   → reversed_str = 'h' + 'tyP' = 'htyP'
# Iteration 5:    reverse = 'o'   → reversed_str = 'o' + 'htyP' = 'ohtyP'
# Iteration 6:    reverse = 'n'   → reversed_str = 'n' + 'ohtyP' = 'nohtyP'
