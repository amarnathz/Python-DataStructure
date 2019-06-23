"""
Given the first 2 terms A and B of a Geometric Series, tell the Nth term of the series.

Input:
First line contains an integer, the number of test cases 'T'. T testcases follow. Each test case in its first line contains two positive integer A and B (First 2 terms of GP). In the second line of every test case it contains of an integer N.

Output:
In each seperate line print the Nth term of the Geometric Progression. Print the floor ( floor(2.3)=2 ) of the answer.

Constraints:
1 <= T <= 30
-100 <= A <= 100
-100 <= B <= 100
1 <= N <= 5

Example:
Input:
2
2 3
1
1 2
2
Output:
2
2

Tn=ar^(n-1)


"""
import math
T=int(input())
for i in range(T):
    a,m=input().split(" ")
    a=int(a)
    m=int(m)
    term=int(input())
    r=float(m/a)
    print(r)
    s=a*r**(term-1)
    if  s <0:
        s=abs(s)
        s=math.floor(s)
        print(s*-1)
    else:
        s=math.floor(s)
        print(s)
    
    
    
