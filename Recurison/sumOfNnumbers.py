import sys
sys.getrecursionlimit(10000) ##to set recursion limit

def sum_numbers(n):
    if n==1: ##base case
        return 1
    smallAns = sum_numbers(n-1) ##Assume2
    ans = n+smallAns
    return ans
print(sum_numbers(5))

##Regular
def reg_sum_numbers(n):
    res = 1
    for i in range(2, n+1):
        res += i
    return res
print(reg_sum_numbers(5))

