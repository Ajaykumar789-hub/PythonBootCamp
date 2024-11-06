from common import take_input_better, Node, print_LL

head = take_input_better()

print_LL(head)

def insert_at_tail(head, data):
    newNode = Node(data)

    if head == None:
        return newNode
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = newNode

    return head

# head = insert_at_tail(head, 100)
# print("---------------")
# print_LL(head)


def inser_at_tail_rec(head, data):
    
    if head == None:
        newNode = Node(data)
        return newNode
    if head.next == None:
        newNode = Node(data)
        head.next = newNode
        return head
    head.next = inser_at_tail_rec(head.next, data)
    return head

head = inser_at_tail_rec(head, 100)
print("recursion---------------")
print_LL(head)