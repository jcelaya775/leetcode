from typing import List

# https://leetcode.com/problems/generate-parentheses/description/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Only add open if open > 0
        # Only add close if close > open
        # Valid iff open == closed == 0

        stack = []
        res = []

        def backtrack(openRemaining, closedRemaining):
            if openRemaining == closedRemaining == 0:
                res.append("".join(stack))
                return

            if openRemaining > 0:
                stack.append("(")
                backtrack(openRemaining - 1, closedRemaining)
                stack.pop()

            if closedRemaining > openRemaining:
                stack.append(")")
                backtrack(openRemaining, closedRemaining - 1)
                stack.pop()

        backtrack(n, n)
        return res


def main():
    n = 3
    s = Solution()
    print(s.generateParenthesis(n))


main()
