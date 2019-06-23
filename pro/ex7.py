                     
T=int(input())
for i in range(T):
    n=int(input())
    if(n<2 and n>=0):
        print(1)
    elif(n==2):
        print(2)
      
    elif(n==3):
        print(6)
    elif(n==4):
        print(4)
    else:
        print(0)

##Given a number N. The task is to find the unit digit of factorial of given number N.
##
##Input:
##First line of input contains number of testcases T. For each testcase, there will be a single line containing N.
##
##Output:
##For each testcase, print the unit digit of factorial of N.
##
##Constraints:
##1 <= T <= 1000
##1 <= N <= 1018
##
##Example:
##Input:
##2
##3
##4
##
##Output:
##6
##4
##
