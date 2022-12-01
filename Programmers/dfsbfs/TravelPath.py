### 나의 풀이 ###
from collections import defaultdict
def dfs(now, path, tickets, graph):
    global gpath
    if len(path) >= len(tickets) + 1:
        gpath = min(gpath, path)
    for i in range(len(graph[now])):
        next_graph = graph.copy()
        next_graph[now] = graph[now][:i] + graph[now][i+1:]
        result = dfs(graph[now][i], path + [graph[now][i]], tickets, next_graph)

def solution(tickets):
    global graph, gpath
    tickets.sort(key = lambda x: (x[0], x[1]))
    gpath = ['ZZZZZZZ']
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    dfs('ICN', ['ICN'], tickets, graph)
    return gpath

### 타인 풀이 참고 (Enumerate) ###
from collections import defaultdict
def dfs(now, path, n):
    global gpath, graph
    if len(path) >= n + 1:
        gpath = min(gpath, path)
    for idx, next in enumerate(graph[now]):
        graph[now].pop(idx)
        result = dfs(next, path + [next], n)
        graph[now].insert(idx, next)

def solution(tickets):
    global graph, gpath
    tickets.sort(key = lambda x: (x[0], x[1]))
    gpath = ['ZZZZZZZ']
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    dfs('ICN', ['ICN'], len(tickets))
    return gpath