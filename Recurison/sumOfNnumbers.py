def sum_numbers(n):
    if n==1:
        return 1
    return n + sum_numbers(n-1)
print(sum_numbers(5))

##Regular
def reg_sum_numbers(n):
    res = 1
    for i in range(2, n+1):
        res += i
    return res
print(reg_sum_numbers(5))

