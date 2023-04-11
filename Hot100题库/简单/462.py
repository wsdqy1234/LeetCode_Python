# 异或完，二进制下找1有多少个就完事了
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = x ^ y
        ans = 0
        while a > 0:
            if a % 2 == 1:
                ans = ans + 1
            a = a // 2
        return ans
