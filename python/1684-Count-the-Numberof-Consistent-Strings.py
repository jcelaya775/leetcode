# https://leetcode.com/problems/count-the-number-of-consistent-strings/


class Solution:
    # O(n * m) Time | O(1) Space
    # Where n = number of words and m = length of longest string
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        res = 0

        for word in words:
            is_consistent = True

            for letter in word:
                if letter not in allowed:
                    is_consistent = False
                    break

            if is_consistent:
                res += 1

        return res
