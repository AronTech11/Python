# Name = Taluba Aron Hopson
# Student ID = 101747537

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkList:
    def __init__(self): #it shows an empty linklist
        self.head = None #it has a single attribute head which is set to None, which shows Linklist is empty at innitial
    
    def is_Empty(self):
        if self.head is None:
            print("Linklist is empty")
            return
        
    def insert_at_begining(self,data):
        node = Node(data, self.head) #Every node is an object
        self.head = node
        
        # newNode = Node(data)
        # if (self.is_Empty()):
        #     self.head = newNode
        # else: 
        #     newNode.next = self.head
        #     self.head = newNode 
            
        
    def traverse(self):
        self.is_Empty()
        
        current = self.head
        linklistString = " "
        
        while current:
            linklistString += str(current.data) + '-->'
            current = current.next
        print(linklistString)                     
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next           
        return count
    
    def remove_head(self):
        if not self.head:
            print("Linked list is empty. Nothing to remove.")
            return
        self.head = self.head.next
    
    
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data, None) #Since inserting data at the end, None is pointing to next which is empty
            return
        #LL is no black
        current = self.head
        
        while current.next:
            current = current.next # current.next is null means at last element
        current.next = Node(data,None) 
          
               
if __name__ == "__main__":
    
    ll = linkList()
    # ll.is_Empty()
    ll.insert_at_begining(1)
    ll.insert_at_begining(2)
    ll.insert_at_begining(3)
    ll.traverse()
    
    ll.remove_head()
    ll.insert_end(100)
    
    ll.traverse()
    print("Length", ll.get_length())
        