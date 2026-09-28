class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_price = 0
        last_index = 0
        for i in range(len(prices) - 1, -1, -1):
            num = prices[i]
            if num > last_price:
                last_price = num
                last_index = i
            else:
                break
        
        ans = 0
        for i in range(last_index, -1, -1):
            price = prices[i]
            if price < last_price:
                ans += last_price - price
                last_price = price
            if price > last_price:
                last_price = price
        return ans
