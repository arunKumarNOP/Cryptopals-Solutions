import os
from set1.Aes_cipher import encrypt_cbc, encrypt_ecb
import random


def encryption_oracle(plainTxt):
    iv = os.urandom(16)
    key = os.urandom(16)
    choice = random.randint(1, 100) % 2

    plainTxt = os.urandom(random.randint(5, 10)) + plainTxt + os.urandom(random.randint(5, 10))

    if choice == 0:
        return encrypt_ecb(plainTxt, key)
    else:
        return encrypt_cbc(plainTxt, key, iv)


def encryption_oracle_ecb(plainTxt):
    # constant but unknown key
    key = "UUPSRYIQXIKACKGA"
    return encrypt_ecb(plainTxt, key)


def encryption_oracle_ecb2(pre, plaintxt):
    # constant but unknown key
    key = "UUPSRYIQXIKACKGA"
    return encrypt_ecb(pre+plaintxt, key)


if __name__ == '__main__':
    print encryption_oracle("HELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLDHELLO WORLD")
