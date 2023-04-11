# 1. 采用动态规划DP，维护一个D[i, j]，表示第i个字符到第j个字符是否是回文，D[i, i] = 1, D[i, j] = D[i+1, j-1] and s[i]==s[j]，然后找为1的D[i, j]里面最大的j-i+1
# 2. 采用中心扩散法，从D[i, i]开始，或从[D[i,i], D[i, i+1]]开始，每次判断前一位i-1是否等于后一位j+1，然后遍历所有i，期间监听最大的长度

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        for i in range(len(s)):
            # 从i开始往左右扩散
            left1, right1 = self.expand(s, i, i)
            # 如果s[i]==s[i+1]的话，从i, i+1 开始往左右扩散
            left2, right2 = self.expand(s, i, i+1)
            # 监听最长的回文子串
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end+1]
                
    def expand(self, s, left, right):
        while left >= 0 and right<len(s) and s[left]==s[right]:
            left = left - 1
            right = right + 1
        return left+1, right-1