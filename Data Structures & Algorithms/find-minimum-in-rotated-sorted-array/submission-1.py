class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r + 1) // 2
            ans = min(ans, nums[l], nums[m], nums[r])
            if nums[l] > nums[m]:
                r = m - 1
            else:
                l = m
        return ans