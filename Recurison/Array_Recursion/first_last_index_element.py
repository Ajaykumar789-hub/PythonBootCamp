def first_index(l1, x):
    if len(l1) == 0:  ##base case
        return -1
    if l1[0] == x:
        return 0
    ans = first_index(l1[1:], x) 
    if ans == -1:
        return ans
    else:
        return ans + 1

# print(first_index([3,2,5,6], 2))
# print(first_index([3,2,5,6], 7))

def last_index(l1, x):
    if len(l1) == 0:  ##base case
        return -1
    if l1[-1] == x:
        return len(l1) -1
    ans = last_index(l1[:-1], x)
    if ans == -1:
        return ans
    else:
        return ans


print(last_index([3,2,5,2,6], 2))
# print(last_index[3,2,5,6], 7))
