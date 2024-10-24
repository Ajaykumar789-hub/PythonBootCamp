def check_array_sorted(lst):  ##Head method
    if len(lst)==1 or len(lst)==0:  ##base case
        return True
    ans = check_array_sorted(lst[1:]) 
    if lst[0] < lst[1]: ##m y work
        return ans
    else:
        return False
    
print(check_array_sorted([2,5,7,9,10]))   

def check_array_sorted_tail(lst):
    if len(lst)==1 or len(lst)==0:  ##base case
        return True
    if lst[0] >= lst[1]:
        return False
    return check_array_sorted(lst[1:])

print(check_array_sorted_tail([2,5,7,9,10]))  