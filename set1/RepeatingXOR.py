from Xor import xor
import binascii

msg = binascii.hexlify("Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal")
key = binascii.hexlify("ICE")

print xor(msg,key)