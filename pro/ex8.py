##Given an array A of size N which consists of positive integers. The task is to make the largest number K from array elements such that every chosen array element has exactly 3 divisiors. If no such number can be formed then print -1.
##
##Input:
##The first line of input contains T denoting the number of testcases. Each testcase contains two lines. The first line contains N(size of the array) and second line contains N space separated elements of an array
##
##Output:
##Print the required answer in new line
##
##Constraints:
##1 <= T <= 100
##1 <= N <= 107
##1 <= A[i] <= 1018
## 
##
##Example:
##Input:
##1
##10
##1 2 3 4 5 6 7 8 9 10
##
##Output:
##94
##
##Explanation:
##Testcase 1: In the given array 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. 4 and 9 are the only elements which are having exactly 3 divisors i.e divisors of 4 are 1, 2, 4 and divisors of 9 are 1, 3, 9. Thus 94 is the largest number formed from these two numbers having exactly 3 divisors.
##
## 
##



T=int(input())
for i in range(T):
    s=int(input())
    a=[]
    w=[]
    a=input().split(" ")
    for i in range(s):
        y=int(a[i])
        c=0
        for q in range(y):
            if( y%(q+1)==0 ):
                c+=1
        if(c==3):
            w.append(y)
        w.sort(reverse = True)  #desending order
    if (w is None):
        print(-1)
    else:
        for i in w:
            print(i,end="")
    

        
