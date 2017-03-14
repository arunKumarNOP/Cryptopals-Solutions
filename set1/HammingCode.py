def hamming_distance(s, t):
    s = bytearray(s)
    t = bytearray(t)
    count = 1.0
    for i in range(len(s)):
        count += str(bin(s[i] ^ t[i]))[2:].count('1')

    return count