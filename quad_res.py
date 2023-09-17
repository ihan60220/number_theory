def quad_res(x, n):
    """
    determines if x is a quadratic residue mod n
    i.e., if there exists a in Z_n such that
    x = a^2 (mod n)
    """

    for m in range(n):
        if x % n == m**2 % n:
            return m
        
    return -1


print("quadratic residue of x in modulo n")
x = int(input("x: "))
n = int(input("n: "))

print("a =", quad_res(x, n))