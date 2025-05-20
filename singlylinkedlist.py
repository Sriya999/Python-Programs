class Node:
    def __init__(self,val):
        self.data=val
        self.nxt=None

class singlell:
    def __init__(self):
        self.head=None
        
    def insert(self,element):
        newnode=Node(element)
        
        if self.head==None:   #list is empty
            self.head=newnode
        else:
            crnt=self.head
            while crnt.nxt!=None:
                crnt=crnt.nxt
            crnt.nxt=newnode
            
    def  insert_atbeg(self,element):
        newnode=Node(element)
        if self.head==None:
            self.head=newnode
        else:
            newnode.nxt=self.head
            self.head=newnode
            
    def del_at_beg(self):
        if self.head==None:
            print("List is Empty")
        else:
            curr=self.head
            self.head=curr.nxt
            print(curr.data,"deleted")
            del curr
    def del_at_last(self):
        if self.head==None:
            print("List is Empty")
        else:
            curr=self.head
            while curr.next.next!=None:
                curr=curr.nxt
            curr.next=None
    def dellast(self):
        if self.head is None:
            print("list is empty")
        elif self.head.nxt==None:
            print(self.head.data,"deleted,list is nw empty")
            self.head=None
        else:
            prev=self.head
            curr=self.head.nxt
            while curr.nxt!=None:
                prev=curr
                curr=curr.nxt
            print(curr.data,"deleted")
            prev.nxt=None
    def search_Element(self,t):
        if self.head==None:
            print("list is empty ....No element to search")
            return
        curr=self.head
        while curr:
            if curr.data==t:
                print("Node with data",t,"Element Found in the list")
                return
            curr=curr.nxt
        print("Node with data",t,"not found")
            
        
    def display(self):
        if self.head is None:
            print("List Empty")
        else:
            curr=self.head
            while curr:
                print(curr.data)
                curr=curr.nxt
    def insert_before_node(self,val,key):
        if self.head==None:
            print("ll is empty,insertion not possible")
        else:
            newnode=Node(val)
            curr=self.head
            if curr.data==key:
                newnode.nxt=self.head
                self.head=newnode
            else:
                curr=self.head
                while curr.nxt and curr.nxt.data!=key:
                    curr=curr.nxt
                if curr.nxt:
                    newnode.nxt=curr.nxt
                    curr.nxt=newnode
                else:
                    print("Node vth data ",key,"not found")
    def insert_after_node(self, value, key):
        if self.head is None:
            print("List is empty")
        else:
            newnode = Node(value)
            current = self.head
            while current:
                if current.data == key:
                    newnode.nxt = current.nxt
                    current.nxt = newnode
                    return
                current = current.nxt
            else:
                print("Node with data", key, "not found")
    def insert_at_pos(self,val,key):
        if key<0:
            print("Invalid Position")
            return
        newnode=Node(val)
        if key==0:
            newnode.nxt=self.head
            self.head=newnode
            return
        curr=self.head
        idx=0
        while curr and idx<key-1:
            curr=curr.nxt
            idx+=1
        if curr is None:
            print("pos out of bounds")
        else:
            newnode.nxt=curr.nxt
            curr.nxt=newnode
    
    def delete_before_node(self,key):
            if self.head is None:
                print("LL is empty")
            else:
                if self.head.nxt is None:
                    print("List has only one element")
                elif self.head.nxt.data==key:
                    self.head=self.head.nxt
                else:
                    prev=self.head
                    curr=prev.nxt
                    while curr.nxt and curr.nxt.data!=key:
                        prev=curr
                        curr=curr.nxt
                    if curr.nxt:
                        print(curr.data,"deleted")
                        prev.nxt=curr.nxt
                    else:
                        print("Key Element not Found")
                        
    def delete_after_node(self,key):
        if self.head==None:
            print("LL is Empty")
        else:
            if self.head.nxt is None:
                print("List has only one element,not possible")
            else:
                curr=self.head
                while curr and curr.data!=key:
                    curr=curr.nxt
                if curr and curr.nxt:
                    curr.nxt=curr.nxt.nxt
                else:
                    print("Key Element not found in list or Last Element")
                    
    def reverse(self):
        if self.head is None:
            print("List is empty")
        else:
                prev = None
                current = self.head
                while current:
                    next_node = current.nxt
                    current.nxt = prev
                    prev = current
                    current = next_node
                self.head = prev
                 

sll=singlell()
while True:
    print("1.insert at last   2.Display   3.insert at beginning   4.delete at beg   5.delete at last   6.Element to search    7.insert before a node   8.insert after a node  9.insert at position  10.delete before node  11  delete after a node   12.Reverse  13.exit")
    ch=int(input())
    if ch==1:
        ele=int(input("Enter Element"))
        sll.insert(ele)
    elif ch==2:
        sll.display()
    elif ch==3:
        ele=int(input("Enter Element"))
        sll.insert_atbeg(ele)
    elif ch==4:
        sll.del_at_beg()
    elif ch==5:
        sll.del_at_last()
    elif ch==6:
        ele=int(input("Enter Element to search"))
        sll.search_Element(ele)
    elif ch==7:
        val=int(input("Enter Element"))
        key=int(input("Enter before node"))
        sll.insert_before_node(val,key)
    elif ch==8:
        val=int(input("Enter Element"))
        key=int(input("Enter after node"))
        sll.insert_after_node(val,key)
    elif ch==9:
        val=int(input("Enter Element"))
        key=int(input("Enter the position"))
        sll.insert_at_pos(val,key)
    elif ch==10:
        pos=int(input("enter to delete before node"))
        sll.delete_before_node(pos)
    elif ch==11:
        key=int(input("Enter after node Element to delete:"))
        sll.delete_after_node(key)
    elif ch==12:
        sll.reverse()
    elif ch==13:
        break
    



         
