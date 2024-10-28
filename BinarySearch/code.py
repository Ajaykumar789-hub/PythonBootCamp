lst = [10, 23, 35, 45, 50, 75, 85]
target = 23
## Hint array is sorted

def binary_search(arr, target):
    size = len(arr)
    start = 0
    end = size - 1
    while(start<=end):
        mid = (start + end)//2
        if(arr[mid]==target):
            return mid ## found target
        elif(arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1 
    return -1

print(binary_search(lst, target=target))

def binary_search_up(arr, target):
    size = len(arr)
    start = 0
    end = size - 1
    while(start<=end):
        mid = start + (start + end)//2
        if(arr[mid]==target):
            return mid ## found target
        elif(arr[mid] > target):
            end = mid - 1
        else:
            start = mid + 1 
    return -1

print(binary_search_up(lst, target=target))