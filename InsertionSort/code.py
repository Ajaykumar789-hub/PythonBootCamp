lst = [12,25,11,34,90,22]
lst2 = [5,4,3,2,1]

def insertion_sort(arr):
    n = len(arr)
    for current in range(1,n):
        currentCard = arr[current]
        currentPosition = current -1
        while currentPosition >=0:
            if(arr[currentPosition] < currentCard):
                break
            else:
                arr[currentPosition+1] = arr[currentPosition]
                currentPosition -= 1
            arr[currentPosition +1] = currentCard
    return arr



print(insertion_sort(lst))

print(insertion_sort(lst2))
