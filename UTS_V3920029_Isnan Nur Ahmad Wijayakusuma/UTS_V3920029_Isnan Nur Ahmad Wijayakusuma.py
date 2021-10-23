print("=====[Encrypt & Decrypt]=====")
#ini adalah tempat menampung alfabet a-z
alfabet = "abcdefghijklmnopqrstuvwxyz"

def enkrips(alfabet):          #Membuat fungsi Enkripsi
    #[--------------------------<===CAESAR CHIP===>--------------------------]
    str = input("Pesan\t\t: ")     #input pesan yang ingin dienkripsi
    key = int(input("Kunci angka\t: ")) #input key
    str = str.lower()           #merubah semua input jadi Lower Case
    result1=""                   #Wadah kosong untuk hasilnya nanti

    for char in str:                    
        if char in alfabet:               #Memecah string menjadi satu2 dan pengecekan ada tidaknya karakter dalam string
            n = alfabet.index(char)       #Jika ada, maka cari nilai indexnyas
            enkrip = (n + key) % 26     #Rumus enkripsi
            convert = alfabet[enkrip]     #konversi string ke hasil enkripsi
            result1 = result1 + convert   #Jika ada, maka dikonversi menjadi karakter dalam array alfabet
        else:
            result1 = result1 + " "       #Mengkonversi menjadi karakter spasi jika tidak terdapat dalam array alfabet.
            
    #[-------------------------<===VIGENERE CHIP===>-------------------------]
    result2=""                   #Wadah kosong untuk hasilnya nanti
    posisiKey = 0                           #Posisi default string
    
    #Mengambil kunci enkripsi dr user
    wordKey = input("Kunci kata/huruf: ")
    wordKey = wordKey.lower()           #Mengubah input menjadi lowercase
       
    #Panjang input string
    panjang_string = len(result1)

    #Membuat key lebih panjang dari yang diinputkan
    luas_key = wordKey
    panjang_key = len(luas_key)

    #Jika Keyword lebih pendek dari String/pesan yan diinputkan
    while panjang_key < panjang_string: 
        luas_key = luas_key + wordKey   #Menambahkan pengulangan kunci enkripsi sepanjang pesan yg diinputkan. Jadi maksdunya
        panjang_key = len(luas_key)     #adalah panjang WordKey + pesan nanti totalnya dihitung. Lalu, nantinya akan digunakan
                                        #sebagai rumus untuk loop WordKey sepanjang pesan yg diinputkan.
    for char in result1:
        if char in alfabet:                          #Memecah string menjadi satu2 dan pengecekan ada tidaknya karakter dalam pesan
            posisi         = alfabet.find(char)      #Jika ada, maka cari nilai indexnya
            key_char       = luas_key[posisiKey]     #Mengkonversi panjang Keynya dengan nilai default 0
            keyChar_posisi = alfabet.find(key_char)  #Untuk mengetahui posisi WordKey pada array Alfabet
            posisiKey      = posisiKey + 1           #Posisi Key bertambah seiring panjangnya pesan yg diinputkan
            posisiBaru     = posisi + keyChar_posisi #Lalu dibuat rumus(posisiBaru) penjumlahan posisi(index) pesan & WordKeynya
            
            if posisiBaru > 26:               #Jika posisi barunya lebih besar dari karakter yang ditampung variabel alfabet
                posisiBaru = posisiBaru - 26  #Maka akan dikurangin dengan jumlah karakter yang terdapat di variabel alfabet
            newChar= alfabet[posisiBaru]      #Mengkonversi index ke karakter pada variabel alfabet
            result2  = result2 + newChar        #Jika ada, maka dikonversi menjadi karakter yang ada di variabel alfabet sesuai index
        else:
            result2 = result2 +  " "          #Mengkonversi menjadi karakter @% jika tidak terdapat dalam array alfabet.
                                              #Jadi ini digunakan untuk mengkonversi spasi dalam pesan
    print(f"\n<---------------------------------->\n[Hasil program enkripsi]")
    print(f"Data pesan\t: {str}\nEnkripsi 1\t: {result1}\nEnkripsi 2\t: {result2}")  


