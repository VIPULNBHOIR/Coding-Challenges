def count_sequences(n, k):
    MOD = 10000

    # dp[i][j] will store the number of sequences of length i ending with j+1
    dp = [[0] * n for _ in range(k)]

    # Base case: sequences of length 1
    for j in range(n):
        dp[0][j] = 1

    # Fill the dp table
    for i in range(1, k):
        for j in range(n):
            for m in range(j, n, j + 1):
                dp[i][m] = (dp[i][m] + dp[i - 1][j]) % MOD
                print(dp)

    # Sum up all the valid sequences of length k
    total = sum(dp[k - 1][j] for j in range(n)) % MOD

    return total

#Sample Input
n = 2
k = 1
print(count_sequences(n, k))  # Output: 2
n = 2
k = 2
print(count_sequences(n, k))  # Output: 3

n = 7
k = 3
print(count_sequences(n, k))  # Output: 5
