def gcd(a, b):
    """Recursively calculate the GDC between two positive
    integer numbers.
    If a < b, the first recursion will exchange both numbers.
    """
    assert a >= 0 and b >= 0, (
        "Both number must be positive integers")
    if b == 0:
        return b
    return gdc(b, a % b)


def egcd(a, b):
    """Extends the euclidian gdc with negative numbers."""
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)
