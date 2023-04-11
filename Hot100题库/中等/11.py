# 双指针，每次向内移动更短的板子，因为如果移动更长的板子，则由于短板效应，存储水量必定下降
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        max_water = 0
        while l <= r:
            tmp_water = min(height[l], height[r])*(r - l)
            max_water = max(max_water, tmp_water)
            if height[l] <= height[r]:
                l = l + 1
            else:
                r = r - 1
        return max_water