def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):
        # print("i:", i)
        # i = N의 개수
        all_case = set()
        check_number = int(str(N) * i)
        # {N}, {NN} , {NNN}...
        all_case.add(check_number)

        for j in range(0, i - 1):
            # print("===================")
            # print("1. dp[", j, "]:", dp[j])
            for op1 in dp[j]:
                # print("2. dp[", -j - 1, "]:", dp[j - 1])
                # print("===================")
                for op2 in dp[-j - 1]:
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)
            # print("all_case:", all_case)
        if number in all_case:
            answer = i
            break
        dp.append(all_case)
        # print("dp:", dp)

    return answer


print(solution(5, 12))
# print(solution(2, 11))

ans = [{5}]
