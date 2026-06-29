class Solution:
    def isValid(self, s: str) -> bool:

    
        opening = "{(["
        closing = "])}"

        stack = []

        for letter in s:
            
            if letter in opening:
                stack.append(letter)
            
            elif letter in closing:
                if len(stack) > 0:
                    if letter == "}" and stack[-1] == "{":
                        stack.pop()
                    elif letter == ")" and stack[-1] == "(":
                        stack.pop()
                    elif letter == "]" and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(stack) == 0:
            return True
        
        return False
