class Solution:
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