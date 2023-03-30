class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_final = strFinal(s)
        t_final = strFinal(t)
        return s_final == t_final
    
def strFinal(x):
    x = list(x) # 字符串不能直接x[1] = x[2]，要先转化为list
    slow = 0
    for fast in range(len(x)):
        if x[fast]=='#' and slow > 0:
            slow = slow - 1
        elif x[fast]!='#':
            x[slow] = x[fast]
            slow = slow + 1 
    return x[:slow]