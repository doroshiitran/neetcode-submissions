class Solution:
    def isValid(self, s: str) -> bool:
        preset = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for char in s:
            if char in preset.keys():
                stack.append(char)
            elif stack and char == preset[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack