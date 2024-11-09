class StackList:
    def __init__(self):
        self.__stack = []
    def push(self,data):
        self.__stack.append(data)
        print(f"pushed {data} into stack")
    def size(self):
        return len(self.__stack)
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    def top(self):
        if self.is_empty():
            print("stack is empty")
            return None
        return self.__stack[-1]
    def pop(self):
        if(self.is_empty()):
            print("stack is empty")
            return None
        return self.__stack.pop()

myStack = StackList()

print(myStack.push(1))
print(myStack.push(2))
print(myStack.push(3))
print(myStack.is_empty())  
print(myStack.size())  
print(myStack.top())   
print(myStack.pop())
print(myStack.pop())


        
