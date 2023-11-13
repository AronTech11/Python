# Name = Taluba Aron Hopson
# Student ID = 101747537

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)  # Append data to the end of the list

    def is_empty(self):
        return len(self.stack) == 0

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the last element
        else:
            raise IndexError("Pop from empty stack")

    def traverse(self):
        if not self.is_empty():
            for i in self.stack:
                print("Traverse", i)
        else:
             print("Stack is empty stack")

def main():
    # Creating a stack
    stack = Stack()
    # Pushing data onto the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)

    # Checking the contents of the stack
    print("Pushing:", stack.stack)
    print("Popping:", stack.pop())
    print("Traversing:")
    stack.traverse()
    

if __name__ == "__main__":
    main()

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)  # Append data to the end of the list

    def is_empty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the first element
        else:
            raise IndexError("Dequeue from empty queue")

    def traverse(self):
        if not self.is_empty():
            for i in self.queue:
                print("Traverse", i)           
        else: 
            print("The Queue is Empty Queue")        
            
def main():
    # Creating a queue
    queue = Queue()

    # Enqueuing data into the queue
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4) 
    queue.enqueue(5)
    queue.enqueue(6)
    
    # Checking the contents of the queue
    print("Enqueue:", queue.queue)
    print("Dequeue:", queue.dequeue())
    print("Traverse:")
    queue.traverse()

if __name__ == "__main__":
    main()
