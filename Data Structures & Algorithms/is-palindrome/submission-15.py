class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        front = 0
        back = len(lower) - 1
        while (front < back):
            if not lower[front].isalnum():
                front += 1
            elif not lower[back].isalnum():
                back -= 1
            else:
                if lower[front] != lower[back]:
                    return False
                front += 1
                back -= 1
        return True
