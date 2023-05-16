from decimal import *

getcontext().prec = 32

primeList = [2, 3, 5, 7, 11, 13, 17, 19]


def get_initial_constant_number():
    pre_generated_initial_constant_number = [
        0x6a09e667,
        0xbb67ae85,
        0x3c6ef372,
        0xa54ff53a,
        0x510e527f,
        0x9b05688c,
        0x1f83d9ab,
        0x5be0cd19
    ]
    for i, j in enumerate(primeList):
        t = Decimal(j) ** Decimal(1/2)
        t -= int(t)
        t *= pow(16, 8)
        primeList[i] = int(hex(int(t)), 16)
    return primeList
