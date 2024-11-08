from common import take_input_better, Node, print_LL

head = take_input_better()

def delete_at_index(head, index):
    if head == None:
        return head
    if index == 0:
        return head.next
    temp = head
    count = 0
    while(temp != None and count < index-1):
        temp = temp.next
        count += 1
    if temp == None or temp.next == None:
        print("out of bounds")
        return head
    temp.next = temp.next.next
    return head

# head = delete_at_index(head, 3)
# print_LL(head)

def delet_at_index_rec(head, index):
    if head == None:
        print("out of bounds")
        return None
    if index == 0:
        return head.next
    head.next = delet_at_index_rec(head.next, index-1)

    return head

head = delet_at_index_rec(head, 3)
print_LL(head)