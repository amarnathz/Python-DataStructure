def find_gcd(x,y):
    while(y):
        x,y=y,x%y
    return x
    
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    
    if(len(a)==1):
        gcd=a[0]
    else:
        num1=a[0]
        num2=a[1]
        gcd=find_gcd(num1,num2)
        
        for i in range(2,len(a)):
            gcd=find_gcd(gcd,a[i])
        
    print(gcd)
    
