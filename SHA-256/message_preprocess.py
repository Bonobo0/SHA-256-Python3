def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] >> shift) & 0x1


def pre_process(message: str):
    message = bytearray(message, 'utf-8')
    message_length = len(message) * 8
    message.append(0x80)
    while (len(message) * 8 + 64) % 512 != 0:
        message.append(0x00)
    message += message_length.to_bytes(8, byteorder='big')
    assert (len(message) * 8) % 512 == 0, "메시지 길이가 적합하지 않습니다."
    blocks = []
    for i in range(0, len(message), 64):
        blocks.append(message[i:i+64])
    return blocks
