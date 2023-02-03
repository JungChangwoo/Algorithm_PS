# 이모티콘 할인 행사
def get_result(sales, users, emoticons):
    global answer
    plus_count = 0
    costs = 0
    for ratio, price in users:
        total = 0
        for idx, sale in enumerate(sales):
            if ratio <= sale:
                total += emoticons[idx] - (emoticons[idx] * (sale / 100)) 
        if total >= price:
            plus_count += 1
        else:
            costs += total
            
    answer = max(answer, [plus_count, costs])

def dfs(idx, sales, users, emoticons):
    if idx == len(emoticons):
        get_result(sales, users, emoticons)
        return
    
    for sale in [10, 20, 30, 40]:
        sales.append(sale)
        dfs(idx + 1, sales, users, emoticons)
        sales.pop()
    
def solution(users, emoticons):
    global answer
    answer = [0, 0]
    
    dfs(0, [], users, emoticons)
    return answer