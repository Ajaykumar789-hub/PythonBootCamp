def indexHelper(l1, x, index):
    if len(l1) == index:
        return 
    if l1[index] == x:
        print(index)
    indexHelper(l1, x, index+1)

def printAllIndex(l1,x):
    indexHelper(l1,x, 0)

print(printAllIndex([3,2,5,6,2,7,8,2],2))
