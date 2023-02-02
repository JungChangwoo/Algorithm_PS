# [N으로 표현]
def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        cases = set()
        cases.add(int(str(N) * i))

        for j in range(0, i - 1):
            for op1 in dp[j]:
                for op2 in dp[i - j - 2]:
                    cases.add(op1 + op2)
                    cases.add(op1 - op2)
                    cases.add(op1 * op2)
                    if op2 != 0:
                        cases.add(op1 // op2)

        if number in cases:
            answer = i
            break

        dp.append(cases)
    return answer
