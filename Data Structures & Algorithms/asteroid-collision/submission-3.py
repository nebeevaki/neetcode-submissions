class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for aster in asteroids:
            destroy = False
            if aster > 0:
                stack.append(aster)
            else:
                while stack and not destroy and stack[-1] > 0:
                    last = stack[-1]
                    if abs(aster) > last:
                        stack.pop()
                        continue
                    elif abs(aster) == last:
                        stack.pop()
                        destroy = True
                    elif abs(aster) < last:
                        destroy = True
                if not destroy:
                    stack.append(aster)
        return stack