lst = [3,67,4, 10, 70, 89]
target = 70
## Return Index of targe, Ans: 4

def linear_search(arr, target):
    size = len(arr)
    for i in range(0, size):
        if arr[i]==target:
            return i
    return -1

print(linear_search(lst, target=target))

lst2 = [1,2,3,3,4,5]
tr = 3

def last_occ(lst, target):
    n = len(lst)
    for i in range(n-1, 0, -1):
        if lst[i] == target:
            return i
    return -1

print(last_occ(lst2, tr))


