from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
#KELOMPOK 1
"""
Bagas Aditya pramudana			(V3920012) 
Dion Aji cahyono				(V3920018) 
Isnan Nur Ahmad Wijayakusuma	(V3920029)
Ivan Fausta Dinata				(V3920030) 
Kreshna Pura Adi Wicaksana		(V3920032) 
"""

#Sintak b untuk bytes. Panjang n byte block 
key = b'23tfwk4'                
panjang_key = len(key)           #For key bytes lenght
data = b'A2g4j6F8'               #Data is convert to bytes 
panjang_data = len(data)         #For data bytes lenght

#ENKRIPSI
BLOCK_SIZE = 32                     #Ukuran blok(32 atau 64 bit)
des = DES.new(key,DES.MODE_ECB)     #DES is active
padded_txt = pad(data, BLOCK_SIZE)  #Padd txt is active
hasil1 = des.encrypt(padded_txt)    #Encrypt was used for end result1
if panjang_key <= 8 :
    if panjang_data == 8:
        print('KEY harus lebih dari 8 bit dan PESAN tidak boleh 8 bit')
    else:
        print('\nEnkripsi:',hasil1) #Result print

#DEKRIPSI
if panjang_key <= 8 :
    if panjang_data == 8:
        print('KEY harus lebih dari 8 bit dan PESAN tidak boleh 8 bit')
    else:
        BLOCK_SIZE = 32
        des = DES.new(key,DES.MODE_ECB)
        padded_txt = pad(data, BLOCK_SIZE)
        hasil2 = des.decrypt(hasil1)        #Decrypt was used for end result2 from result1 converted before it
        print("\nDekripsi:",hasil2,"\n")    #Result print