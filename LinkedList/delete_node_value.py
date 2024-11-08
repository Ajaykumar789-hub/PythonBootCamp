from common import take_input_better, Node, print_LL

head = take_input_better()

def delete_node_by_value(head, value):
    if head == None:
        return None
    if head.data == value: # when head is value
        return head.next
    temp = head

    while temp.next != None and temp.next.data != value:
        temp = temp.next
    if temp.next == None:
        print("value not present")
        return head
    temp.next = temp.next.next
    return head

head = delete_node_by_value(head, 3)
print_LL(head)