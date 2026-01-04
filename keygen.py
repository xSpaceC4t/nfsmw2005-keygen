import zlib
import random
import string


# const val = 0x1d66b
# 12345678ABCDEFGHIJKL -> input key
# 1KFLGH7IABCDJ3568E24 -> first swap
# hash(1KFLGH7IABCDJ) -> 0x17E60372
# 2MGRXJB -> generated str from hash 0x17e60372
# 1KFLGH7IABCDJ 2MGRXJB
# 0x11121E35 -> hash from 1KFLGH7IABCDJ 2MGRXJB
# 46b3wfc -> generated str from hash 0x11121e35
# 1KFLGH7IABCDJ 46B3WFC
# 1 [23456] 7 [8] ABCD [E] FGHIJKL
# 1 [F4C6B] 7 [3] ABCD [W] FGHIJKL - final cmp
# 1KFLGH7IABCDJ 3568E24


def crc32_byte(crc):
    for i in range(8):
        if crc & 1:
            crc = (crc >> 1) ^ 0xEDB88320
        else:
            crc = crc >> 1
    return crc


def swap(key):
    swaps = [
        (1, 18),
        (2, 13),
        (3, 19),
        (4, 14),
        (5, 15),
        (7, 16),
        (12, 17)
    ]
    for x, y in swaps:
        key[x], key[y] = key[y], key[x]
    return key


if __name__ == "__main__":
    const_val = 0x1D66B
    char_map = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ64382957JKLMNPQRSTUVWXYZABCDEFGH'

    table = []
    for i in range(256):
        table.append(crc32_byte(i))
    print(table)

    chars = string.digits + string.ascii_uppercase
    seed = "".join(random.choice(chars) for _ in range(13))
    print(seed)

    chksum = zlib.adler32(seed.encode())
    print(hex(chksum))

    val = chksum ^ const_val
    buf = [0] * 7
    offsets = [30, 25, 20, 15, 10, 5, 0]
    for i in range(7):
        buf[i] = (val >> offsets[i]) & 0x1f
    buf[0] = (4 * (buf[6] & 7)) | buf[0]
    for i in range(7):
        buf[i] = char_map[buf[i] + 32]
    print(buf)

    key = list(seed) + buf

    x = const_val
    for i in range(20):
        x = table[(x ^ ord(key[i])) & 0xff] ^ (x >> 8)
    print(hex(x))

    val = x
    buf = [0] * 7
    buf[6] = 8 * (val & 3)
    offsets = [27, 22, 17, 12, 7, 2] 
    for i in range(6):
        buf[i] = (val >> offsets[i]) & 0x1f
    buf[6] |= (val >> 27) & 7
    for i in range(7):
        buf[i] = char_map[buf[i]]
    print(buf)

    key = list(seed) + buf
    print(key)

    key = swap(key)
    print(key)

    key = ''.join(key)
    key = '-'.join([key[i:i+4] for i in range(0, len(key), 4)])
    print(key)  # ABCD-EFGH-IJKL-MNOP