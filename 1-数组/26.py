class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                nums[slow + 1] = nums[fast]
                slow = slow + 1
        return slow + 1 #第0个元素也已考虑在内了