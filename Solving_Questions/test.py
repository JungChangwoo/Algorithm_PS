test = [[] for _ in range(6) ]
print(test)
test[5].append([1,2,3,4,5])
test[5].append([1,2,3,4,5])
print(test[5][1][2])