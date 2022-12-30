# 터렛
# 1002번
import sys
for _ in range(int(sys.stdin.readline().rstrip())):
  x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
  d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
  sum = r1 + r2
  diff = r1 - r2 if r1 > r2 else r2 - r1
  # 1. 두 점에서 만난다
  if diff < d < sum:
    print(2)
  # 2. 같은 원
  elif d == 0 and diff == 0:
    print(-1)
  # 3. 외접 or 내접
  elif diff == d or sum == d:
    print(1)
  # 4. 외부 or 내부
  elif sum < d or d < diff:
    print(0)
  # 5. 동심원
  else:
    print(0)
  
  