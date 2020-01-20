import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper(operand, op1, op2):
            if operand == '+':
                return op1 + op2
            if operand == '-':
                return op1 - op2
            if operand == '*':
                return op1 * op2
            if operand == '/':
                if op1 / op2 > 0:
                    return math.floor(op1 / op2)
                else:
                    return math.ceil(op1 / op2)

        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                op2 = stack.pop(-1)
                op1 = stack.pop(-1)
                tmp = helper(t, op1, op2)
                print(tmp)
                stack.append(tmp)
            else:
                stack.append(int(t))

        return stack[0]
