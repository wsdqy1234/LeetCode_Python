# 用个 哈希表 + 栈 来解决
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {'(':')', '[':']', '{':'}', '?':'?'}
        stack = ['?']
        for c in s:
            if c in dic: stack.append(c)
            elif dic[stack.pop()] != c: return False #如果s='}'的话，会pop，然后stack就是false
        return len(stack)==1  #如果s='{{'的话，会append，然后stack长度不是1，就是false

        