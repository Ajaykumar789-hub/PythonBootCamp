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

def take_input():
    value = int(input("Enter Node value:-"))
    head = None
    while(value != -1):
        NewNode = Node(value)
        if head == None:
            head = NewNode
        else:
            temp = head
            while(temp.next != None):
                temp = temp.next
            
            temp.next = NewNode
        value = int(input("Enter Node value:-"))


    return head

newHead = take_input()
print(print_LL(newHead))

