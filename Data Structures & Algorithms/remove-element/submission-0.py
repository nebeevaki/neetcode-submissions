class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        for i in range(len(nums)):
            nums[i - count] = nums[i]
            print(nums, count, nums[i])
            if nums[i] == val:
                count += 1
        return len(nums) - count