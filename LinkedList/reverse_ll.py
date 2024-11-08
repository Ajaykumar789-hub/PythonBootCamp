from common import *

head = createLLfromList([2,3,4,5,6])

def reverse_ll(h):
    if h == None or h.next == None:
        return h
    smallhead = reverse_ll(h.next)

    temp = smallhead
    while temp.next != None:
        temp = temp.next
    temp.next = h
    h.next = None
    return smallhead

# smallhead = reverse_ll(head)
# print_LL(smallhead)

def reverse_ll_better(h):
    if h == None or h.next == None:
        return h
    smallhead = reverse_ll_better(h.next)
    temp = h.next
    temp.next = h
    h.next = None

    return smallhead

# smallhead = reverse_ll_better(head)
# print_LL(smallhead)

def reverse_ll_tail(h):
    if h == None or h.next == None:
        tail = h
        return h, tail
    smallhead, tail = reverse_ll(h.next)

    temp = smallhead
    # while temp.next != None:
    #     temp = temp.next
    temp.next = h
    h.next = None
    return smallhead

# smallhead = reverse_ll_tail(head)
# print_LL(smallhead)

def reverse_LL_Iteration(head):
    if head == None or head.next == None:
        return head
    current = head
    prev = None
    while current != None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
print("better iteration")
smallhead = reverse_LL_Iteration(head)
print_LL(smallhead)
