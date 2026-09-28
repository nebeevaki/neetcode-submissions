class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        last_price = prices[-1]
        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]
            if price < last_price:
                ans += last_price - price
                last_price = price
            if price > last_price:
                last_price = price
        return ans
