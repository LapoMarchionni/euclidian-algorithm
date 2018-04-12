def gdc(a, b):
    """Recursively calculate the GDC between two positive 
    integer numbers.
    a is always setted as the biggest of the two while b is the smallest.
    """
    assert a > 0 and b > 0, ("Both number must be positive integers")
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    return gdc(b, a % b)


def egdc(a, b):
    pass
