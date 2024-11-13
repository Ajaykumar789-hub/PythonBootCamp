

def reverse_array(s,n):
    stack = []
    for i in range(n):
        stack.append(s[i])
    reverse_stack = []
    while stack:
        reverse_stack.append(stack.pop())
    return reverse_stack

s = [1,2,3,4]
print(reverse_array(s,4))