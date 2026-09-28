class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = right = 0
        ans = []
        while left + right < len(word1) + len(word2):
            if left == right and left < len(word1) or right >= len(word2):
                ans.append(word1[left])
                left += 1
            else:
                ans.append(word2[right])
                right += 1
        return "".join(ans)