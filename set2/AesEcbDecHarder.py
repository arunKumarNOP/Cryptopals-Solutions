from EncryptionAES import encryption_oracle_ecb2
import base64
import string
import random


LETTERS = string.printable
BASE_64 = 'Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK'
PRE = ''.join([random.choice(LETTERS) for k in range(random.randint(5,30))])


def get_length_of_padding(base_64_decoded):
    for l in range(32, 64+1):
        attacking = 'a'*l
        enc = encryption_oracle_ecb2(PRE, attacking+base_64_decoded)
        for block in range(0,len(enc)-32, 16):
            if enc[block:block+16] == enc[block+16:block+32]:
                return l % 32, block

def crack_ecb():
    base_64_decoded = base64.decodestring(BASE_64)
    extra_padding, starting_block = get_length_of_padding(base_64_decoded)
    print extra_padding, starting_block

    cracked = ''
    for block in range(starting_block, len(encryption_oracle_ecb2(PRE, base_64_decoded))+16, 16):
        crack_block = ''
        for i in range(1, 16+1):
            padding = 'A'*(16-i+extra_padding)+cracked+crack_block
            lookup = {}
            for c in LETTERS:
                lookup[encryption_oracle_ecb2(PRE, padding+c)[block:block+16]] = c

            padding = 'A'*(16-i+extra_padding)
            enc = encryption_oracle_ecb2(PRE, padding+base_64_decoded)
            try:
                crack_block += lookup[enc[block:block+16]]
            except KeyError:
                pass
        cracked += crack_block
    print cracked


if __name__ == '__main__':
    crack_ecb()