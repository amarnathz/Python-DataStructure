T=int(input())
for i in range(T):
    n,d=map( int, input().split() )
    a=list(input().split())
    b=a[d:]+a[:d]
    #print(*a, sep = "\n")    * list the element
    [print(b[x],end=" ") for x in range(len(b))]
    print()
