from itertools import product
data = ['+', '-', '*', '/']
result = list(product(data, repeat = 3))
print(result)
print(len(result))

