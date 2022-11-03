from typing import List

# https://leetcode.com/problems/merge-intervals/https://leetcode.com/problems/merge-intervals/

class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        res = [intervals[0]]
        intervals.sort(key=lambda interval: interval[0])
        for start, end in intervals[1:]:
            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])
        return res


def main():
    s = Solution()
    intervals = [[1, 3], [5, 6], [2, 5], [10, 12]]
    print(s.mergeIntervals(intervals))


main()