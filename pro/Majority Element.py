def f(a,n):
    ma=0
    w=0
    for i in range(0,n):
        c=1
        for j in range(i+1,n):
            if(a[i]==a[j] ):
                c+=1
        if(ma<c):
            ma=c
            w=i
            
            
    if(ma>n/2):
        return(a[w])
    else:
        return (-1)
    
T=int(input())
for i in range(T):
    n=int(input())
    
    a=list(map(int,input().split() ))
    print(f(a,n))
   #time complexity :O(n*n)
"""
--------------------Hash map---------------------------
def f(k,d):
    myMap = {}
    m=0
    i=0
    for n in k:
        if n in myMap:
            myMap[n] += 1
            
        else:
            myMap[n] = 1
            
        if myMap[n] > m:
            m = myMap[n]
            i=n
    
    if(m>d/2):
        return(i)
    else:
        return (-1)    
    
T=int(input())
for i in range(T):
    n=int(input())
    
    a=list(map(int,input().split() ))
    print(f(a,n))
   
time complexity :O(n)
"""
