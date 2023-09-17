"""
Program designed to solve linear congruences
First take equation in Z of the form
"ax = b (mod n)"
Then solve that by turning it into form
ax = b + nm, m in Z
trying to find the tuple (x, m) in Z X Z
ax + (-m)n = b is bezout's lemma
Hence, try to find gcd(a, n) and the apply the
Extended euclidean algorithm
Of course, impossible to find such a pair if
gcd(a, n) does not divide b
"""

def solve_congruence(a, b, n):
    """
    solve congruence of form ax = b (mod n)
    """

    # first, check if solvable
    # since computer, just brute force it
    for x in range(n):
        if (a * x) % n == b % n:
            return x
    
    print("Cannot be solved")
    return -1

print("Solve congruence of form ax = b (mod n)")
a = int(input("a = "))
b = int(input("b = "))
n = int(input("n = "))

print(solve_congruence(a, b, n))