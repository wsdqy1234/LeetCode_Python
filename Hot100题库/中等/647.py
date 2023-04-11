# 中心扩散法，可以解决所有回文问题

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count1 = self.expand(s, i, i, 0)
            count2 = self.expand(s, i, i+1, 0)
            count = count + count1 + count2
        return count

    def expand(self, s, left, right, count):
        while left>=0 and right<len(s) and s[left]==s[right]:
            count = count + 1
            left = left - 1
            right = right + 1
        return count