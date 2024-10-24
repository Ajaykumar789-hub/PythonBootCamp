def sum_of_digits(n):
    if n==0: ##base case
        return 0
    smallnum = int(n//10)
    smallans = sum_of_digits(smallnum)
    ans = n%10 + smallans

    return ans

print(sum_of_digits(12))

    