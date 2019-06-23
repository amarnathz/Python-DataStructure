class stack:
    def __init__(self,data):
        self.data=data
        self.next=None

class node:
    def __init__(self):
        self.top=None
        
    def push(self,e):
        element=stack(e)
        element.next=self.top
        self.top=element
        print("%d Pushed Element"%e)

    def top(self):
        print("%d Top value"%(self.top.data))

    def pr(self):
        cur=self.top
        while cur:
            print("%d -> "%cur.data,end="")
            cur=cur.next
            if(cur is None):
                print ("Null")
            
        
    def pop(self):
        cur=self.top
        
        if cur:
            self.top=cur.next
            print("%d poped value"%(cur.data))
        else:
            print("stack is Empty")
        del cur
        




n=node()
n.push(3)
    
        
