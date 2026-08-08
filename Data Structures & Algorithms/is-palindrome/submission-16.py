class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower=s.lower()
        l, r = 0, len(s)-1
        while l < r:
            #print(f"r = {lower[r]} l = {lower[l]}")
            if not lower[l].isalnum():
                l += 1
            elif not lower[r].isalnum():
                r -= 1
            elif lower[r] != lower[l]:
                return False
            else:
                l += 1
                r -= 1
        return True