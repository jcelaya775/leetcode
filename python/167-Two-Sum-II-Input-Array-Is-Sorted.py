from typing import List

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum < target:
                l += 1
            elif currSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]


def main():
    numbers = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum(numbers, target))


main()
