class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        1. if not a-z or 0-9 return false
        2. strim, sort reverse, compare with the str given
        """
        s=''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]