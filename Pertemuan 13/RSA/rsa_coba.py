import rsa #import library python

def generate_keys(): # kunci
    (pubKey, privKey) = rsa.newkeys(1024)
    with open('keys/pubkey.pem', 'wb') as f:
        f.write(pubKey.save_pkcs1('PEM')) # public key

    with open('keys/privkey.pem', 'wb') as f:
        f.write(privKey.save_pkcs1('PEM')) # private key

def load_keys(): # untuk load kunci
    with open('keys/pubkey.pem', 'rb') as f:
        pubKey = rsa.PublicKey.load_pkcs1(f.read())

    with open('keys/privkey.pem', 'rb') as f:
        privKey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubKey, privKey

def encrypt(msg, key): # fungsi enskripsi
    return rsa.encrypt(msg.encode('ascii'), key)

def decrypt(ciphertext, key): # fungsi dekkripsi
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False

def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'), key, 'SHA-1')

def verify_sha1(msg, signature, key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

generate_keys()
pubKey, privKey = load_keys()

pesan = input('Masukan Pesan:')
ciphertext = encrypt(pesan, pubKey)

signature = sign_sha1(pesan, privKey)

plaintext = decrypt(ciphertext, privKey)

print(f'Cipher text: {ciphertext}')
print('==================================================================')
print(f'Signature: {signature}')

if plaintext:
    print(f'Plain text: {plaintext}')
else:
    print('Tidak dapat melakukan deskripsi.')

if verify_sha1(plaintext, signature, pubKey):
    print('signature terverifikasi!')
else:
    print('tidak bisa melakukan verifikasi pesan signature.')

