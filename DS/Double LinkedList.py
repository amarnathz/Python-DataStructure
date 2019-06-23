class element:
    def __init__(self,data=None):
        self.next=None
        self.data=data
        self.pre=None


class Node:
    def __init__(self,head=None):
        self.head=head
       # print forward and reverves [last]
       self.last=None

    def forward(self):
        cur=self.head
        while cur:
            print(cur.data)
            self.last=cur
            cur=cur.next
                        
    def reverse(self):
        if self.last == None:
            forward()
        cur=self.last    
        while (cur):
            print(cur.data)
            cur=cur.pre        
        
    def push(self,new_e):
        
    
        if self.head :
            
            cur=self.head
            while cur.next:
                cur=cur.next
                
            cur.next=new_e
            new_e.pre=cur
        else:
            self.head=new_e
            
    def insert(self,new_e,pos):
        cur=self.head
        if pos>1 :
            for i in range(1,pos-1):
                cur=cur.next
            temp=cur.next
            cur.next=new_e
            new_e.pre=cur
            new_e.next=temp
            temp.pre=new_e

        elif(pos==1):
            
            self.head=new_e
            new_e.next=cur
            cur.pre=new_e
            
    def delete(self,num):
        cur=self.head
        
        while cur:
            if (cur.data == num):
                
                if(cur.pre==None):
                    
                    temp=cur.next
                    self.head=temp
                    del temp
                    return 0
                elif(cur.next==None):
                    
                    temp=cur.pre
                    temp.next=None
                    del cur
                    return 0
                else:
                    
                    tem=cur.pre
                    tem1=cur.next
                    tem.next=tem1
                    tem1.pre=tem
                    del cur
                    return 0
                
            cur=cur.next    
                




e1=element(3)
e2=element(4)
e3=element(6)
e4=element(7)
n=Node()
n.push(e1)
n.push(e2)
n.push(e4)
##n.forward()
##n.reverse()
n.insert(e3,2)
##n.forward()
n.delete(6)
n.forward()

