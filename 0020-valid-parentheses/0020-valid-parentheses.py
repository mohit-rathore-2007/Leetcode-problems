class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for brac in s:
            if brac in "([{":
                stack.append(brac)
            else:
                if not stack:
                    return False 

                top = stack.pop()
                if brac == ")" and top != "(":
                    return False
                elif brac == '}' and top !="{":
                    return False 
                elif brac == ']' and top !="[":
                    return False
        return len(stack) == 0
