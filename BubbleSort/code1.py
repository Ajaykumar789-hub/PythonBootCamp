lst = [12, 25, 11, 34, 90,22]
lst2 = [5,4,3,2,1]

def bubble_sort(arr):
    n = len(arr) ## 6

    for passes in range(0, n):
        for j in range(0, n-1-passes):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(arr=lst2))