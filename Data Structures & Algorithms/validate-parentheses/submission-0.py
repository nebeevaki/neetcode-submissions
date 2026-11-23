class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                if char in [")", "]", "}"] and len(stack) == 0:
                    return False
                elif char == ")" and stack[-1] != "(":
                    return False
                elif char == "]" and stack[-1] != "[":
                    return False
                elif char == "}" and stack[-1] != "{":
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        return False
