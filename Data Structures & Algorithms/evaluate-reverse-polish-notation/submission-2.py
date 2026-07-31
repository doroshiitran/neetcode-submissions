class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # initial a stack = [], operator = {'*','+','/','-'}
        # for i in tokens: stack.append(tokens)
        # if tokens[i] == operator.some() => a = stack.pop() b = stack.pop() stack.push(ceil(b tokens[i] a))
        stack = []
        for token in tokens:
            if token in {'*', '+', '/', '-'}:
                a = stack.pop()
                b = stack.pop()
                if token == '/':
                    stack.append(int(b / a))
                elif token == '*':
                    stack.append(b * a)
                elif token == '+':
                    stack.append(b + a)
                elif token == '-':
                    stack.append(b - a)
            else:
                stack.append(int(token))
        return stack[-1]