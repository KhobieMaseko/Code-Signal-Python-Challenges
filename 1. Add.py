Q:

Write a function that returns the sum of two numbers.

Example

For param1 = 1 and param2 = 2, the output should be
solution(param1, param2) = 3.

Input/Output

[execution time limit] 4 seconds (py3)

[input] integer param1

Guaranteed constraints:
-1000 ≤ param1 ≤ 1000.

[input] integer param2

Guaranteed constraints:
-1000 ≤ param2 ≤ 1000.

[output] integer

The sum of the two inputs.

[Python 3] Syntax Tips

# Prints help message to the console
# Returns a string
def helloWorld(name):
    print("This prints to the console when you Run Tests")
    return "Hello, " + name

A:

def solution(param1, param2):
    return param1 + param2