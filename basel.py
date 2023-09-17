"""
Verifies the correctedness of Basel problem
For context, the sum of all reciprocal of square of natural numbers
converges to pi squared over six
"""

pi = 3.14159

def partial_sum(n):
    """
    Returns the partial sum of the 2-series
    up to the nth term
    """
    sum = 0

    for m in range(1, n + 1):
        sum += 1 / m**2
    
    return sum


def error(partial, total):
    """
    calculates the relative error of the partial sum
    with respect to the total
    """
    
    absolute_error = total - partial
    relative_error = absolute_error / total
    return 100 * relative_error


print("The Basel Problem: Convergence")
n = int(input("Check convergence up to nth term: "))
ps = partial_sum(n)
a_s = pi**2 / 6
print("The partial sum is:", ps)
print("The actual value of this series is pi squared over 6:", a_s)
print("The error is:", error(ps, a_s), "%")
