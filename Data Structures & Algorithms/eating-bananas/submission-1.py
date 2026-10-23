import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, sum(piles)

        while l < r:
            k = (l + r + 1) // 2
            need_time = self.kEat(piles, k)
            if need_time <= h:
                r = k - 1
            else:
                l = k
        return l + 1

    def kEat(self, piles, k) -> int:
        ans = 0
        for pile in piles:
            ans += math.ceil(pile / k)
        return ans
        