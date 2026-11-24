class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                last_temp, last_index = stack.pop()
                result[last_index] = i - last_index
            stack.append([temp, i])
        return result
