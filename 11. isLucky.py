#Q:

#Ticket numbers usually consist of an even number of digits. 

#A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

#Given a ticket number n, determine if it's lucky or not.

#Example

#For n = 1230, the output should be
#solution(n) = true;
#For n = 239017, the output should be
#solution(n) = false.
#Input/Output

#[execution time limit] 4 seconds (py3)

#[input] integer n

#A ticket number represented as a positive integer with an even number of digits.

#Guaranteed constraints:
#10 ≤ n < 106.

#[output] boolean

#true if n is a lucky ticket number, false otherwise.

#A:


def solution (n):
    digits_of_n = []
    summation = 0
    while n > 0:
        rem = n % 10
        digits_of_n.append(rem)
        n = int(n / 10)
    for i in range(len(digits_of_n)):
        if i < len(digits_of_n)/2:
            summation += digits_of_n[i]
        else:
            summation -= digits_of_n[i]
    if summation == 0:
        return True
    return False