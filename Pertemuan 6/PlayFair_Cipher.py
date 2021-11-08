key=input("[KUNCI]\t: ")      #Input kunci berupa String
key=key.replace(" ", "")        #Untuk memisahkan
key=key.upper()                 #Merubah uppercase
result=list()                   #Membuat wadah berupa list
   
#Menyimpan kunci
for c in key:
    if c not in result:         #Jika var c tdk ada pd hasil
        if c=='J':              #Jika var c = huruf J
            result.append('I')  #Hasilnya ditambahi huruf I
        else:
            result.append(c)    #Jika tidak, Hasilnya ditambahi var c

#Menyimpan karakter lainnya
flag=0
for i in range(65,91):                      #Untuk var i dalam range 65-91. Ini adalah ASCII A-Z
    if chr(i) not in result:                #Jika karakter i tdk ada pada hasilnya
        if i==73 and chr(74) not in result: #Jika i = 73 dan karakter 74 tdk ada dalam hasil
            result.append("I")              #Hasilnya ditambahi huruf I
            flag=1                          
        elif flag==0 and i==73 or i==74:
            pass    
        else:
            result.append(chr(i))

#Fungsi matrix dengan 3 parameter
def matrix(x,y,initial):                                    
    #Mengembalikan nilai pada parameter [initial untuk i dalam jarak x] untuk j pada jarak y
    return [[initial for i in range(x)] for j in range(y)]  


#Inisialisasi matrix
k=0
my_matrix=matrix(5,5,0)
for i in range(0,5):                #Membuat matrix
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1

#Fungsi lokasi index. Mendapatkan lokasi masing-masing karakter
def locindex(c):
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc

#Fungsi Enkripsi
def Enkripsi():
    pesan=str(input("Data pesan\t: "))      #Input pesan berupa String
    pesan=pesan.upper()                     #Merubah uppercase
    pesan=pesan.replace(" ", "")            #Untuk memisahkan
    
    i=0
    for s in range(0,len(pesan)+1,2):
        if s<len(pesan)-1:
            if pesan[s]==pesan[s+1]:
                pesan=pesan[:s+1]+'X'+pesan[s+1:]
    if len(pesan)%2!=0:
        pesan=pesan[:]+'X'
    print("Enkripsi pesan\t:",end=' ')
    
    while i<len(pesan):                 #Jika var i<panjang pesan
        loc=list()
        loc=locindex(pesan[i])          #Var loc menyimpan lokasi indeks pesan
        loc1=list()
        loc1=locindex(pesan[i+1])       #Var loc1 menyimpan lokasi indeks pesan dengan penambahan 1 kali
        
        #Jika var loc & loc1 indexnya sama dengan 1
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        #Jika var loc & loc1 indexnya sama dengan 0
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        #Jika tidak, maka dibawah ini yg dieksekusi
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
        
#Fungsi Enkripsi         
def Dekripsi(): 
    pesan=str(input("Pesan terenkripsi: ")) #Input pesan terenkripsi berupa String
    pesan=pesan.upper()                     #Merubah uppercase
    pesan=pesan.replace(" ", "")            #Untuk memisahkan
    print("Dekripsi pesan\t:",end=' ')
    i=0
    while i<len(pesan):                 #Jika var i<panjang pesan
        loc=list()
        loc=locindex(pesan[i])          #Var loc menyimpan lokasi indeks pesan
        loc1=list()
        loc1=locindex(pesan[i+1])       #Var loc1 menyimpan lokasi indeks pesan dengan penambahan 1 kali
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        


#Menu PROGRAM
pilihan = 'y'
while (pilihan == 'Y' or pilihan == 'y'):   #If you choose 'y' or 'Y', this menu script will be execute again
    print("\n- - - - - - - - - -")
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