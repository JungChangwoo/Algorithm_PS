# [단속 카메라 설치하기]
def solution(routes):
    routes.sort(key = lambda x: x[1])
    result = 0
    camera = -300001
    for a, b in routes:
        if camera < a:
            camera = b
            result += 1
        
    return result