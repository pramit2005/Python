class Stack:
    def __init__(self):
        self.item=[]
    def push(self,data):
        self.item.append(data)
    def pop(self):
        self.item.pop()
    def peek(self):
        return self.item[-1]
    def display(self):
        print(self.item)
s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.pop()
s1.display()