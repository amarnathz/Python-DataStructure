T=int(input())
for i in range(T):
    a=int(input())
    p=2
    l=[True for i in range(a+1)]
    while(p * p <=a):
        if(l[p]==True):
            for i in range(p*p,a+1,p):
                l[i]=False
        p+=1    
    for p in range(2,a+1):
        if (l[p]==True):
            print(p,end=" ")
            
            

        
        
        
