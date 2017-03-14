import binascii


def xor(a, key, hexilify=True):
    if len(key)%2 == 1:
        key = '0'+key
    s = bytearray(binascii.unhexlify(a))
    k = bytearray(binascii.unhexlify(key))

    l = bytearray()
    for i in range(len(s)):
        l.append(s[i] ^ k[i%len(k)])

    if hexilify:
        return binascii.hexlify(l)
    return str(l)


def xorPlain(s, t, hexilify=False):
    if len(t)%2 == 1:
        t = '0'+t

    s = bytearray(s)
    t = bytearray(t)

    l = bytearray()
    for i in range(len(s)):
        l.append(s[i] ^ t[i%len(t)])

    if hexilify:
        return binascii.hexlify(l)
    return str(l)

def main():
    print xor('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    print xor('1c0111001f010100061a024b53535009181c', '68', False)

if __name__=='__main__':
    main()
