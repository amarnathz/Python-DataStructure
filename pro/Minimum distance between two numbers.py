import os
os.system('clear')
def minDist(arr, n, x, y):
    op=100000
    for i in range(0,n):
        for j in range(i+1,n):
            if( ((x== arr[i] and y==arr[j] )or(x== arr[j] and y==arr[i] )) and op>abs(i-j) ):
                print(op) 
                op=abs(i-j)
                
    if(op==100000):
        return -1
    else:
        return op
                
        
T=int(input())
for i in range(T):
    n=int(input())
    a=list(map(int,input().split() ))
    s,e=map(int,input().split() )
    
    
    
    print(minDist(a,n,s,e))        
            
            

















        
    
    
"""
for x1 in range(n):
        if (x == arr[x1] or c>=1 or y ==arr[x1]):
            
        
            if( (y==arr[x1] or x ==arr[x1] )and c>=1):
                return c
                break
            if(x==arr[x1]):
                x=0
            if(y==arr[x1]):
                y=0
                
            c+=1   
    return -1

"""
