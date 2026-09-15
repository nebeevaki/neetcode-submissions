class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        min_line = len(min(strs, key=len))
        for i in range(min_line):
            char_set = set()
            for j in range(len(strs)):
                print(strs[j][i])
                char_set.add(strs[j][i])
            if len(char_set) == 1:
                ans += char_set.pop()
            else:
                break
        return ans
