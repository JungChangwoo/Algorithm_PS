# [해밀턴 경로]
# 기본: 시간복잡도 O(N!)
# DP: 시간복잡도 O(N*2^N)


# 1. (n-1)째 정점은 출발 정점과 반드시 인접
# 2. 경로 상의 i번재 정점은 i-1번째 정점과 인접
# 3. i번째 정점은 그 앞에 오는 i-1번째 정점들 중 하나가 될 수 없다.
def promising(i, w, trace):
    flag = True
    # 마지막에 도달했는데 시작점으로 돌아오지 않는다면
    if i == n - 1 and not w[trace[n - 1]][trace[0]]:
        flag = False
    # 인접하지 않는다면
    elif i > 0 and not w[trace[i - 1]][trace[i]]:
        flag = False
    # 방문한 곳을 또 방문한다면
    else:
        j = 1
        while j < i and flag:
            if trace[i] == trace[j]:
                flag = False
            j += 1
    return flag


# level, 인접행렬, 경로
def hamiltonian(i, w, trace):
    n = len(w) - 1
    # 현재 노드가 조건에 성립한다면 (인접 and not visited)
    if promising(i, w, trace):
        # 마지막에 도달했다면
        if i == n - 1:
            print(trace[:n])
        else:
            # 가능한 다음 노드의 경우의 수를 모두 탐색
            for j in range(2, n + 1):
                trace[i + 1] = j
                hamiltonian(i + 1, w, trace)


INF = int(1e9)
n = 4
edges = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
w = [[False] * (n + 1) for _ in range(n + 1)]
for edge in edges:
    w[edge[0]][edge[1]] = w[edge[1]][edge[0]] = True
trace = [-1] * (n + 1)
trace[0] = 1  # 시작노드 (어떤 노드인지는 상관 x)

hamiltonian(0, w, trace)

##################################################
# 동적 계획법
##################################################
# W = 인접 행렬
# V = 모든 도시의 집합
# A = V의 부분 집합
# D[vi][A] = A에 속한 도시를 각각 한 번씩만 거쳐서 vi에서 v1으로 가는 최단 경로 길이의 길이
# P = 경로
# 재귀 관계식
# D[Vi][공집합] = W[i][1],
# D[vi][A] = min(W[i][j] + D[vj][A - {vj}]), (A가 공집합이 아님)
# : A에 있는 각 노드를 지나쳐가는 경로를 선택했을 때 가장 짧은 것 선택
# 비트 마스크로 부분집합 표현


# 부분집합 포함 확인
def isIn(i, A):
    if A & (1 << (i - 2)) != 0:
        return True
    else:
        return False


# 차집합 (비트를 0으로 만든다.)
def diff(A, j):
    t = 1 << (j - 2)
    return A & (~t)


# A의 원소 갯수 확인
def count(A, n):
    count = 0
    for i in range(n):
        if A & (1 << i) != 0:
            count += 1
    return count


def minimun(W, D, i, A):
    minValue = INF
    minJ = 1
    n = len(W) - 1
    for j in range(2, n + 1):
        if isIn(j, A):
            m = W[i][j] + D[j][diff(A, j)]
            if minValue > m:
                minValue = m
                minJ = j
    return minValue, minJ


# TSP
def travel(w):
    n = len(w) - 1
    size = 2**(n - 1)
    D = [[0] * size for _ in range(n + 1)]
    P = [[0] * size for _ in range(n + 1)]
    # A가 공집합인 경우
    for i in range(2, n + 1):
        D[i][0] = w[i][1]
    # A의 원소 갯수
    for k in range(1, n - 1):
        # 모든 부분집합의 경우의 수
        for A in range(1, size):
            # A의 갯수가 k인 경우
            if count(A, n) == k:
                # 각 노드에서 해당 부분집합을 거치는 경우의 수를 구함
                for i in range(2, n + 1):
                    # i(출발노드)는 부분집합에 포함 X
                    if not isIn(i, A):
                        D[i][A], P[i][A] = minimun(W, D, i, A)
    A = size - 1
    D[1][A], P[1][A] = minimun(W, D, 1, A)
    return D, P


INF = int(1e9)
W = [[-1, -1, -1, -1, -1], [-1, 0, 2, 9, INF], [-1, 1, 0, 6, 4],
     [-1, INF, 7, 0, 8], [-1, 6, 3, INF, 0]]

D, P = travel(W)
print('D = ')
for i in range(1, len(D)):
    print(D[i])
print('P = ')
for i in range(1, len(P)):
    print(P[i])
print('minLenth = ', D[1][2**(len(W) - 2) - 1])
