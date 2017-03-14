from set1.Aes_cipher import *


def pkcs7_pad(s, length):
    inputLen = len(s)
    lenOfPadding = length - inputLen % length
    return s + chr(lenOfPadding)*lenOfPadding


def pkcs7_pad_check(s):
    last_block = bytearray(s[-16:])
    if last_block[-1] < 16:
        lenOfPadding = last_block[-1]
        padding_block = last_block[-lenOfPadding:]
        for i in range(len(padding_block)-1):
            if padding_block[i] != padding_block[i+1]:
                raise Exception('Incorrect padding')
        return s[:-lenOfPadding]
    return s


if __name__ == '__main__':
    key = 'A'*16
    for i in range(1,17):
        print pkcs7_pad_check(encrypt_ecb('a'*i, key))
    enc = bytearray(encrypt_ecb('a'*10, key))
    enc[-1] = '\10'
    print pkcs7_pad_check(str(enc))