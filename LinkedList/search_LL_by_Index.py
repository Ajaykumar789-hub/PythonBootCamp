from common import take_input_better, Node, print_LL

head = take_input_better()

def search_LL_index(head, index):
    if index == 0:
        return head.data
    temp = head
    count = 0
    while temp is not None and count < index-1:
        temp = temp.next
        count += 1
    if temp is None or temp.next is None:
        return -1
    return temp.next.data

print(search_LL_index(head, 5))
