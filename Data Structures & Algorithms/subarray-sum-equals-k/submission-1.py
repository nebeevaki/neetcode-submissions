class Solution:
    def createPrefix(self, nums) -> list:
        prefix = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]
        return prefix 

    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = self.createPrefix(nums)
        ans = 0
        sum_dict = dict()

        for num in prefix:
            if num - k in sum_dict:
                ans += sum_dict[num - k]
            sum_dict[num] = sum_dict.get(num, 0) + 1
        
        return ans
            