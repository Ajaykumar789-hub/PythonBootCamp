from common import take_input_better, Node, print_LL

head = take_input_better()

def delet_tail(head):
    if head == None or head.next == None:
        return None
    temp = head
    while(temp.next.next is not None):
        temp = temp.next
    temp.next = None
    return head
# head = delet_tail(head)
# print_LL(head)


def delete_tail_rec(head):
    if head == None or head.next == None:
        return None
    head.next = delete_tail_rec(head.next)
    return head
head = delete_tail_rec(head)
print_LL(head)