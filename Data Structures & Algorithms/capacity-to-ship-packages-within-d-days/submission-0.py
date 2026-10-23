class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            need_days = self.need_days(weights, m)
            if need_days <= days:
                r = m
            else:
                l = m + 1
        return l

    def need_days(self, weights, now_w: int) -> int:
        ans = 1
        current = 0
        for w in weights:
            if current + w > now_w:
                ans += 1
                current = w
            else:
                current += w
        return ans