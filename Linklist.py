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
        # node = Node(data, self.head) #Every node is an object
        # self.head = node
        newNode = Node(data)
        if (self.is_Empty()):
            self.head = newNode
            
        
    def print(self):
        if self.head is None:
            print("Linklist is empty")
            return
        
        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
            
        print(llstr)               
    
    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data, None) #Since inserting data at the end, None is pointing to next which is empty
            return
        #LL is no black
        itr = self.head
        
        while itr.next:
            itr = itr.next # itr.next is null means at last element
        itr.next = Node(data,None)
    
    def insert_value(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)        
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next           
        return count
    
    def remove(self,index):
        if index<0 or index >=self.get_length():
            raise Exception("invalid index")
        #Condtion for checking remoiving head
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0 # to maintain the count to remove the index
        
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next # After removing its pointing to the next element of next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self,index,data): 
        if index<0 or index >self.get_length():
            raise Exception("invalid index")
        #Condtion for checking remoiving head
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0 # to maintain the count to insert the index    
        itr = self.head
        while itr:
            if count == index - 1: # when we insert we modify so stopo=ing at previous elememnt
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    
              
               
if __name__ == "__main__":
    
    ll = linkList()
    ll.is_Empty()
    # ll.insert_at_begining(2)
    
    # ll.insert_value(["banana", "Mnago","Apple","Grapes"])
    # ll.insert_end(100)
    # # ll.remove(2)
    # ll.insert_at(0,"Papaya")
    # ll.insert_at(2,"jk")
    
    # ll.print()
    
    # print("Length", ll.get_length())
        