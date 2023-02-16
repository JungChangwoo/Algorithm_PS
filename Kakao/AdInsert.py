import heapq
def solution(play_time, adv_time, logs):
    play_time = str_to_int(play_time)
    adv_time = str_to_int(adv_time)
    
    arr = [0] * (play_time + 1)
    for idx, log in enumerate(logs):
        start, end = log.split('-')
        start = str_to_int(start)
        end = str_to_int(end)
    
        arr[start] += 1
        arr[end] -= 1
    
    for i in range(1, play_time + 1):
        arr[i] = arr[i] + arr[i-1]
    
    for i in range(1, play_time + 1):
        arr[i] = arr[i] + arr[i-1]
    
    
    max_value = 0
    answer = 0
    for start in range(play_time + 1):
        end = start + adv_time - 1
        
        if end > play_time:
            break
        
        value = 0
        if start == 0:
            value = arr[end]
        else:
            value = arr[end] - arr[start - 1]
            
        if value > max_value:
            answer = start
            max_value = value
    
    return int_to_str(answer)

def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def int_to_str(time):
    h = time // 3600
    h = str(h).zfill(2)
    time %= 3600
    
    m = time // 60
    m = str(m).zfill(2)
    time %= 60
    
    s = time
    s = str(s).zfill(2)
    return h + ':' + m + ':' + s