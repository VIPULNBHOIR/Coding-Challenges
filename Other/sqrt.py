# Python3 program to find floor(sqrt(x)

# Returns floor of square root of x

class Solution(object):
    def mySqrt(self, x):

        if (x == 0 or x == 1):
            return x

        sqr_root = 1
        max_sqr = 0
        while (max_sqr <= x):
            sqr_root += 1
            max_sqr = sqr_root * sqr_root
            
        return sqr_root - 1



print(Solution().mySqrt(65))