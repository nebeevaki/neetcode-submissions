class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        now = 1
        for i in range(len(nums)):
            num = nums[i]
            if num >= 1 and i != num - 1 and num < len(nums):
                while True:
                    parent = nums[num - 1]
                    nums[num - 1] = num
                    if parent <= 0 or parent > len(nums) or nums[parent - 1] == parent:
                        break
                    num = parent
        now = 1
        for i in range(len(nums)):
            if nums[i] != now:
                return now
            now += 1
        return now
