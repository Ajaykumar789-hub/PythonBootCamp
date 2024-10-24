def haedfact(n):
    if n == 0:
        return 1
    smallans = haedfact(n-1)
    ans = n*smallans
    return ans

print(haedfact(4))


def tailfact(n, accumaltor=1):
    if n==0:
        return accumaltor
    accumaltor = accumaltor * n
    return tailfact(n-1, accumaltor)

print(tailfact(4))