# File for testing small sections of code that are not required as part of a project
import math


def sqrt(n, precision):
    answer = n
    max_remainder = 1
    error = n/2.0
    if n < 0:
        print("Square root of negative numbers not supported")
        return 0
    for i in range(precision):
        max_remainder *= 0.1
    while abs(error) > max_remainder:
        result = answer * answer
        if error > 0.0 and result < n:
            error = -error/2
        elif error < 0.0 and result > n:
            error = -error/2
        answer = answer - error
    return answer


number = 2
prec = 10
ans = sqrt(number, 10)
math_ans = math.sqrt(number)
print("Square root of {} is {:0.9f} with a calculation precision of {}".format(number, ans, prec))
print("Using the math crate the square root of {} is {}".format(number, math_ans))
print("Difference between the two is {:0.2e}".format(ans - math_ans))
