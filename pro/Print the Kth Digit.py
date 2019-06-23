
"""

Given two numbers A and B, find Kth digit from right of A^B.

Input:
The first line of the input contains T denoting the number of test cases. T testcases follow.  Each of the next T lines contains three space separated positive integers denoting the value of a , b and k respectively.

Output:
For each test case, in a new line, output the Kth digit from right of A^B in new line.

Constraints:
1 <= T <= 100
1 <= A , B <=15
1 <= K <= |totaldigits in AB|

Example:
Input:
2
3 3 1
5 2 2
Output:
7
2
"""


import math
t=int(input())
for i in range(t):
    a,b,k=input().split(' ')
    a=int(a)
    b=int(b)
    k=int(k)
    ans=int(math.pow(a,b))
    ans=str(ans)
    ans=ans[::-1]
    print(ans[k-1])
    
