from set2.EncryptionAES import encryption_oracle


def detectMode():
    plaintxt = 'a'*16*3
    cipher = encryption_oracle(plaintxt)

    if cipher[16:32] == cipher[32:48]:
        return 'ECB'
    else:
        return 'CBC'

if __name__=='__main__':
    for i in range(10):
        print detectMode()