class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class QueueUsingLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    def size(self):
        return self.len
    def isEmpty(self):
        return self.len == 0
    def enqueue(self, data):
        newNode = Node(data)
        self.len += 1
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return f"added {data} to queue"
    def front(self):
        if self.isEmpty():
            print("quueue is empty")
            return None
        return self.head.data
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return None
        self.len -= 1
        dataToReturn = self.head.data
        self.head = self.head.next
        if self.head == None:
            self.tail = None
        return dataToReturn
    
Q = QueueUsingLL()

print(Q.enqueue(3))
print(Q.enqueue(30))
print(Q.enqueue(300))
print(Q.isEmpty())
print(Q.size())
print(Q.dequeue())
print(Q.isEmpty())
print(Q.size())

    