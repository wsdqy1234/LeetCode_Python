# 采用异或运算（半加运算），1^1=0, 1^0=1, 0^0=0
# 两个相同元素异或运算后为0，0与单个元素异或运算后为该单个元素

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums[0]
        for i in range(1, len(nums)):
            a = a ^ nums[i]
        return a