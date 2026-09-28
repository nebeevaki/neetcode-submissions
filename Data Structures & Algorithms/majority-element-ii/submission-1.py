class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        first = nums[0]
        count1 = 0
        second = nums[0]
        count2 = 0
        for num in nums:
            if num == first: count1 += 1
            elif num == second: count2 += 1
            elif count1 == 0:
                first = num
                count1 = 1
            elif count2 == 0 and num != first:
                second = num
                count2 = 1
            elif num != first and num != second:
                count1 -= 1
                count2 -= 1
        ans = []
        if nums.count(first) > len(nums) / 3:
            ans.append(first)
        if first != second and nums.count(second) > len(nums) / 3:
            ans.append(second)
        return ans