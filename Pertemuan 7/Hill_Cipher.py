import numpy as np
from egcd import egcd  #instal paket terlebih dahulu dengan 'pip install egcd'
#ini adalah tempat menampung abjad abjad a-z
alfabet = "abcdefghijklmnopqrstuvwxyz"

#Ubtuk operasi konversi var index dan letter
letter_to_index = dict(zip(alfabet, range(len(alfabet))))
index_to_letter = dict(zip(range(len(alfabet)), alfabet))

#Fungsi untuk mencari matriks modulus inverse.
def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))      #Cari determinan
    det_inv = egcd(det, modulus)[1] % modulus       #Temukan nilai determinan dalam modulus tertentu(panjang alfabet)
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus)  #Lalu det_inv dikali matriks determin terbalik(akan menjadi adjoint) di mod 26

    return matrix_modulus_inv


def Enkripsi():
    pesan       =str(input("Data pesan\t: "))      #Input pesan berupa String
    result      = ""
    pesan_numb  = []
    n1  = int(input("Matrik 1\t: "))   #Input Matrik angka yg nantinya akan dimasukkan dalam list bernama K pada indeks 0 
    n2  = int(input("Matrik 2\t: "))   #Input Matrik angka yg nantinya akan dimasukkan dalam list bernama K pada indeks 1
    n3  = int(input("Matrik 3\t: "))   #Input Matrik angka yg nantinya akan dimasukkan dalam list bernama K pada indeks 2
    n4  = int(input("Matrik 4\t: "))   #Input Matrik angka yg nantinya akan dimasukkan dalam list bernama K pada indeks 3
    K = np.matrix([[n1,n2], [n3,n4]])
    Kinv = matrix_mod_inv(K, len(alfabet))

    #Untuk var letter pd pesan
    for letter in pesan:
        pesan_numb.append(letter_to_index[letter])

    #Memisahkan karakter
    split_P = [
        pesan_numb[i : i + int(K.shape[0])]
        for i in range(0, len(pesan_numb), int(K.shape[0]))
    ]
    #Untuk var P dalam var split_p
    for P in split_P:
        P = np.transpose(np.asarray(P))[:, np.newaxis]             #P = Mentranspose nilai 
        while P.shape[0] != K.shape[0]:
            P = np.append(P, letter_to_index[" "])[:, np.newaxis]

        numbers = np.dot(K, P) % len(alfabet)                      
        n = numbers.shape[0]                                       #Panjang pesan(angka)

        #Pemetaan indeks untuk result pesan
        for idx in range(n):
            number = int(numbers[idx, 0])
            result += index_to_letter[number]

    print(f"<---------------------------------->\nHasil program enkripsi\nData pesan\t: {pesan}\nKunci matriks\t:{K}\nEnkripsi pesan\t: {result}") 


def Dekripsi():
    pesan       =str(input("Data terenkripsi: "))      #Input pesan berupa String
    result     = ""                    #Wadah hasilnya
    cipher_numb = []                   #Wadah cipertxt
    n1  = int(input("Matrik 1\t: "))   #Input Matrik angka yg nantinya akan dimasukkan dalam list bernama K pada indeks 0 
    n2  = int(input("Matrik 2\t: "))   #Input Matrik angka yg nantinya akan dimasukkan dalam list bernama K pada indeks 1
    n3  = int(input("Matrik 3\t: "))   #Input Matrik angka yg nantinya akan dimasukkan dalam list bernama K pada indeks 2
    n4  = int(input("Matrik 4\t: "))   #Input Matrik angka yg nantinya akan dimasukkan dalam list bernama K pada indeks 3
    K = np.matrix([[n1,n2], [n3,n4]])  #Matriks 2x2
    Kinv = matrix_mod_inv(K, len(alfabet))

    #Untuk var letter pd pesan
    for letter in pesan:
        cipher_numb.append(letter_to_index[letter])

    #Memisahkan karakter
    split_C = [
        cipher_numb[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_numb), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alfabet)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            result += index_to_letter[number]

    print(f"<---------------------------------->\nHasil program enkripsi\nPesan terenkripsi: {pesan}\nKunci matriks\t :{K}\nDekripsi pesan\t : {result}") 

#K = Matriks yang merupakan 'key' yang digunakan
#P = Vektor plaintext (dipetakan dlm angka)
#C = Vektor ciphertext(dipetakan dlm angka)
""""
[RUMUS]
C => E(K,P) = K*P (mod X) dan X adalah panjang alfabet yang digunakan
P => D(K,C) = inv(K)*C (mod X) dan X adalah panjang alfabet yang digunakan
"""

#Menu PROGRAM
pilihan = 'y'
while (pilihan == 'Y' or pilihan == 'y'):   #If you choose 'y' or 'Y', this menu script will be execute again
    print("Menu yang tersedia:\nA.Enkripsi pesan\nB.Dekripsi pesan\nC.Keluar dari program")
    menu = input("Pilih: ")
    print("__________________________________")
           
    if menu == 'A' or menu == 'a':      #Choose menu a
        print("Menu enkripsi pesan\n----------------------------------")
        Enkripsi()                      #Menjalankan Encryp funct
    elif menu == 'B' or menu == 'b':    #Choose menu b
        print("Menu dekripsi pesan")
        Dekripsi()                      #Menjalankan Dekripsi funct
    elif menu == 'C' or menu == 'c':    #Choose menu c, will be what?? Exactly,it will be done or close program
        print("!!---!!---[Program selesai]---!!---!!")
        break;
    else:
        print("Menu tidak tersedia")
           
    print("\n==================================")
    pilihan = input("Apakah ingin mengulangi?(Y/N): ")  #Setelah menjalankan program, akan ditanya
    if pilihan == 'n' or pilihan == "N":                #This script will be execute
        print("\n!!---!!---[Program selesai]---!!---!!\n")