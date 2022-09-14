# [선분교차 CCW]

# 기본: 벡터 쌍들의 CCW를 구하고 그 방향이 다르면 선분이 교차한다.
# 종류: 시계방향, 반시계방향, 일직선

import sys


def ccw(pp1, pp2, pp3):
    value = (pp2[0] - pp1[0]) * (pp3[1] - pp1[1]) - (pp2[1] - pp1[1]) * (
        pp3[0] - pp1[0])
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0


def is_crossing(p1, p2, p3, p4):
    left_value = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    right_value = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if left_value == 0 and right_value == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        return p3 <= p2 and p1 <= p4
    else:
        return left_value <= 0 and right_value <= 0


x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
p1 = [x1, y1]
p2 = [x2, y2]
p3 = [x3, y3]
p4 = [x4, y4]
result = is_crossing(p1, p2, p3, p4)
if result:
    print(1)
else:
    print(0)
