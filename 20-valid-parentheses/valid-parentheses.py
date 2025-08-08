class Solution:
    def isValid(self, s: str) -> bool:

        #notes 
        #done with LIFO Last-In, First-Out in py we can use list as our stack
        #see opening bracket -> push top of stack remember its "open" -> see closing bracket -> check if matches open bracket -> pop top iten 
            # stack order as its seen -- 1 - (, 2 - [, 3 - )
            # top of stack (, then [, then ) but it dosn't match top so false 
        #create empty list which will represent the stack 
        #loop through the string looking at the characters seeing if they are one of our wanted brackets
        #if it is then push the char to stack list append.stack(our bracket char)
        #check 1 -- elif we see a closing bracket so lets first see if the stack is empty if it is then return False
        #check 2 -- if the stack is not empty then we pop the top item of the stack. which should be the most recent open bracket
        #we then should check if the popped opening bracket is the pair for the current closed bracket
        #if the brackets do not match the string should be False as it will be invalid
        #when the loop finishes we should look if the stack is empty which sgould mean every opening bracket had a match so the string is valid so return True
        #if the stack is not empty then there is some unmatches the string is invalid so return False

        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)

            elif char in ")}]":
                if not stack: 
                    return False
                else:
                    last_opened = stack.pop()
                    if (last_opened == '(' and char != ')') or \
                       (last_opened == '{' and char != '}') or \
                       (last_opened == '[' and char != ']'):
                        return False

        if not stack: 
            return True
        else:
            return False





