class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()])
        for i in range(len(s) // 2):
            if (s[i]).lower() != (s[len(s) - i - 1]).lower():
                return False
        return True
