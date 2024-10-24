
def num_Ofdigits(n):
    if n>=1 and n<=9: ##base case
        return 1
    elif n==0:
        return 1 
    
    smallNum = int(n/10)
    smallans = num_Ofdigits(smallNum) ##assume 2

    ans = 1 + smallans ##step3
    return ans
    
def num_digits(n):
    if n == 0 or (n>=1 and n<=9):
        return 1
    
    smallnum = n//10
    smallans = num_Ofdigits(smallnum)

    return 1 + smallans
print(num_digits(9))
    