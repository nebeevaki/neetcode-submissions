class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        set_ans = set()
        for i in range(len(nums)):
            target = nums[i]
            result = self.twoSum(nums, target, i)
            for res in result:
                if tuple(res) not in set_ans:
                    set_ans.add(tuple(res))
                    ans.append(res)
        return ans


    def twoSum(self, numbers: List[int], target: int, left: int) -> List[int]:
        index = left
        right = len(numbers) - 1
        ans = []
        while left < right:
            if numbers[left] + numbers[right] + target > 0:
                right -= 1
            else:
                left += 1
            if left != right and index != left and index != right and numbers[left] + numbers[right] + target == 0:
                ans.append([target, numbers[left], numbers[right]])
        return sorted(ans)