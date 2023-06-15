from typing import List
import math


class Solution:
    # O(n*logn) Time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search value for k within range [1, max(piles)]
        minK, maxK = 1, max(piles)
        res = maxK

        while minK <= maxK:
            midK = (minK + maxK) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / midK)

            if hours <= h:
                res = min(res, midK)
                maxK = midK - 1
            elif hours > h:
                minK = midK + 1

        return res


def main():
    s = Solution()
    piles = [30, 11, 23, 4, 20]
    h = 5
    print(s.minEatingSpeed(piles, h))


main()
