class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
def print_LL(head):
    temp = head
    while(temp!=None):
        print(temp.data, end='->')
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

# newHead = take_input_better()
# print(print_LL(newHead))

def createLLfromList(l1):
    head = None
    tail = None
    for value in l1:
        newNode = Node(value)
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head
def length_ll(head):
    temp = head
    ans = 0
    while(temp != None):
        temp = temp.next 
        ans += 1
    return ans

