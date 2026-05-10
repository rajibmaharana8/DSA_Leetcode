class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        for char in s:
            if char in '([{':
                stack.append(char)
            else:
                if len(stack) ==0:
                    return False
                
                ch = stack.pop()

                if ch == "(" and char == ")" or ch == "[" and char == "]" or ch == "{" and char == "}":
                    continue
                else:
                    return False
            
        if (len(stack))!=0:
            return False
        else:
            return True