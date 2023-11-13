class Node:
   def __init__(self, data = None, next = None):
       self.data = data
       self.next = next
       
class LinkedList:
    def __init__(self) -> None:
        self.head = None
     
    def insert_data_begining(self,data):
        node = Node(data, self.head)
        self.head = node
        
    def Print_Linked_list_element(self):
        if self.head is None:
            print("Empty Linklist")
            
        current = self.head
        llstr = " " 
        
        while current:
            llstr += str(current.data) + "-->" #apend to the next data
            current = current.next
        print(llstr)
        
    def insert_data_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None) #if empty it directly sets a head
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data, None) #new node is added 
            
    def insert_value(self,datalist):
        self.head = None
        for data in datalist:
            self.insert_data_at_end(data)
    
                
    def get_length(self):
        count = 0
        current = self.head
        
        while current:
            count +=1
            current = current.next
        return count
                  
    def remove(self,index):
        if index < 0 or 0>= self.get_length():
            print("invalid Index")
            
        if index == 0:
            self.head = self.head.next
            return  
        
        count = 0
        
        current = self.head
        
        while current:
            if count == index -1:
                current.next = current.next.next
                break
            current = current.next
            count +=1 
            
    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next
        
    
    def insert_in_betwwen(self, index,data):
        if index<0 or 0>=self.get_length():
            print("Invalid index")
            
        if index == 0:
            self.insert_data_begining(data)
            return
        
        count = 0
        current = self.head
        
        while current:
            if count == index - 1:
                node = Node(data, current.next)
                current.next = node
                break
            current = current.next
            count +=1
                
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
            
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        current = self.head
        
        while current:
            if current.data == data_after:
                current.next = Node(data_to_insert, current.next)
                break
            current = current.next
            
            
            
                                    
       
def main():
    ll = LinkedList()
   
    ll.insert_value(["a","b","c","d"])
    ll.insert_data_begining(1)
    ll.insert_data_begining(2) 
    ll.insert_data_at_end(89)
    ll.insert_after_value("b","pol")
    ll.remove_by_value("d")
    # ll.remove(2)
    ll.insert_in_betwwen(2,"Amazing")
    ll.Print_Linked_list_element()
   
    
    print(ll.get_length(),"Length")
   
    
    
   
    

if __name__ == "__main__":
    main()         
           
        
    