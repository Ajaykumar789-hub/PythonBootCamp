##most imp topic
##we do recurision when solution of problem depend on same smaller problem

##infinite recursive
# def printNum(n):
#     print(n)
#     printNum(n-1)
# printNum(5)

def printNum(n):
    print(n)
    if(n==1):
        return
    printNum(n-1)
