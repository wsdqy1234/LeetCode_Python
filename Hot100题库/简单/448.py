# 利用nums本身当作哈希表，遇到什么元素就在该位置上+n来表示出现过，然后最后找出所有不超过n的位置，就是没有出现过的元素
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            tmp = (nums[i] - 1) % n
            nums[tmp] = nums[tmp] + n
        
        return [i+1 for i,num in enumerate(nums) if num <= n]