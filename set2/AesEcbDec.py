from EncryptionAES import encryption_oracle_ecb
import base64
import string

BASE_64 = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'

LETTERS = string.printable


def crack_ecb():
    cracked = ''
    base_64_decoded = base64.decodestring(BASE_64)
    for block in range(0, len(encryption_oracle_ecb(base_64_decoded))+16,16 ):
        crack_block = ''
        for i in range(1, 16+1):
            padding = 'A'*(16-i)+cracked+crack_block
            lookup = {}
            for c in LETTERS:
                lookup[encryption_oracle_ecb(padding+c)[block:block+16]] = c

            padding = 'A'*(16-i)
            enc = encryption_oracle_ecb(padding+base_64_decoded)
            try:
                crack_block += lookup[enc[block:block+16]]
            except KeyError:
                pass
        cracked += crack_block
    print cracked


if __name__ == '__main__':
    crack_ecb()