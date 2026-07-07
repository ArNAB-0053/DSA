class Solution:   
    def operation(self, a: int, b: int, op: str) -> int:
        match op:
            case '+':
                return b + a
            case '-':
                return b - a
            case '*':
                return b * a
            case '/':
                return int(b / a)

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ch in tokens:
            if ch in "+-*/":
                a = stack.pop()
                b = stack.pop()
                op = self.operation(a, b, ch)
                stack.append(op)
            else:
                stack.append(int(ch))
    
        return stack[-1]