# 双指针法，从两边开始比大小，大的放到新数组的最右边
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        new = [0]*len(nums)
        new_right = len(nums)-1
        while left <= right:
            l2 = nums[left]**2
            r2 = nums[right]**2
            if l2 < r2:
                new[new_right] = r2
                new_right = new_right - 1
                right = right - 1
            else:
                new[new_right] = l2
                new_right = new_right - 1
                left = left + 1
        return new