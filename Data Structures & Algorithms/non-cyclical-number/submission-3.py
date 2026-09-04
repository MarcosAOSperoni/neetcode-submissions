class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        square = 0
        curr = n
        while square != 1:
            square = 0
            while curr > 0:
                square += (curr%10)**2
                curr //=  10
            if square in seen:
                return False
            seen.add(square)
            curr =square
        return True
                

