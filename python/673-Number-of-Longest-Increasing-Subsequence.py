from typing import List

# https://leetcode.com/problems/number-of-longest-increasing-subsequence/


class Solution:
    # O(n^2) Time | O(n) Space
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))]  # [lenOfIncSub, count]
        lenLIS, res = 0, 0  # length of LIS, count of LIS

        # i = start of subseq
        for i in range(len(nums) - 1, -1, -1):
            maxLen, maxCnt = 1, 1  # len, count of LIS start from 1

            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:  # increasing
                    length, count = dp[j]  # len, count of LIS start from j
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt

            dp[i] = [maxLen, maxCnt]

        return res


def main():
    nums = [5, 10, 5, 4, 7]
    s = Solution()


main()
