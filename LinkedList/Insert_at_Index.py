from common import take_input_better, Node, print_LL
from insert_head_LL import insert_at_head

head = take_input_better()
#print_LL(head)

def insert_at_index(head, data, index):
    if index == 0:
        return insert_at_head(head, data)
    newNode = Node(data)
    temp = head
    count = 0
    while temp is not None and count < index -1 :
        temp = temp.next
        count = count+1

    if temp == None:
        print("Index out of bounds please check index")
        return head
    newNode.next = temp.next
    temp.next = newNode

    return head

head = insert_at_index(head, 100, 3)
print("------------")
print(head)



