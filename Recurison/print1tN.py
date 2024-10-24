def print1ToN(n):
    if n<=0:   ##base case question is print 1 to N not from 0
        return
    print1ToN(n-1)
    print(n)

print(print1ToN(5))

def printNTo1(n):
    if n<=0:   ##base case question is print 1 to N not from 0
        return
    print(n)
    printNTo1(n-1)
    

print(printNTo1(5))

