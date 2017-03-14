import base64
from HammingCode import hamming_distance
import binascii
from EnglishScore import solve_single_xor
from Xor import xor


def getProbableKeylen(encMsg, top):
    keylen = {}

    for i in range(2, 41):
        ham_dist = 0.0
        for k in range(0,10*2*i,i+i):
            ham_dist += hamming_distance(encMsg[k:k+i], encMsg[k+i:k+i+i])
        ham_dist /= i*10.0
        if i not in keylen:
            keylen[i] = ham_dist
        elif ham_dist < keylen[i]:
            keylen[i] = ham_dist

    sorted_keys = sorted(keylen.items(), key=lambda t: t[1])
    print sorted_keys
    for i in range(top):
        yield sorted_keys[i][0]


def findXORKey(encMsg, noOfKey):
    for keylength in getProbableKeylen(encMsg, noOfKey):
        key = bytearray()
        for i in range(keylength):
            block = bytearray()
            for j in range(0,len(encMsg)-keylength,keylength):
                block.append(encMsg[j+i])
            block = binascii.hexlify(block)
            for ans in solve_single_xor(block, 95, 6):
                key.append(ans[0])
                print i,ans
        print key

s = base64.decodestring(open('6.txt').read().replace('\n', ''))
findXORKey(s, 4)
# k = binascii.hexlify('Terminator X: Bring the noise')
# print xor(s,k,False)