#Untuk fungsi deskripsi, hirarki dan kodenya sama dengan fungsi enkripsi, cuman beda rumus saja
def dekrips(alfabet):
    #[-------------------------<===CAESAR CHIP===>-------------------------]
    str = input("Pesan terenkripsi: ")
    key = int(input("Kunci angka\t: "))
    str = str.lower()
    result1=""

    for char in str:
        if char in alfabet:
            n = alfabet.index(char)
            dekrip = (n - key) % 26     #Rumus deskripsi
            convert = alfabet[dekrip]
            result1 = result1 + convert
        else:
            result1 = result1 + " "

    
    #[--------------------------<===VIGENERE CHIP===>--------------------------]
    result2 = ""         #Membuat wadah kosong untuk hassilnya nanti
    posisiKey = 0       #Posisi default string
    
    #Mengambil kunci enkripsi dr user
    wordKey = input("Kunci enkripsi  : ")
    wordKey = wordKey.lower()           #Mengubah input menjadi lowercase
       
    #Panjang input string
    panjang_string = len(result1)

    #Membuat key lebih panjang dari yang diinputkan
    luas_key = wordKey
    panjang_key = len(luas_key)

    #Jika Keyword lebih pendek dari String/pesan yan diinputkan
    while panjang_key < panjang_string: 
        luas_key = luas_key + wordKey   #Menambahkan pengulangan kunci enkripsi sepanjang pesan yg diinputkan. Jadi maksdunya
        panjang_key = len(luas_key)     #adalah panjang WordKey + pesan nanti totalnya dihitung. Lalu, nantinya akan digunakan
                                        #sebagai rumus untuk loop WordKey sepanjang pesan yg diinputkan.
    for char in result1:
        if char in alfabet:                          #Memecah string menjadi satu2 dan pengecekan ada tidaknya karakter dalam pesan
            posisi         = alfabet.find(char)      #Jika ada, maka cari nilai indexnya
            key_char       = luas_key[posisiKey]     #Mengkonversi panjang Keynya dengan nilai default 0
            keyChar_posisi = alfabet.find(key_char)  #Untuk mengetahui posisi WordKey pada array Alfabet
            posisiKey      = posisiKey + 1           #Posisi Key bertambah
            posisiBaru     = posisi - keyChar_posisi #Lalu dibuat rumus(posisiBaru) pengurangan posisi(index) pesan & WordKeynya
            
            if posisiBaru > 26:               #Jika posisi barunya lebih besar dari karakter yang ditampung variabel alfabet
                posisiBaru = posisiBaru + 26  #Maka akan ditambah dengan jumlah karakter yang terdapat di variabel alfabet
            newChar= alfabet[posisiBaru]      #Mengkonversi index ke karakter pada variabel alfabet
            result2  = result2 + newChar      #Jika ada, maka dikonversi menjadi karakter yang ada di variabel alfabet sesuai index
        else:
            result2 = result2 + " "          #Mengkonversi menjadi karakter spasi jika tidak terdapat dalam array alfabet.
    #Hasil                                   #Jadi ini mengkonversi @% menjadi spasi dalam pesan    
    print(f"\n<---------------------------------->\n[Hasil program dekripsi]")
    print(f"Pesan terenkripsi\t: {str}\nEnkripsi 1\t: {result1}\nEnkripsi 2\t: {result2}")  


#Menu PROGRAM
pilihan = 'y'
while (pilihan == 'Y' or pilihan == 'y'):   #If you choose 'y' or 'Y', this menu script will be execute again
    print("Menu yang tersedia:\nA.Enkripsi pesan\nB.Dekripsi pesan\nC.Keluar dari program")
    menu = input("Pilih: ")
    print("----------------------------")

    if menu == 'A' or menu == 'a':          #Choose menu a
        print("Menu enkripsi pesan")
        enkrips(alfabet)                    #Menjalankan Encryp funct
    elif menu == 'B' or menu == 'b':        #Choose menu b
        print("Menu dekripsi pesan")
        dekrips(alfabet)                    #Menjalankan Decrypt funct
    elif menu == 'C' or menu == 'c':        #Choose menu c
        print("!!-----Program selesai-----!!")
        break;
    else:
        print("Menu tidak tersedia")

    print("\n\na=================================")
    pilihan = input("Apakah ingin mengulangi?(Y/N): ")  #Setelah menjalankan program, akan ditanya
    if pilihan == 'n' or pilihan == "N":                #This script will be execute
        print("\n!!-----Program selesai-----!!\n")

