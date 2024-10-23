##recursion
def factorial(n):
    if n==1:
        return 1
    small = factorial(n-1)
    ans = n*small
    return ans
print(factorial(5))


##regular
def reg_factorial(n):
    res = 1
    for i in range(2,  n+1):
        res *= i
    return res

print(reg_factorial(6))