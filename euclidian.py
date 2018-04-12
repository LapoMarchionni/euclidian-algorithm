def gdc(a, b):
    """Recursively calculate the GDC between two positive
    integer numbers.
    If a < b, the first recursion will exchange both numbers.
    """
    assert a >= 0 and b >= 0, (
        "Both number must be positive integers")
    if b == 0:
        return b
    return gdc(b, a % b)


def egdc(a, b):
    pass
