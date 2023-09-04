ciphertext = """ymnx nx ymj ktwjxy uwnrjafq
esp bflwtej zq xpcnj td yze decltypo}
owlzwhwghdwgxlzwmfalwvklslwk
haahjr ha khdu
wkh srufxslqh lv xqghu wkh vkhhwv
WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
"""


def shift_text(text, key):
    shifted = ''
    for c in text:
        if ord('a') <= ord(c) <= ord('z'):
            shifted_c = ord('a') + ((ord(c) + key + 1) % ord('a')) % 26
        elif ord('A') <= ord(c) <= ord('Z'):
            shifted_c = ord('A') + ((ord(c) + key + 1) % ord('A')) % 26
        else:
            shifted_c = ord(c)
        shifted += chr(shifted_c)
    return shifted


def brute_force():
    for i in range(25):
        print('Key:', i)
        print(shift_text(ciphertext, i))


if __name__ == '__main__':
    brute_force()