print("=====---[Vigerner Chiper]---=====") 
#Tempat menampung semua karakter(alfabet)
alfabet = "abcdefghijklmnopqrstuvwxyz"

#Encrypt funct
def Enkripsi(alfabet):
    pesan = ""                              #Membuat wadah kosong untuk isi pesan
    wordKey = ""                            #Membuat wadah kosong untuk isi kunci
    result = ""                             #Membuat wadah kosong untuk hasilnya nanti
    posisiKey = 0                           #Posisi default string
        
    #Mengambil string dr user
    pesan = input("Data pesan    : ")
    pesan = pesan.lower()               #Mengubah input menjadi lowercase
    
    #Mengambil kunci enkripsi dr user
    wordKey = input("Kunci enkripsi: ")
    wordKey = wordKey.lower()           #Mengubah input menjadi lowercase
       
    #Panjang input string
    panjang_string = len(pesan)

    #Membuat key lebih panjang dari yang diinputkan
    luas_key = wordKey
    panjang_key = len(luas_key)

    #Jika Keyword lebih pendek dari String/pesan yan diinputkan
    while panjang_key < panjang_string: 
        luas_key = luas_key + wordKey   #Menambahkan pengulangan kunci enkripsi sepanjang pesan yg diinputkan. Jadi maksdunya
        panjang_key = len(luas_key)     #adalah panjang WordKey + pesan nanti totalnya dihitung. Lalu, nantinya akan digunakan
                                        #sebagai rumus untuk loop WordKey sepanjang pesan yg diinputkan.
    for char in pesan:
        if char in alfabet:                          #Memecah string menjadi satu2 dan pengecekan ada tidaknya karakter dalam pesan
            posisi         = alfabet.find(char)      #Jika ada, maka cari nilai indexnya
            key_char       = luas_key[posisiKey]     #Mengkonversi panjang Keynya dengan nilai default 0
            keyChar_posisi = alfabet.find(key_char)  #Untuk mengetahui posisi WordKey pada array Alfabet
            posisiKey      = posisiKey + 1           #Posisi Key bertambah seiring panjangnya pesan yg diinputkan
            posisiBaru     = posisi + keyChar_posisi #Lalu dibuat rumus(posisiBaru) penjumlahan posisi(index) pesan & WordKeynya
            
            if posisiBaru > 26:               #Jika posisi barunya lebih besar dari karakter yang ditampung variabel alfabet
                posisiBaru = posisiBaru - 26  #Maka akan dikurangin dengan jumlah karakter yang terdapat di variabel alfabet
            newChar= alfabet[posisiBaru]      #Mengkonversi index ke karakter pada variabel alfabet
            result  = result + newChar        #Jika ada, maka dikonversi menjadi karakter yang ada di variabel alfabet sesuai index
        else:
            result = result + "@%"            #Mengkonversi menjadi karakter @% jika tidak terdapat dalam array alfabet.
    #Hasil                                    #Jadi ini digunakan untuk mengkonversi spasi dalam pesan
    print(f"<---------------------------------->\nHasil program enkripsi\nData pesan\t: {pesan}\nEnkripsi pesan\t: {result}")  

#Decrypt funct
def Dekripsi(alfabet):
    pesan = ""          #Membuat wadah kosong untuk isi pesan
    wordKey = ""        #Membuat wadah kosong untuk isi kunci
    result = ""         #Membuat wadah kosong untuk hassilnya nanti
    posisiKey = 0       #Posisi default string
        
    #Mengambil string dr user
    pesan = input("Pesan terenkripsi: ")
    pesan = pesan.lower()               #Mengubah input menjadi lowercase
    
    #Mengambil kunci enkripsi dr user
    wordKey = input("Kunci enkripsi  : ")
    wordKey = wordKey.lower()           #Mengubah input menjadi lowercase
       
    #Panjang input string
    panjang_string = len(pesan)

    #Membuat key lebih panjang dari yang diinputkan
    luas_key = wordKey
    panjang_key = len(luas_key)

    #Jika Keyword lebih pendek dari String/pesan yan diinputkan
    while panjang_key < panjang_string: 
        luas_key = luas_key + wordKey   #Menambahkan pengulangan kunci enkripsi sepanjang pesan yg diinputkan. Jadi maksdunya
        panjang_key = len(luas_key)     #adalah panjang WordKey + pesan nanti totalnya dihitung. Lalu, nantinya akan digunakan
                                        #sebagai rumus untuk loop WordKey sepanjang pesan yg diinputkan.
    for char in pesan:
        if char in alfabet:                          #Memecah string menjadi satu2 dan pengecekan ada tidaknya karakter dalam pesan
            posisi         = alfabet.find(char)      #Jika ada, maka cari nilai indexnya
            key_char       = luas_key[posisiKey]     #Mengkonversi panjang Keynya dengan nilai default 0
            keyChar_posisi = alfabet.find(key_char)  #Untuk mengetahui posisi WordKey pada array Alfabet
            posisiKey      = posisiKey + 1           #Posisi Key bertambah
            posisiBaru     = posisi - keyChar_posisi #Lalu dibuat rumus(posisiBaru) pengurangan posisi(index) pesan & WordKeynya
            
            if posisiBaru > 26:               #Jika posisi barunya lebih besar dari karakter yang ditampung variabel alfabet
                posisiBaru = posisiBaru + 26  #Maka akan ditambah dengan jumlah karakter yang terdapat di variabel alfabet
            newChar= alfabet[posisiBaru]      #Mengkonversi index ke karakter pada variabel alfabet
            result  = result + newChar        #Jika ada, maka dikonversi menjadi karakter yang ada di variabel alfabet sesuai index
        else:
            result = result + " "            #Mengkonversi menjadi karakter spasi jika tidak terdapat dalam array alfabet.
    #Hasil                                   #Jadi ini mengkonversi @% menjadi spasi dalam pesan    
    print(f"<---------------------------------->\nHasil program enkripsi\nData pesan\t: {pesan}\nDekripsi pesan\t: {result}")  
    

#Menu PROGRAM
pilihan = 'y'
while (pilihan == 'Y' or pilihan == 'y'):   #If you choose 'y' or 'Y', this menu script will be execute again
    print("Menu yang tersedia:\nA.Enkripsi pesan\nB.Dekripsi pesan\nC.Keluar dari program")
    menu = input("Pilih: ")
    print("__________________________________")
           
    if menu == 'A' or menu == 'a':      #Choose menu a
        print("Menu enkripsi pesan\n----------------------------------")
        Enkripsi(alfabet)                      #Menjalankan Encryp funct
    elif menu == 'B' or menu == 'b':    #Choose menu b
        print("Menu dekripsi pesan")
        Dekripsi(alfabet)                      #Menjalankan Decrypt funct
    elif menu == 'C' or menu == 'c':    #Choose menu c, will be what?? Exactly,it will be done or close program
        print("!!---!!---[Program selesai]---!!---!!")
        break;
    else:
        print("Menu tidak tersedia")
           
    print("==================================")
    pilihan = input("Apakah ingin mengulangi?(Y/N): ")  #Setelah menjalankan program, akan ditanya
    if pilihan == 'n' or pilihan == "N":                #This script will be execute
        print("\n!!---!!---[Program selesai]---!!---!!\n")

#Penjelasan HASIL
"""
Plain_txt       : Isnan Nur Ahmad Wijayakusuma
Word_Key        : Magetan
Enkrpsi/Cipher  : usteg@%nhd@%anqtd@%jujgctkheuse
"""
