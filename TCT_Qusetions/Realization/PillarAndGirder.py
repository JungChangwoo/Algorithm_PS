def possible(answer):
    for part in answer:
        x, y, stuff = part
        if stuff == 0:
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        else:
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                continue
            return False
    return True 

def solution(n, build_frame):
    answer = []
    
    for build in build_frame:
        x, y, stuff, operate = build
        if operate == 0:
            answer.remove([x, y, stuff])
            if possible(answer) == True:
                continue
            else: 
                answer.append([x, y, stuff])
        else:
            answer.append([x, y, stuff])
            if possible(answer) == True:
                continue
            else:
                answer.remove([x, y, stuff])
    answer.sort()
    return answer