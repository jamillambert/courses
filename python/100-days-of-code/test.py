# File for testing small sections of code that are not required as part of a project
import math


def sqrt(n, precision):
    ans = n
    max_remainder = 1
    error = n/2.0
    if n < 0:
        print("Square root of negative numbers not supported")
        return 0
    for i in range(precision):
        max_remainder *= 0.1
    while abs(error) > max_remainder:
        result = ans*ans
        if error > 0.0 and result < n:
            error = -error/2
        elif error < 0.0 and result > n:
            error = -error/2
        ans = ans - error
    return ans
n = 17
precision = 10
ans = sqrt(n, 10)
print("Square root of {} is {:0.9f} with a calculation precision of {}".format(n, ans, precision))


print("Using the math crate the square root of {} is {}".format(n, math.sqrt(n)))