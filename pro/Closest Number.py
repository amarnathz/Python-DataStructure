"""
Given two integers N and M. The problem is to find the number closest to N and divisible by M.
If there are more than one such number, then output the one having maximum absolute value.

Input:
The first line consists of an integer T i.e number of test cases. T testcases follow.
The first and only line of each test case contains two space separated integers N and M.

Output:
For each testcase, in a new line, print the closest number to N which is also divisible by M.

Constraints: 
1 <= T <= 100
-1000 <= N, M <= 1000

Example:
Input:
2
13 4
-15 6
Output:
12
-18

"""

for i in range(0, T):
    line = input()
    n, m = line.split(' ')
    n = int(n)
    m = abs(int(m))
    rest = n % m
    result = 0
    if rest == 0:
        result = n
    else:
        if rest < m-rest:
            result = n - rest
        elif m-rest < rest:
            result = n + (m-rest)
        else:
            candidate1 = n - rest
            candidate2 = n + (m-rest)
            if abs(candidate1) > abs(candidate2):
                result = candidate1
            else:
                result = candidate2

    print(result)
  
