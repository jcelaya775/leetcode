from typing import List

# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        currMin = min(self.min[-1], val) if self.min else val
        self.min.append(currMin)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min[-1] if self.min else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def main():
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())


main()
