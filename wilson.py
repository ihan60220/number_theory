def fact(m):
    """
    the factorial function
    """

    if m == 0:
        return 1
    else:
        return m * fact(m - 1)


def wilson(p):
    """
    demonstrates wilson's theorem which states that
    p is prime <=> (p - 1)! = -1 (mod p)
    """

    if fact(p - 1) % p == p - 1:
        return True
    else:
        return False
    

print("primality testing with wilson's theorem")
p = int(input("pick p: "))
print(wilson(p))