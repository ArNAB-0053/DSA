class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        prev_time = 0
        stack = []
        ans = [0] * n

        for log in logs:
            _id, op, curr_time = log.split(":")
            _id, curr_time = int(_id), int(curr_time)

            # if operation is start
            if op == "start":
                if stack:
                    # a new function is starting
                    # stack[-1] represents which one is currently ongoing
                    # the function on top of the stack was running from prev_time until curr_time - 1
                    ans[stack[-1]] += curr_time - prev_time

                # new function becomes the active one
                stack.append(_id)
                # future time accounting starts from curr_time.
                prev_time = curr_time
            else:
                # current function runs from prev_time through curr_time (inclusive)
                # and that is why +1 here, because ending means also the current field
                ans[_id] += curr_time - prev_time + 1
                # function finishes execution.
                stack.pop()
                # move to the next timestamp since curr_time has already been counted.
                prev_time = curr_time + 1

        return ans