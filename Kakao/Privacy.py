# [개인정보 수집 유효기간]

# 나의 풀이
def Date_Comparison(idx, today, date):
    if idx == 3:
        return False
    if today[idx] > date[idx]:
        return False
    elif today[idx] < date[idx]:
        return True
    else:
        return Date_Comparison(idx + 1, today, date)

def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    term_dict = dict()
    for term in terms:
        name, length = term.split()
        term_dict[name] = int(length)
    
    result = []
    for idx, privacy in enumerate(privacies):
        date, name = privacy.split()
        date = list(map(int, date.split('.')))
        length = term_dict[name]
        date[0] += (date[1] + length - 1) // 12
        date[1] = (date[1] + length) % 12
        if date[1] == 0:
            date[1] = 12
        if not Date_Comparison(0, today, date):
            result.append(idx + 1)
    return result

# 참조 풀이
def solution2(today, terms, privacies):
    today = list(map(int, today.split('.')))
    today = today[2] + today[1] * 28 + today[0] * 28 * 12
    
    term_dict = dict()
    for term in terms:
        name, length = term.split()
        term_dict[name] = int(length) * 28
    
    result = []
    for idx, privacy in enumerate(privacies):
        expDate, name = privacy.split()
        expDate = list(map(int, expDate.split('.')))
        expDate = expDate[2] + expDate[1] * 28 + expDate[0] * 28 * 12
        expDate += term_dict[name]
        if today >= expDate:
            result.append(idx + 1)
    
    return result
  