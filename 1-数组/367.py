class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num
        while l<=r:
            mid = (l+r)//2
            mid2 = mid*mid
            if mid2 < num:
                l = mid + 1
            elif mid2 > num:
                r = mid - 1
            else:
                return True
        return False