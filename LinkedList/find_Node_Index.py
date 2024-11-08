from common import *

def find_node_index(head, Node):
    if head == None:
        return None
    # if head.data == Node:
    #     return 0
    temp = head
    count = 0
    while temp:
        if temp.data == Node:
            return count
        temp = temp.next
        count += 1
    return -1
head = createLLfromList([2,3,4,5,6])
print(find_node_index(head, 7))