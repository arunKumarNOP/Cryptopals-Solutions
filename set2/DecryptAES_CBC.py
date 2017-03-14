from set1.Aes_cipher import *


cipherTxt = base64.decodestring(open('10.txt').read().replace('\n', ''))
key = 'YELLOW SUBMARINE'
iv = ''.join(['\0']*16)
print decrypt_cbc(cipherTxt,key,iv)