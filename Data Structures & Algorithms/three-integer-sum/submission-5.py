class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for index, curr in enumerate(nums):
            if curr > 0:
                break
            
            if index > 0 and curr == nums[index - 1]:
                continue
            
            left, right = index + 1, len(nums) - 1

            while left < right:
                if curr + nums[left] + nums[right] > 0:
                    right -= 1
                elif curr + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    res.append([curr, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res