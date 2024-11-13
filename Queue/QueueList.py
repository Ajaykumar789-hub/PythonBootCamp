class QueueList:
    def __init__(self):
        self.__queue = []
    def size(self):
        return len(self.__queue)
    def isEmpty(self):
        return len(self.__queue) == 0
    def enqueue(self,data):
        self.__queue.append(data)
        return f"added {data} to queue"
    def front(self):
        if self.size() == 0:
            print("queue is empty")
            return None
        return self.__queue[0]
    def dequeue(self):
        if self.size() == 0:
            print("queue is empty")
            return None
        return self.__queue.pop(0)
    
Q = QueueList()

print(Q.enqueue(3))
print(Q.enqueue(30))
print(Q.enqueue(300))
print(Q.isEmpty())
print(Q.size())
print(Q.dequeue())
print(Q.isEmpty())
print(Q.size())