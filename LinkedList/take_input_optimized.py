class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data)
        temp = temp.next
    return

def take_input_better():
    value = int(input("Enter Node value:-"))
    head = None
    tail = None
    while(value != -1):
        NewNode = Node(value)
        if head == None:
            head = NewNode
            tail = NewNode
        else:
            tail.next = NewNode
            tail = NewNode
        value = int(input("Enter Node value:-"))


    return head

newHead = take_input_better()
print(print_LL(newHead))

