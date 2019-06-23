class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class circularlist(object):
    def __init__(self, head=None):
        self.head = head
        

    def append(self,new_e):
        
        if self.head is not None:
            cur=self.head
            
            while cur.next:
                
                cur=cur.next
                if(cur.next == self.head):
                    break
            cur.next=new_e
            
            new_e.next=self.head
        else:
            
            self.head=new_e
            
        
    def add(self,new_e,pos):
        if pos == 1:
            new_e.next=self.head
            tem=self.head
            cur=tem
            self.head=new_e
            
            while cur:
                
                if (cur.next == tem):
                    cur.next=self.head
                    break
                cur=cur.next
            
        else:
            tem=self.head
            c=1
            while tem.next and c<=pos-2 :
                if(tem.next ==self.head):
                    self.append(new_e)
                    break
                tem=tem.next
                c+=1
            cur=tem.next
            tem.next=new_e
            new_e.next=cur
                    
                
                
    def dele(self,new_e):
        
        cur=self.head
        if (cur.value==new_e):
            self.head=cur.next
            tem=self.head
            
            while tem:
                
                if (cur.value == tem.next.value):
                    tem.next=self.head
                    break
                tem=tem.next
        else:
            while cur:
                if(cur.next.next==self.head and cur.next.value == new_e):
                    tem=cur.next
                    cur.next=self.head
                    
                    del tem
                    break
                else:
                    if(cur.next.value == new_e):
                        tem=cur.next.next
                        pre=cur.next
                        cur.next=tem
                        del pre
                        break
                cur=cur.next        
        
        
    def pr(self):
        print("Printing Elments :")

        if self.head is not None:
            cur=self.head
            
            while True:
                print(cur.value)
                
                if(cur.next == self.head):
                    break
                cur=cur.next
            
        else :
            
            return None


n=circularlist()
n.append(Element(23))
n.append(Element(233))
n.append(Element(2133))
n.add(Element(451),1)
n.pr()
