class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        find = set()
        for i, first in enumerate(nums):  
            if i > 0 and first == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                curr = nums[j]
                left, right = j + 1, len(nums) - 1

                while left < right:
                    if first + curr + nums[left] + nums[right] > target:
                        right -= 1
                    elif first + curr + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        if (first, curr, nums[left], nums[right]) not in find:
                            res.append([first, curr, nums[left], nums[right]])
                            find.add((first, curr, nums[left], nums[right]))
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
        return res
