class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_dict = dict()
        for num in nums:
            if num not in num_dict:
                num_dict[num] = {
                    "count": 1,
                    "seen": False,
                }
        for num in nums:
            if num_dict[num]['seen'] == True:
                continue
            step = 0
            parent = num + 1

            while True:
                if parent not in num_dict or num_dict[parent]['seen'] == True:
                    break
                num_dict[parent]['seen'] = True
                step += 1
                parent += 1
                
            if parent in num_dict and num_dict[parent]['seen']:
                num_dict[num]['count'] += step + num_dict[parent]['count']
            else:
                num_dict[num]['count'] += step
            num_dict[num]['seen'] = True

        ans = 0
        for key in num_dict:
            ans = max(ans, num_dict[key]['count'])
        return ans










        