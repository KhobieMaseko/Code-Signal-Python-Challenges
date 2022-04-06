Q:

#Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

#Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

#Example

#For sequence = [1, 3, 2, 1], the output should be
#solution(sequence) = false.

#There is no one element in this array that can be removed in order to get a strictly increasing sequence.

#For sequence = [1, 3, 2], the output should be
#solution(sequence) = true.

#You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

#Input/Output

#[execution time limit] 4 seconds (py3)

#[input] array.integer sequence

#Guaranteed constraints:
#2 ≤ sequence.length ≤ 105,
#-105 ≤ sequence[i] ≤ 105.

#[output] boolean

#Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

A:

def solution(sequence):
    n = len(sequence)
    if n <= 2:
        return True
    c1 = 0
    c2 = 0
    for i in range(1, n-1):
        if sequence[i-1] >= sequence[i]:
            c1 += 1
        if sequence[i-1] >= sequence[i+1]:
            c2 += 1
    if sequence[n-1] <= sequence[n-2]:
        c1 += 1
    if c1 <= 1 and c2 <= 1:
        return True
    else:
        return False