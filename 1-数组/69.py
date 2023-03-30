# 找到最后一个元素ans，使得ans^2<=x
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 0, x
        ans = -1    # The answer
        while l<=r:
            mid = (l+r)//2
            mid2 = mid*mid
            if mid2 > x: # mid too large
                r = mid - 1
            else: # mid small
                ans = mid 
                l = mid + 1 
        return ans