from itertools import combinations_with_replacement
def solution(n, info):
    answer = [-1]
    max_value = -1
    
    score_num = [i for i in range(11)]
    
    for score_list in list(combinations_with_replacement(score_num, n)):
        lion = 0
        appeach = 0
        
        score_board = [0] * 11
        for score in score_list:
            score_board[10 - score] += 1
        
        for i in range(11):
            if info[i] < score_board[i]:
                lion += 10 - i
            elif info[i] != 0:
                appeach += 10 - i
        
        diff = lion - appeach
        if max_value < diff and diff > 0:
            answer = score_board
            max_value = diff
        
    return answer