def DSLR(value, oper):
  if oper == 'D':
    return (value * 2) % 10000
  elif oper == 'S':
    if value == 0:
      return 9999
    value -= 1
    return value
  elif oper == 'L':
    value = ((value * 10) + (value // 1000)) % 10000
    return value
  else:
    value = ((value // 10) + ((value % 10) * 1000)) % 10000
    return value
print(DSLR(1234, 'D'))
print(DSLR(1234, 'S'))
print(DSLR(1000, 'L'))
print(DSLR(1, 'R'))