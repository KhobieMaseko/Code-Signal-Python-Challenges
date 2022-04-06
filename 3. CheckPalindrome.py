Q:

#Given the string, check if it is a palindrome.

#Example

#For inputString = "aabaa", the output should be
#solution(inputString) = true;
#For inputString = "abac", the output should be
#solution(inputString) = false;
#For inputString = "a", the output should be
#solution(inputString) = true.
#Input/Output

#[execution time limit] 4 seconds (py3)

#[input] string inputString

#A non-empty string consisting of lowercase characters.

#Guaranteed constraints:
#1 ≤ inputString.length ≤ 105.

#[output] boolean

#true if inputString is a palindrome, false otherwise.


A:

def solution(inputString):
    input1 = inputString.lower()
    input1 = input1.replace(" ","")
    reverse = input1[::-1]
    if (reverse == input1):
        return True
    else:
        return False
