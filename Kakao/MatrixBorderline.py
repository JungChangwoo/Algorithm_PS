import copy
def move(graph, x1, y1, x2, y2):
    # 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    d = 0
    x, y = x1, y1
    min_value = 10002
    prev = graph[x][y]
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        
        if nx == x1 and ny == y1:
            graph[nx][ny] = prev
            min_value = min(min_value, graph[nx][ny])
            break
        
        if nx >= x1 and nx <= x2 and ny >= y1 and ny <= y2:
            nex = graph[nx][ny]
            graph[nx][ny] = prev
            min_value = min(min_value, graph[nx][ny])
            x, y = nx, ny
            prev = nex
        else:
            d += 1
        
    return min_value

def solution(rows, columns, queries):
    graph = [[(i*columns)+j+1 for j in range(columns) ] for i in range(rows)]
    result = []
    
    for query in queries:
        x1, y1, x2, y2 = query[0]-1, query[1]-1, query[2]-1, query[3]-1
        
        value = move(graph, x1, y1, x2, y2)
        
        result.append(value)
        
    return result