class Node:
    
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    
    def __init__(self):
        self.head=None
        
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def insert_at_ending(self,data):
        if self.head is None:
            self.head=Node(data)
            return 
        
        itr=self.head
        while itr.next:
            itr=itr.next
            
        itr.next=Node(data,None)
        
    def insert_at_position(self,data,pos):
        if self.head is None:
            self.head=Node(data)
            return
        if pos==0:
            self.insert_at_beginning(data)
            return
        if pos>=self.get_length():
            self.insert_at_ending(data)
            return
        
        count=0
        itr=self.head
        while itr.next:
            if count==pos-1:
                itr.next=Node(data,itr.next)
                break
            itr=itr.next
            count+=1
        
    def delete_at_beginning(self):
        if self.head is None:
            print("Empty list")
            return
        self.head=self.head.next
        
    def delete_at_ending(self):
        if self.head is None:
            print("Empty list")
            return
        
        itr=self.head
        while itr.next.next:
            itr=itr.next
        itr.next=None
        
    def delete_at_position(self,pos):
        if self.head is None:
            print("Empty list")
            return
        if pos==0:
            self.head=self.head.next
            return
        if pos>=self.get_length():
            self.delete_at_ending()
            return
        
        count=0
        itr=self.head
        while itr.next:
            if count==pos-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
            
            
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count            
    
    def print(self):
        
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr=self.head
        llstr=''
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.next    
        print(llstr)
        
ll=LinkedList()
ll.insert_at_ending(50)
ll.insert_at_beginning(70)
ll.insert_at_ending(90)
ll.print()
ll.delete_at_position(1)
ll.print()
print("Length:",ll.get_length())
