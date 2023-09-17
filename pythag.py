"""
Function for generating pythagorean triples
"""

def is_pythag_triple(a, b, c):
    return a**2 + b**2 == c**2

    
def integer_partitions(n):
    """
    Gives all possible integer partitions of integer n:
    Given an integer partition of n, we can create all integer partitions of n - 1 by
    taking one argument in the position and subtracting it
    Or, we can construct an integer partition of n as an n tuple, where each component
    has to be nondecreasing:
    for example, a partition of 6 would look like (1, 1, 1, 1, 1, 1), (0, 1, 1, 1, 1, 2), (0, 0, 0, 0, 0, 6)
    Uses brute force method
    """
    partition = []
    for i in len(n):
        pass


a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

print(is_pythag_triple(a, b, c))

