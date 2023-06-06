from typing import List

# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(token))

        return stack[0]


def main():
    tokens = ["4", "13", "5", "/", "+"]
    s = Solution()
    print(s.evalRPN(tokens))


main()
