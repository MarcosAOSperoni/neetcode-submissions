class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        stack = []
        matches = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in matches:
                if stack and stack[-1] == matches[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack