class Solution:

    def encode(self, strs: List[str]) -> str:
        nums = []
        for word in strs:
            nums.append(str(len(word)))
        return '_'.join(nums) + "#" + "".join(strs)

    def decode(self, s: str) -> List[str]:
        if len(s) == 1: return []
        index = s.find("#")
        nums = s[:index].split("_")
        ans = []
        left = 0
        for num in nums:
            num = int(num)
            if num == 0:
                ans.append("")
            else:
                ans.append(s[index + 1 + left: index + 1 + left + num])
                left += num
        return ans
