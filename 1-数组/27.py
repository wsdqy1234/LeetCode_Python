class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """ 
        # 1。快慢指针法
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow = slow + 1
        return slow

        # 2. 双指针法，把右侧的不等于val的元素，换到左侧等于val的元素
        # left, right = 0, len(nums)-1
        # while left <= right:
        #     while left <= right and nums[left] != val:
        #         left = left + 1
        #     while left <= right and nums[right] == val:
        #         right = right - 1
        #     if left < right:
        #         nums[left] = nums[right]
        #         left = left + 1
        #         right = right - 1

        # return left