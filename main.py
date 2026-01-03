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
print(bin(val))

buf = [0] * 7
buf[6] = val & 0x1F          # Bits 0-4
buf[5] = (val >> 5) & 0x1F   # Bits 5-9
buf[4] = (val >> 10) & 0x1F  # Bits 10-14
buf[3] = (val >> 15) & 0x1F  # Bits 15-19
buf[2] = (val >> 20) & 0x1F  # Bits 20-24
buf[1] = (val >> 25) & 0x1F  # Bits 25-29
buf[0] = (val >> 30) & 0x1F  # Bits 30-31 (only 2 bits)
print(buf)

char_map = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ64382957JKLMNPQRSTUVWXYZABCDEFGH'
buf[0] = (4 * (buf[6] & 7)) | buf[0]
buf[0] = char_map[buf[0] + 32]
buf[1] = char_map[buf[1] + 32]
buf[2] = char_map[buf[2] + 32]
buf[3] = char_map[buf[3] + 32]
buf[4] = char_map[buf[4] + 32]
buf[5] = char_map[buf[5] + 32]
buf[6] = char_map[buf[6] + 32]
print(buf)

table = [
    0x00000000, 0x77073096, 0xEE0E612C, 0x990951BA,
    0x076DC419, 0x706AF48F, 0xE963A535, 0x9E6495A3,
    0x0EDB8832, 0x79DCB8A4, 0xE0D5E91E, 0x97D2D988,
    0x09B64C2B, 0x7EB17CBD, 0xE7B82D07, 0x90BF1D91,
]
for i in range(5, 20, 5):
    pass

# 0042FAB8  00 00 00 00 96 30 07 77 2C 61 0E EE BA 51 09 99  .....0.w,a.îºQ..  
# 0042FAC8  19 C4 6D 07 8F F4 6A 70 35 A5 63 E9 A3 95 64 9E  .Äm..ôjp5¥cé£.d.  
# 0042FAD8  32 88 DB 0E A4 B8 DC 79 1E E9 D5 E0 88 D9 D2 97  2.Û.¤¸Üy.éÕà.ÙÒ.  
# 0042FAE8  2B 4C B6 09 BD 7C B1 7E 07 2D B8 E7 91 1D BF 90  +L¶.½|±~.-¸ç..¿.  
# 0042FAF8  64 10 B7 1D F2 20 B0 6A 48 71 B9 F3 DE 41 BE 84  d.·.ò °jHq¹óÞA¾.  
# 0042FB08  7D D4 DA 1A EB E4 DD 6D 51 B5 D4 F4 C7 85 D3 83  }ÔÚ.ëäÝmQµÔôÇ.Ó.  
# 0042FB18  56 98 6C 13 C0 A8 6B 64 7A F9 62 FD EC C9 65 8A  V.l.À¨kdzùbýìÉe.  
# 0042FB28  4F 5C 01 14 D9 6C 06 63 63 3D 0F FA F5 0D 08 8D  O\..Ùl.cc=.úõ...  
# 0042FB38  C8 20 6E 3B 5E 10 69 4C E4 41 60 D5 72 71 67 A2  È n;^.iLäA`Õrqg¢  
# 0042FB48  D1 E4 03 3C 47 D4 04 4B FD 85 0D D2 6B B5 0A A5  Ñä.<GÔ.Ký..Òkµ.¥  
# 0042FB58  FA A8 B5 35 6C 98 B2 42 D6 C9 BB DB 40 F9 BC AC  ú¨µ5l.²BÖÉ»Û@ù¼¬  
# 0042FB68  E3 6C D8 32 75 5C DF 45 CF 0D D6 DC 59 3D D1 AB  ãlØ2u\ßEÏ.ÖÜY=Ñ«  
# 0042FB78  AC 30 D9 26 3A 00 DE 51 80 51 D7 C8 16 61 D0 BF  ¬0Ù&:.ÞQ.Q×È.aÐ¿  
# 0042FB88  B5 F4 B4 21 23 C4 B3 56 99 95 BA CF 0F A5 BD B8  µô´!#Ä³V..ºÏ.¥½¸  
# 0042FB98  9E B8 02 28 08 88 05 5F B2 D9 0C C6 24 E9 0B B1  .¸.(..._²Ù.Æ$é.±  
# 0042FBA8  87 7C 6F 2F 11 4C 68 58 AB 1D 61 C1 3D 2D 66 B6  .|o/.LhX«.aÁ=-f¶  
# 0042FBB8  90 41 DC 76 06 71 DB 01 BC 20 D2 98 2A 10 D5 EF  .AÜv.qÛ.¼ Ò.*.Õï  
