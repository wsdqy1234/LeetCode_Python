# 哈希表直接统计每个数字出现的次数，返回最大的对应的key

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        Dict = {}
        for n in nums:
            if n in Dict: 
                Dict[n] = Dict[n] + 1
            else: 
                Dict[n] = 0
        return max(Dict, key=Dict.get)