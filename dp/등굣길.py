def solution(m, n, puddles):
    answer = 0

    puddles = [[q, p] for [p, q] in puddles]
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

    answer = dp[n][m] % 1000000007

    return answer