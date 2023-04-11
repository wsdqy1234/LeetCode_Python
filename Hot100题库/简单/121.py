# 相当于维护一个单调栈，再添加一个哨兵
# 单调栈记录迄今为止最小的股价，哨兵记录迄今为止最大的利润
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            max_profit = max(price - min_price, max_profit) # 记录迄今为止最大的利润
            min_price = min(price, min_price)               # 记录迄今为止最低的价格
        return max_profit