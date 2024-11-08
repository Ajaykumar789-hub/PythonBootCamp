from common import *

head1 = createLLfromList([2,5,9,10,17])
head2 = createLLfromList([3,6,7])

def two_merge_sorted_LL(h1,h2):
    if h1 == None:
        return h2
    if h2 == None:
        return h1
    
    finalHead = None
    finalTail = None
    while h1 != None and h2 != None:
        if h1.data < h2.data:
            if finalHead == None:
                finalHead = h1
                finalTail = h1
            else:
                finalTail.next = h1
                finalTail = h1
            h1 = h1.next
        else:
            if finalHead == None:
                finalHead = h2
                finalTail = h2
            else:
                finalTail.next = h2
                finalTail = h2
            h2 = h2.next
        if h1 != None:
            finalTail.next = h1
        if h2 != None:
            finalTail.next = h2
    
    return finalHead

finalHead = two_merge_sorted_LL(head1, head2)

print_LL(finalHead)
