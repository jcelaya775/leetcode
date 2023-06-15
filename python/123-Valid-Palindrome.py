class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():  # skip
                l += 1
                continue
            if not s[r].isalnum():  # skip
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True


def main():
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("0P  "))


main()
