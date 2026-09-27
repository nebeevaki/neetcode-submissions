class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count_zero = index_zero = 0
        num_dict = dict()
        ans = []
      
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1

        if 0 in num_dict and num_dict[0] >= 2:
            return [0] * len(nums)

        elif 0 in num_dict and num_dict[0] == 1:
            index_zero = nums.index(0)
            ans = [0] * len(nums)
            result = 1
            for num in nums[:index_zero] + nums[index_zero + 1:]:
                result *= num
            ans[index_zero] = result
            return ans
            
        else:
            num_set = set(nums)
            result = 1
            for key in num_dict:
                result *= key ** (num_dict[key] - 1)          
            ans = []
            for num in nums:
                curr_set = num_set - {num}
                curr_prod = 1
                for uniq in curr_set:
                    curr_prod *= uniq
                ans.append(result * curr_prod)
            return ans
            


# 2 3 4 4 5 5
# result = 20
# 2 = 20 * 3 * 4 * 5
# 5 * 5 * 4 * 4 * 3