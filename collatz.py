def collatz(n):
    """
    produces the collatz function
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1
    

def sequence(i, n):
    """
    Creates the collatz sequence starting at n
    goal is to see if it converges to 1
    """
    if n == 1:
        print("1 reached in", i, "steps")
        return
    if i == 500:
        print("Could not reach 1 in 500 steps")
        return
    else:
        print(n)
        sequence(i + 1, collatz(n))



n = int(input("Collatz: "))
sequence(0, n)