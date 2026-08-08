class MinStack:

    def __init__(self):
        self.minu = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minu or val <= self.minu[-1]:
            self.minu.append(val)

    def pop(self) -> None:
        rem = self.stack.pop()
        if rem == self.minu[-1]:
            self.minu.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minu: return self.minu[-1]
        return