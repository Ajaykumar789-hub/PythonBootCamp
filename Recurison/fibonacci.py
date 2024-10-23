def fibonancci(n):
    if n==0:
        return 1
    if n==1:
        return 1
    last = fibonancci(n-1)
    secondlast = fibonancci(n-2)

    ans = last + secondlast
    return ans

print(fibonancci(4))