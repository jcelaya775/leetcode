from typing import List

# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)  # map charCounts to list of anagrams

        for s in strs:
            count = [0] * 26  # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)
        return res.values()


def main():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution()
    print(s.groupAnagrams(strs))


main()
