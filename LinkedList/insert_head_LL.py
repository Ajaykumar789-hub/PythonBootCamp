from common import take_input_better, Node, print_LL

head = take_input_better()

print_LL(head)

def insert_at_head(head, data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return head

head = insert_at_head(head, 100)
print("---------------")
print_LL(head)

##complexity of this O(1)