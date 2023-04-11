# 滑窗 + 队列 + 监听最大长度
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        q = []
        max_len = 0
        for i in s:
            while i in q:
                del q[0] # 只要有重复，就删去首位，直到把重复字符完全删除，再把后面的字符加进来
            q.append(i)
            max_len = max(max_len, len(q))
        return max_len