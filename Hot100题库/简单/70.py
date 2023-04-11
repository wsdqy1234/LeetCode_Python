# 动态规划 f(n) = f(n-1) + f(n-2)
# 边界条件 f(0) = 1, f(1) = 1

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        p, q, r = 0, 0, 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r