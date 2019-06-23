def a(n):
    t=n
    if(n>=1 and n<=9):
        return n;
    else:
        s=[]
        r=1
        for i in range(9,1,-1):
            if(n%i==0):
                s.append(i)
                n=n//i
            if(i==2 and n !=1 and n<=9):
                s.append(n)
        for i in range(len(s)):
            r*=int(s[i])
          
        if(len(s) == 0 or r!=t):
            
            return -1
        s.sort()
        n=0
        for i in range(len(s)):
            n=n*10+s[i]
        
        return n
                     
T=int(input())
for i in range(T):
    n=int(input())
    print(a(n))
##
##Given a number N. Find a number K such that product of digits of K must be equal to N.
##Note : K must be as small as possible.
##
##Input: First line of input contains number of testcases T. For each testcase, there will be a single line containing N.
##
##Output: For each testcase, output single integer. If K is not possible, print "-1" (without quotes).
##
##Constraints:
##1 <= T <= 100
##1 <= N <= 1015
##
##Example:
##Input:
##2
##12
##5
##
##Output:
##26
##5
##
##Explanation:
##Testcase 1: 26 is the smallest number, and product of 2 and 6 is 12.
##Testcase 2: 5 is the smallest number which is itself equal to 5.

 
