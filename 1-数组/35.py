# 升序 + 无重复元素
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 二分查找
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
            
        return l  # 因为如果target不再[l, r]之间的话（l==r了已经），如果target<l，说明要插入到l位置，如果target>l，则l = l+1要插入到新l的位置
        