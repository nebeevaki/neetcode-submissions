class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = 0
        stack = []
        for x in operations:
            if x == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            elif x == "D":
                stack.append(int(stack[-1]) * 2)
            elif x == "C":
                stack.pop()
            else:
                stack.append(int(x))
        return sum(stack)
