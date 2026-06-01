class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # ensure length is the same
        if len(s) != len(t):
            return False
        # algorithm
        countS, countT = {}, {} # Hashmaps

        for i in range(len(s)): # iterate through both strings adding chars
            countS[s[i]] = 1 + countS.get(s[i], 0) # map.get(x, 0) -> defaults to 0 if char not already present
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS: # iterate through the maps comparing
            if countS[c] != countT.get(c, 0): # in not equal return false
                return False
        return True # strings have the same length and have the exact same # of each char