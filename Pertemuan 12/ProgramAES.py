from Crypto.Cipher import AES

data = b'praktikum sistem keamanan data'
key = b'5i5t3mKeam4n4nDa' #16 blok kunci karena menggunakan AES 128

#enskripsi
chipher = AES.new(key, AES.MODE_EAX)
nonce = chipher.nonce
chipherText, tag = chipher.encrypt_and_digest(data)

print(" Hasil Enskripsi yaitu baris paling atas")
print("========================================")
print('Enkripsi     = ',chipherText,'\n','Nonce     = ',tag, '\n',nonce, '\n')

#deskripsi
key = b'5i5t3mKeam4n4nDa'
chipher = AES.new(key, AES.MODE_EAX, nonce)
plainteks = chipher.decrypt(chipherText)
try: 
    chipher.verify(tag)
   
    print("Hasil deskripsi adalah")
    print("========================================")
    print("Dekripsi = ",plainteks.decode())
except ValueError:
    print("Terdapat kunci yang salah")