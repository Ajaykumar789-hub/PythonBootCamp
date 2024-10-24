def pow_of_num(base, expo):
    if expo == 0 or base ==0:
        return 1
    smallans = pow_of_num(base, expo-1)
    ans = base*smallans
    return ans

print(pow_of_num(3,3))
    
    