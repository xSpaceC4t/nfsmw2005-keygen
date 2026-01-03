import zlib

key = 'AAAA-BBBB-CCCC-DDDD-EEEE'
key = '1234-5678-ABCD-EFGH-IJKL'
print(key)
key = list(key.replace('-', ''))

# 12345678ABCDEFGHIJKL
# 1KFLGH7IABCDJ3568E24

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
key[13] = 0
print(key)

const_val = 0x1D66B

x = key[:13]
x = ''.join(x).encode()
chksum = zlib.adler32(x)
print(hex(chksum))
# 0x17E60372

val = chksum ^ const_val
buf = [0] * 7
buf[6] = val & 0x1F          # Bits 0-4
buf[5] = (val >> 5) & 0x1F   # Bits 5-9
buf[4] = (val >> 10) & 0x1F  # Bits 10-14
buf[3] = (val >> 15) & 0x1F  # Bits 15-19
buf[2] = (val >> 20) & 0x1F  # Bits 20-24
buf[1] = (val >> 25) & 0x1F  # Bits 25-29
buf[0] = (val >> 30) & 0x1F  # Bits 30-31 (only 2 bits)

char_map = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ64382957JKLMNPQRSTUVWXYZABCDEFGH'
buf[0] = (4 * (buf[6] & 7)) | buf[0]