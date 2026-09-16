class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            # if nothing is stack or top of stack is negative then nothing can be collide to it
            if not stack or stack[-1] < 0:
                stack.append(asteroid)
            # if asteroid is negative
            elif asteroid < 0:
                # pop until you find
                # - stack is empty
                # - top of stack >= |asteroid|
                # - top of stack is negative

                # note: `> 0` is correct here because contraints guarantee 
                # asteroids[i] != 0 (as asteroid size can not be 0).
                # so {element} > 0 -> alwasys indicates positive numbers.
                
                while stack and stack[-1] < abs(asteroid) and stack[-1] > 0:
                    stack.pop()
                # if top of stack is posstive and it is same as |asteroid|
                # then pop only one element                
                if stack and stack[-1] == abs(asteroid) and stack[-1] > 0:
                    stack.pop()
                # if stack is empty or top of stack is negative
                # then current asteroid can be pushed to stack
                elif not stack or stack[-1] < 0:
                    stack.append(asteroid)
            # if asteroid is positive
            else:
                stack.append(asteroid)
        # stack contains remaining items and this is the answer
        return stack