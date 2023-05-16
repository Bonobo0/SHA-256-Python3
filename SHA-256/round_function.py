def BSigma_0(x):
    num = (_rotate_right(x, 2) ^
           _rotate_right(x, 13) ^
           _rotate_right(x, 22))
    return num


def BSigma_1(x):
    num = (_rotate_right(x, 6) ^
           _rotate_right(x, 11) ^
           _rotate_right(x, 25))
    return num


def Choose(x, y, z):
    return (x & y) ^ (~x & z)


def Majority(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)


def _rotate_right(num: int, shift: int, size: int = 32):
    return (num >> shift) | (num << size - shift)


def round_function(H, K, W):
    a, b, c, d, e, f, g, h = H
    for t in range(64):
        T1 = ((h + BSigma_1(e) + Choose(e, f, g) +
               K[t] + int.from_bytes(W[t], 'big')) % 2**32)
        T2 = BSigma_0(a) + Majority(a, b, c) % 2**32
        h = g
        g = f
        f = e
        e = (d + T1) % 2**32
        d = c
        c = b
        b = a
        a = (T1 + T2) % 2**32
    return [a, b, c, d, e, f, g, h]
