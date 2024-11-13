'''
Problem statement You're given a string 'S' consisting of "{", "}", "(", ")", "[" and "]" . 
Return true if the given string 'S' is balanced, else return false. 
For example: 'S' = "{}()". 
There is always an opening brace before a closing brace i.e. '{' before '}', '(' before '). 
So the 'S' is Balanced.
'''

def is_Balenced(S):
    stack = []
    matching_brace = {')': '(', '}': '{', ']': '['}
    for char in S:
        if char in matching_brace.values():
            stack.append(char)
        elif char in matching_brace.keys():
            # If the character is a closing brace, check if it matches the top of the stack
            if not stack or stack.pop() != matching_brace[char]:
                return False
        else:
            # If the character is not a brace, return False (invalid input)
            return False
    return len(stack) == 0
s = "{}()"
print(is_Balenced(s))