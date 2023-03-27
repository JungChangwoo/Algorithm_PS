def dfs(now, amount):
    global money, parent
    if now == '-':
        return
    royal = int(amount * 0.1)
    mine = amount - royal
    money[now] += mine
    if royal != 0:
        dfs(parent[now], royal)

def solution(enroll, referral, seller, amount):
    global money, parent
    
    money = dict()
    parent = dict()
    for i, name in enumerate(enroll):
        parent[name] = referral[i]
        money[name] = 0
        
    for i, name in enumerate(seller):
        dfs(name, amount[i] * 100)
        
    return list(money.values())