import gcd as g

def totient(n):
    """
    returns phi(n), the euler totient function
    the number of integers less than n relative prime to n
    """
    phi = 0

    for m in range(1, n):
        if g.gcd(m, n) == 1:
            phi += 1

    return phi


print("Euler Totient Function: ")
n = int(input("n: "))

print("Value of totient fn:", totient(n))

print("Euler's Theorem: ")

a = int(input("Pick a: "))

a_to_n = a ** totient(n)

print("a^n =", a_to_n % n, "(mod n)")