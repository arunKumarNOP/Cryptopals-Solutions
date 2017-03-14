from set1.Aes_cipher import encrypt_ecb,decrypt_ecb
import binascii

def profile_for(email):
    email = email.replace('&','').replace('=','')
    encoded = 'email={0}&uid=10&role=user'.format(email)
    enc = encrypt_ecb(encoded,'UUPSRYIQXIKACKGA')
    return binascii.hexlify(enc)


def decode_profile(enc):
    unhex = binascii.unhexlify(enc)
    dec = decrypt_ecb(unhex,'UUPSRYIQXIKACKGA')
    return dec

if __name__=='__main__':
    s = profile_for('a'*10+'admin'+'\b'*11)
    print decode_profile(s)
    admin_block = s[32:32+32]
    s2 = profile_for('a'*13)
    print decode_profile(s2)
    s3 = s2[:-32] + admin_block
    print decode_profile(s3)