from collections import defaultdict

# https://leetcode.com/problems/permutation-in-string/description/


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = defaultdict(int)
        s2Count = defaultdict(int)
        for c in s1:
            s1Count[c] += 1

        # Grow window
        l = 0
        for r in range(len(s2)):
            s2Count[s2[r]] += 1

            # Shrink window while s2 letter counts > s1 letter counts
            while l < r and s2Count[s2[l]] > s1Count[s2[l]]:
                s2Count[s2[l]] -= 1
                l += 1

            if s1Count == s2Count:
                return True

        return s1Count == s2Count


def main():
    s1 = "ab"
    s2 = "eidbaooo"
    s = Solution()
    print(s.checkInclusion(s1, s2))


main()
