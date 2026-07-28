class MinStack:

    def __init__(self):
        self.stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop()
        return None
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return 0

    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        return 0
        
