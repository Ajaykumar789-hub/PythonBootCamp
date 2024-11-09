from common import *
head = createLLfromList([1,2,3,4,5,6,5,4,3,2,1])
head2 = createLLfromList([1,2,3,4])
def revers_ll(head):
    if head == None or head.next == None:
        return head
    current = head
    prev = None
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

def palindrome_LL(head):
    if head == None or head.next == None:
        return True
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = revers_ll(slow)
    while second:
        if second.data != head.data:
            return False
        second = second.next
        head = head.next
    return True
print(palindrome_LL(head))
print(palindrome_LL(head2))
# head = revers_ll(head2)
# print_LL(head)
    