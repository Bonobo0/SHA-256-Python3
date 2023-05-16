from k import get_list_of_constant_k
from message_preprocess import pre_process
from round_function import round_function
from w import get_w
from h import get_initial_constant_number
import hashlib


def sha256(message: list):
    block_count = len(message)

    # Initial constant number
    H = get_initial_constant_number()
    # K constant
    K = get_list_of_constant_k()
    # Round function
    for i in range(block_count):
        w = get_w(message[i])
        rf = round_function(H, K, w)

    H[0] = (H[0] + rf[0]) % 2**32
    H[1] = (H[1] + rf[1]) % 2**32
    H[2] = (H[2] + rf[2]) % 2**32
    H[3] = (H[3] + rf[3]) % 2**32
    H[4] = (H[4] + rf[4]) % 2**32
    H[5] = (H[5] + rf[5]) % 2**32
    H[6] = (H[6] + rf[6]) % 2**32
    H[7] = (H[7] + rf[7]) % 2**32

    return (H[0].to_bytes(4, 'big') +
            H[1].to_bytes(4, 'big') +
            H[2].to_bytes(4, 'big') +
            H[3].to_bytes(4, 'big') +
            H[4].to_bytes(4, 'big') +
            H[5].to_bytes(4, 'big') +
            H[6].to_bytes(4, 'big') +
            H[7].to_bytes(4, 'big'))

if __name__ == "__main__":
    string_message = input("암호화 할 메시지를 입력해주세요: ")
    assert len(string_message) > 0, "메시지를 입력해주세요."
    # assert len(string_message) < 55, "메시지는 55자 이하로 입력해주세요."
    message = pre_process(string_message)
    hash_value = sha256(message)
    print(hash_value.hex(), "\nlength: ", len(hash_value))
    print("Same as SHA-256: ", hash_value.hex() == hashlib.sha256(string_message.encode(
        'utf-8')).hexdigest())
