class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ('+', '-', '*', '/'):
                stack.append(int(token))
            else:
                operand1 = stack.pop()
                operand2 = stack.pop()
                if token == '+':
                    stack.append(operand2 + operand1)
                elif token == '-':
                    stack.append(operand2 - operand1)
                elif token == '*':
                    stack.append(operand2 * operand1)
                elif token == '/':
                    stack.append(int(operand2 * 1.0 / operand1))

        return stack[-1]
        