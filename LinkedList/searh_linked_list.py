from common import take_input_better, Node, print_LL

head = take_input_better()

def search_by_value(head, value):
    temp = head
    index = 0

    while temp != None:
        if temp.data == value:
            return index
        temp = temp.next
        index += 1
    return -1

print(search_by_value(head, 30))

def search_by_value_rec(head, value):
    if head == None:
        return None
    if head.data == value:
        return 