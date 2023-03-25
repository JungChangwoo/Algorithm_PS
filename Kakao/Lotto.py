def solution(lottos, win_nums):
    z_count = lottos.count(0)
    l_count = 0
    for lotto in lottos:
        if lotto in win_nums:
            l_count += 1
            
    rank = [6, 6, 5, 4, 3, 2, 1]
    answer = [rank[z_count + l_count], rank[l_count]]
    return answer