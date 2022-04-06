Q:

Write a function that returns the sum of two numbers.

Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
solution(year) = 20;
For year = 1700, the output should be
solution(year) = 17.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.


A:

def solution(year):
    century = int(year/100)
    while year >= 1:
        if year % 100 == 0:
            return year / 100
        else:
            return century + 1
