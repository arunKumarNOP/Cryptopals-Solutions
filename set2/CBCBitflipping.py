import string
import random
from set1.Aes_cipher import *
from set2.PkcsPadding import pkcs7_pad_check
from set1.Xor import xorPlain

KEY = ''.join([chr(random.randint(0,255)) for i in range(16)])
IV = ''.join([chr(random.randint(0,255)) for i in range(16)])


def format_string(user_input):
    user_input = user_input.replace(';', '').replace('=', '')
    plainTxt = 'comment1=cooking%20MCs;userdata='+user_input+';comment2=%20like%20a%20pound%20of%20bacon'
    return encrypt_cbc(plainTxt, KEY, IV)


def is_admin(cipher_txt):
    decrypted = pkcs7_pad_check(decrypt_cbc(cipher_txt, KEY, IV))
    pairs = decrypted.split(';')
    if 'admin=true' in pairs:
        return True
    return False


def getBitFlippedBlock(enc_block, input_plain, desired_output):
    return xorPlain(xorPlain(input_plain,desired_output), enc_block)


if __name__ == '__main__':
    # replace d with ; and second d with =
    enc = format_string('dadmindtrue')
    print 'Before:', is_admin(str(enc))

    # https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/CBC_decryption.svg/601px-CBC_decryption.svg.png
    # we know that 'comment1=cooking%20MCs;userdata='+user_input+';comment2=%20like%20a%20pound%20of%20bacon'
    # is being encrypted so split it into block of 16 and determine in which block our input falls into.
    # Take the previous encrypted block xor with the plain input to get the output of the AES cipher of the current block
    # then xor it with the desired output and make the previous block equal to that

    # in my case it was 2nd block
    enc2 = enc[0:16] + getBitFlippedBlock(enc[16:32], 'dadmindtrue;comm', ';admin=true;comm') + enc[32:]
    print 'After:', is_admin(str(enc2))
