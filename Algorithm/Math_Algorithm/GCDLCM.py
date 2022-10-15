# [최대공약수 (Greatest Common Divisor)]
a = 10
b = 12
for i in range(min(a, b), 0, -1):
  if a % i == 0 and b % i == 0:
    print(i)
    break

# [최소공배수 (Least Common Multiple)]
for i in range(max(a, b), (a*b) + 1):
  if i % a == 0 and i % b == 0:
    print(i)
    break

# [유클리드 호제법]
# <최대 공약수>
# x와 y의 최대공약수 == y와 r의 최대공약수
# (r = x % y)
def GCD(x, y):
  while y:
    x, y = y, x % y
  return x

# <최대공약수>
def LCM(x, y):
  return (x*y) // GCD(x, y)

print(GCD(a, b))
print(LCM(a, b))