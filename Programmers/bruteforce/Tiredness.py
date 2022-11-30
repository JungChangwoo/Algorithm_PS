def dfs(now, count, dungeons):
    global visited, n, result
    result = max(result, count)
    for i in range(n):
        if not visited[i] and now >= dungeons[i][0]:
            visited[i] = True
            dfs(now - dungeons[i][1], count + 1, dungeons)
            visited[i] = False
    
def solution(k, dungeons):
    global visited, n, result
    result = 0
    n = len(dungeons)
    visited = [False] * n
    dfs(k, 0, dungeons)
    return result