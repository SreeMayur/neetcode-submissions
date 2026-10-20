class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                b, a = stack.pop(), stack.pop()
                if token == '+': val = a+b
                elif token == '-': val = a-b
                elif token == '*': val = a*b
                else: val = int(a/b)
                stack.append(val)
            else:
                stack.append(int(token))
        return stack[-1]