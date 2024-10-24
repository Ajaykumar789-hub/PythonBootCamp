def sum_of_array(lst):
    # if len(lst) == 1:
    #     return lst[0]
    if len(lst) == 0:
        return 0
    ans = sum_of_array(lst[1:])
    return lst[0] + ans

print(sum_of_array([2,3,4,5]))

def sum_of_array_tail(lst, accumulator=0):
    if len(lst) == 0:
        return accumulator
    accumulator += lst[0]

    return sum_of_array_tail(lst[1:], accumulator)

print(sum_of_array_tail([2,3,4,5,6]))