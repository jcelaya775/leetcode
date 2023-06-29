from typing import List

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l + r) // 2
            res = min(res, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return res


def main():
    nums = [5, 6, 7, 8, 10, 12, 1, 2, 3]
    s = Solution()
    print(s.findMin(nums))


main()
