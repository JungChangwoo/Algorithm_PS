def solution(numbers):
    numbers = list(map(str, numbers))
    return str(int("".join(sorted(numbers, key=lambda x: x * 3,
                                  reverse=True))))


from functools import cmp_to_key


def compare(a, b):
    if a + b > b + a:
        return -1
    elif a + b == b + a:
        return 0
    else:
        return 1


def solution(numbers):
    numbers = list(map(str, numbers))
    return str(int("".join(sorted(numbers, key=cmp_to_key(compare)))))
