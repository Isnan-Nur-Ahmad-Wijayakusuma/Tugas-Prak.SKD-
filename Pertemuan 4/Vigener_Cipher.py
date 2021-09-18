print("=====---[Vigerner Chiper]---=====") 
#Tempat menampung semua karakter(alfabet)
alfabet = "abcdefghijklmnopqrstuvwxyz"

#Encrypt funct
def Enkripsi():
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
        #Menambahkan pengulangan lain dari kunci enkripsi
        luas_key = luas_key + wordKey
        panjang_key = len(luas_key)

    for char in pesan:
        if char in alfabet:                          #Memecah string menjadi satu2 dan pengecekan ada tidaknya karakter dalam pesan
            posisi         = alfabet.find(char)      #Jika ada, maka cari nilai indexnya
            key_char       = luas_key[posisiKey]     #Konversi string asli ke hasil enkripsi
            keyChar_posisi = alfabet.find(key_char)  #Untuk mengetahui posisi suatu kata atau deret karakter tertentu pada kalimat
            posisiKey      = posisiKey + 1           #Posisi keyWord bertambah seiring panjangnya pesan yg diinputkan
            posisiBaru     = posisi + keyChar_posisi #Posisi lafabet/karakter setelah dienkripsi
            
            if posisiBaru > 26:               #Jika posisi barunya lebih besar dari karakter yang ditampung variabel alfabet
                posisiBaru = posisiBaru - 26  #Maka akan dikurangin dengan jumlah karakter yang terdapat di variabel alfabet
            newChar= alfabet[posisiBaru]      #Konversi string asli ke hasil enkripsi
            result  = result + newChar        #Jika ada, maka dikonversi menjadi karakter yang ada di variabel alfabet dengan kombinasi enkripsi
        else:
            result = result + "@%"            #Mengkonversi menjadi karakter @% jika tidak terdapat dalam array alfabet.
    #Hasil
    print(f"<---------------------------------->\nHasil program enkripsi\nData pesan\t: {pesan}\nEnkripsi pesan\t: {result}")  

#Decrypt funct
def Dekripsi():
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

    while panjang_key < panjang_string:
        #Menambahkan pengulangan lain dari kunci enkripsi
        luas_key = luas_key + wordKey
        panjang_key = len(luas_key)

    for char in pesan:
        if char in alfabet:                          #Memecah string menjadi satu2 dan pengecekan ada tidaknya karakter dalam pesa
            posisi = alfabet.find(char)              #Jika ada, maka cari nilai indexnya
            key_char = luas_key[posisiKey]           #Konversi string asli ke hasil enkripsi
            keyChar_posisi = alfabet.find(key_char)  #Untuk mengetahui posisi suatu kata atau deret karakter tertentu pada kalimat
            posisiKey= posisiKey + 1                 #Posisi keyWord bertambah seiring panjangnya pesan yg diinputkan
            posisiBaru = posisi - keyChar_posisi     #Posisi afabet/karakter setelah dienkripsi

            if posisiBaru > 26:                 #Jika posisi barunya lebih besar dari karakter yang ditampung variabel alfabet     
                posisiBaru = posisiBaru + 26    #Maka akan dijumlahkan dengan jumlah karakter yang terdapat di variabel alfabet
            newChar = alfabet[posisiBaru]       #Konversi string asli ke hasil enkripsi
            result = result + newChar           #Jika ada, maka dikonversi menjadi karakter yang ada di variabel alfabet dengan kombinasi enkripsi
        else:                                   
            result = result + " "               ##Mengkonversi menjadi karakter @% jika tidak terdapat dalam array alfabet.
    #Hasil
    print(f"<---------------------------------->\nHasil program enkripsi\nData pesan\t: {pesan}\nDekripsi pesan\t: {result}")  
    

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
        Dekripsi()                      #Menjalankan Decrypt funct
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
PLAIN TXT   : Isnan lucu
CHIPER TXT  : eojwj hqyw
"""

