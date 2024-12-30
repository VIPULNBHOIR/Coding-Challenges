class Solution():
    def SumOfNfibbo(self, N):
        fibb1 = 0
        fibb2 = 1
        if N <= 2:
            return N-1

        sum = fibb1 + fibb2
        for _ in range(2, N):
            t = fibb1
            fibb1 = fibb2
            fibb2 = fibb1 + t
            sum +=  fibb2
            print(fibb2)
        return sum

n = int(input())

print(Solution().SumOfNfibbo(n))