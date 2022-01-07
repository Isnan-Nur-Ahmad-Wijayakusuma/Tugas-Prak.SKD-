import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

random_generator = Random.new().read
key = RSA.generate(1024, random_generator) #generate public and private keys

publickey = key.publickey() # pub key export for exchange

p = open('plaintext.txt', 'r')
pesan = p.read()

msg = bytes(pesan, 'utf-8')
encryptor = PKCS1_OAEP.new(publickey)
encrypted = encryptor.encrypt(msg)
#message to encrypt is in the above line 'encrypt this message'

print ('encrypted =', encrypted) #ciphertext

f = open ('enkripsi.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open ('enkripsi.txt', 'r')
msg2 = f.read()

decryptor = PKCS1_OAEP.new(key)
decrypted = decryptor.decrypt(ast.literal_eval(str(msg2)))

print ('decrypted = ', decrypted.decode('utf-8'))

f = open ('enkripsi.txt', 'w')
f.write(str(msg2))
f.write(str(decrypted))
f.close()