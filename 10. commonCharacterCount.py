#Q:

#Given two strings, find the number of common characters between them.

#Example

#For s1 = "aabcc" and s2 = "adcaa", the output should be
#solution(s1, s2) = 3.

#Strings have 3 common characters - 2 "a"s and 1 "c".

#Input/Output

#[execution time limit] 4 seconds (py3)

#[input] string s1

#A string consisting of lowercase English letters.

#Guaranteed constraints:
#1 ≤ s1.length < 15.

#[input] string s2

#A string consisting of lowercase English letters.

#Guaranteed constraints:
#1 ≤ s2.length < 15.

#[output] integer

#A:


def solution(s1, s2):
    s1_l = list(s1)
    s2_l = list(s2)
    common = []
    for i in s1_l:
        if i in s2_l:
            common.append(i)
            s2_l.remove(i)
    return len(common)