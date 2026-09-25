class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {0: 0, 1: 0, 2: 0}
        
        for num in nums:
            count[num] += 1

        curr = 0
        for i in range(len(nums)):
            while count[curr] == 0:
                curr += 1
            nums[i] = curr
            count[curr] -= 1
            
        return nums