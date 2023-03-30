# 升序 + 有重复元素
# key: 难题思路图中有解题方案
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums==[]: return [-1, -1]
        f = searchFirst(nums, target)
        l = searchLast(nums, target)
        return [f, l]

def searchFirst(nums, target):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else: # mid == target
            if mid == 0: return mid
            elif mid > 0 and nums[mid-1] != target:
                return mid
            else: # is not the First
                r = mid - 1
    return -1

def searchLast(nums, target):
    last = len(nums)-1
    l, r = 0, last
    while l <= r:
        mid = (l+r)//2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else: # mid == target
            if mid == last: return mid
            elif mid < last and nums[mid+1] != target:
                return mid
            else: # is not the Last
                l = mid + 1
    return -1