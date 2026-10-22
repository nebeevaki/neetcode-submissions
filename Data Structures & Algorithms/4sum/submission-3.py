class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i, first in enumerate(nums):  
            if i > 0 and first == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                curr = nums[j]
                if j > i + 1 and curr == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    total = first + curr + nums[left] + nums[right]
                    if total > target:
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        res.append([first, curr, nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        return res
