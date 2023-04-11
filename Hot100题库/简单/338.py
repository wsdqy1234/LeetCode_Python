
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n+1)
        for i in range(1, n+1):
            if i % 2 == 1:
                ans[i] = ans[i-1] + 1 # 奇数是前一位偶数的末位多了一个1
            else:
                ans[i] = ans[i/2]     # 偶数最后一位一定是0，所以1的数量等于其处以2
        return ans