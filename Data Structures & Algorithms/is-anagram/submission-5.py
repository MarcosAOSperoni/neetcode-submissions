class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check that the sizes are the same
        if len(s) != len(t):
            return False
        # Make dicts that count the number of letters
        countT, countS =  {} , {}
        for i in range(len(s)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)
        # Compare counts
        for c in countT:
            if countT[c] != countS.get(c, 0):
                return False

        return True