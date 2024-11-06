from common import take_input_better, Node, print_LL

head = take_input_better()

def delete_head(head):
    if head == None:  ## if head is empty
        return None
    newhead = head.next
    return newhead

head = delete_head(head)
print_LL(head)