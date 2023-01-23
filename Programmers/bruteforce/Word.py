# [모음사전]
def DFS(word, target, count, alpha):
    global result
    if word == target:
        result = count
        return count
    if len(word) >= 5:
        return count
    for i in range(5):
        word = word + alpha[i]
        count = DFS(word, target, count + 1, alpha)
        word = word[:-1]
    return count
    
def solution(word):
    global result
    result = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    DFS("", word, 0, alpha)
    return result