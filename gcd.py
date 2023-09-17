def gcd(a, b):
    """
    Finds the gcd of a and b, with bezout's lemma
    Implemented by euclidean algorithm
    """
    # iteratively:
    y = max(a, b)
    x = min(a, b)
    r = y % x
    
    while r != 0:
        y = x
        x = r
        r = y % x

    return x

def gcd_recursion(a, b):
    """
    does gcd recursively
    also computes the linear combinations
    assume first that a > b > 0
    """
    y = max(a, b)
    x = min(a, b)

    if y % x == 0:
        # then we have a linear combination, and x is our gcd
        # we need to return in format of: (gcd, x, y)
        return (x, 0, 1)
    else:
        r, new_x, new_y = gcd_recursion(x, y % x)
        # now that you've got expression, do this
    


a = int(input("a: "))
b = int(input("b: "))

print(gcd(a, b))

def gcd_poly(p, q):
    """
    Does the euclidean algorithm, but for polynomials
    """

def find_determinant(matrix):
    """
    Finds determinant of a matrix
    Using the cofactor expansion method
    """
    row = len(matrix)
    column = len(matrix[0])

    if row != column:
        print("Cannot compute determinant: not a square matrix")
        return

    for i in row:
        # take all the cofactors of rows
        pass

