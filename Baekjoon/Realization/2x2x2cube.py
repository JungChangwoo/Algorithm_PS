# [2x2x2 큐브]
# 16939번
import sys
def is_possible(cube):
  for i in range(1, 25, 4):
    color = cube[i]
    for j in range(i, i + 4):
      if cube[j] != color:
        return False
  return True

def roll(array, dir):
  temp = array[:]
  # 시계 방향
  if dir == 1:
    temp[0] = array[6]
    temp[1] = array[7]
    for i in range(2, 8):
      temp[i] = array[i-2]
  # 반시계 방향
  else:
    temp[6] = array[0]
    temp[7] = array[1]
    for i in range(6):
      temp[i] = array[i+2]
  return temp

def rotate():
  # 수직 왼쪽
  for i in range(2):
    c1 = cube[:] 
    c1[7], c1[5], c1[3], c1[1], c1[22], c1[24], c1[11], c1[9] = roll(list([c1[7], c1[5], c1[3], c1[1], c1[22], c1[24], c1[11], c1[9]]), i)
    if is_possible(c1):
      return True
  # 수직 오른쪽
  for i in range(2):
    c2 = cube[:]
    c2[8], c2[6], c2[4], c2[2], c2[21], c2[23], c2[12], c2[10] = roll(list([c2[8], c2[6], c2[4], c2[2], c2[21], c2[23], c2[12], c2[10]]), i)
    if is_possible(c2):
      return True
  # 수평 위
  for i in range(2):
    c3 = cube[:]
    c3[9], c3[10], c3[19], c3[17], c3[4], c3[3], c3[14], c3[16] = roll(list([c3[9], c3[10], c3[19], c3[17], c3[4], c3[3], c3[14], c3[16]]), i)
    if is_possible(c3):
      return True
  # 수평 아래
  for i in range(2):
    c4 = cube[:]
    c4[11], c4[12], c4[20], c4[18], c4[2], c4[1], c4[13], c4[15] = roll(list([c4[11], c4[12], c4[20], c4[18], c4[2], c4[1], c4[13], c4[15]]), i)
    if is_possible(c4):
      return True    
  # 가운데 아래
  for i in range(2):
    c5 = cube[:]
    c5[7], c5[8], c5[19], c5[20], c5[23], c5[24], c5[15], c4[16] = roll(list([c5[7], c5[8], c5[19], c5[20], c5[23], c5[24], c5[15], c4[16]]), i)
    if is_possible(c5):
      return True    
  # 가운데 위
  for i in range(2):
    c6 = cube[:]
    c6[5], c6[6], c6[17], c6[18], c6[21], c6[22], c6[13], c6[14] = roll(list([c6[5], c6[6], c6[17], c6[18], c6[21], c6[22], c6[13], c6[14]]), i)
    if is_possible(c6):
      return True    
  return False

cube = [0] + list(map(int, sys.stdin.readline().split()))
result = rotate()
if result:
  print(1)
else:
  print(0)