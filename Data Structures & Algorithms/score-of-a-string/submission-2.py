class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0
        for i in range(len(s)-1):
            j = i +1
            res += abs(ord(s[i]) - ord(s[j]))

        return res