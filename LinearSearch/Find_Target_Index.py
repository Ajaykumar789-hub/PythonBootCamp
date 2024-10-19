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


