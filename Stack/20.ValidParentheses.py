class Solution:
    def isValid(self, s: str) -> bool:
        BracketsToClose = {
            '}':'{',
            ']':'[',
            ')':'(',
        }

        stack = []

        for i in s:
            if i in BracketsToClose:
                if not(stack and (stack.pop()==BracketsToClose[i])):
                    return False
            else:
                stack.append(i)

        return not stack
                
                
