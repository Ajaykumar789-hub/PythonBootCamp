
lst = [12,25,11,34,90,22]
lst2 = [5,4,3,2,1]

# def selection_sort(arr):
#     n = len(arr)

#     min_index = 0
#     for j in range(0, n-1):
#         if(arr[j] < arr[min_index]):
#             min_index = j
#     arr[0], arr[min_index] = arr[min_index], arr[0]

#     return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min_index = i
        for j in range(i+1, n):
            if(arr[j] < arr[min_index]):
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort(lst2))
        
