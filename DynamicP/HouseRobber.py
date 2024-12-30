
def RobMoney(pos):

    if pos == 0: return Houses[pos]
    if pos < 0 : return 0

    if dp[pos] != -1: return dp[pos]

    take = Houses[pos] + RobMoney(pos - 2)
    nottake = 0 + RobMoney(pos - 1)

    maximum = max(take, nottake)
    dp[pos] = maximum

    return maximum

if __name__ == '__main__':
    n = int(input())
    Houses = list( int(input()) for _ in range(n))

    dp = [ -1 for _ in range (n)]
    dp[0] = Houses[0]

    print(RobMoney(n-1))
