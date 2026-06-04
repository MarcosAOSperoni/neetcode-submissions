class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        for i in range(len(s)):
            j = len(s) - 1 - i
            if s[i] != s[j]:
                return False
        return True