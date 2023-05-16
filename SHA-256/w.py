def _rotate_right(num: int, shift: int, size: int = 32):
    return (num >> shift) | (num << size - shift)


def _SSigma_0(x: int):
    return _rotate_right(x, 7) ^ _rotate_right(x, 18) ^ (x >> 3)


def _SSigma_1(x: int):
    return _rotate_right(x, 17) ^ _rotate_right(x, 19) ^ (x >> 10)


def get_w(binary: int):
    w = []
    for i in range(0, 64):
        if i <= 15:
            w.append(bytes(binary[i*4:(i*4)+4]))
        else:
            term1 = _SSigma_1(int.from_bytes(w[i-2], byteorder='big'))
            term2 = int.from_bytes(w[i-7], byteorder='big')
            term3 = _SSigma_0(int.from_bytes(w[i-15], byteorder='big'))
            term4 = int.from_bytes(w[i-16], byteorder='big')

            total = ((term1 + term2 + term3 + term4) %
                     2**32).to_bytes(4, byteorder='big')
            w.append(total)
    return w
