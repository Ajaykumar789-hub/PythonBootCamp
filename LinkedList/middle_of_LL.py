from common import *

headOdd = createLLfromList([1,2,3,4,5])
# print_LL(headOdd)

def middleLL(head):
    if head == None or head.next == None:
        return head
    length = length_ll(head)
    middle = length//2
    temp = head
    count = 0
    while(count<middle):
        temp = temp.next
        count += 1
    return temp

headMiddleOdd = middleLL(headOdd)
# print_LL(headMiddleOdd)
# print(headMiddleOdd.data)

##2 pointer approach

def middleLLslowandFast(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow ##slow runs 1 times faster and faster run 2x times, by time fast reach at slow at middle

ans = middleLLslowandFast(headOdd)
print(ans.data)