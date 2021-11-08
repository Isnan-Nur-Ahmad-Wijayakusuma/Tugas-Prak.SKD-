#Fungsi egcd dengan var a dan b
def egcd(a, b):
  x,y, u,v = 0,1, 1,0

  while a != 0:                   #Jika var a tidak sama dengan 0
    q, r = b//a, b%a              #Mendeklarasikan objek
    m, n = x-u*q, y-v*q
    b,a, x,y, u,v = a,r, u,v, m,n
  gcd = b
  return gcd, x, y      #Mengembalikan nilai gcd, x, dan y
 

#Fungsi modivn pada variabel a dan m 
def modinv(a, m):
  gcd, x, y = egcd(a, m)

  if gcd != 1:          #Jika gcd tidak sama dengan 1, maka mengembalikan nilainya berupa None
    return None         
  else:                 
    return x % m        #Mengembalikan nilai x mod m
 

#Fungsi Enkripsi
def Enkripsi():
  pesan = input("Data pesan\t: ")       #Input pesan yg akan dienkripsi
  n1    = int(input("Kunci A\t\t: "))   #Input kunci angka yg nantinya akan dimasukkan dalam list bernama key pada indeks 0 
  n2    = int(input("Kunci B\t\t: "))   #Input kunci angka yg nantinya akan dimasukkan dalam list bernama key pada indeks 1
  key   = [n1, n2]                      #List bernama key
  
  #Menampung perhitungan rumus Alfine Cipher 'C = (a*P + b)%26' dalam var hasil1.  Intinya mencari index dan perhitungan kunci pada pesan
  hasil1= ''.join([chr( ( (key[0]*(ord(t) - ord('A')) + key[1]) % 26 ) + ord('A') ) for t in pesan.upper().replace(' ', '') ])
  #Mencetak hasil akhir, data pesan dan kuncinya
  print(f"<---------------------------------->\nHasil program enkripsi\nData pesan\t: {pesan}\nKunci A & B\t:{key}\nEnkripsi pesan\t: {hasil1}") 

 
#Fungsi Dekripsi
def Dekripsi():
  pesan = input("Pesan terenkripsi: ")  #Input pesan yg telah dienkripsi
  n1    = int(input("Kunci A\t\t: "))   #Input kunci angka yg nantinya akan dimasukkan dalam list bernama key pada indeks 0 
  n2    = int(input("Kunci B\t\t: "))   #Input kunci angka yg nantinya akan dimasukkan dalam list bernama key pada indeks 1
  key   = [n1, n2]                      #List bernama key

  #Menampung perhitungan rumus Alfine Cipher 'P = (a^-1*(C - b))%26' dalam var hasil2. Intinya mencari index dan perhitungan kunci pada pesan terenkripsi
  hasil2 = ''.join([chr( ( (modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))% 26 ) + ord('A') ) for c in pesan ])
  #Mencetak hasil akhir, data pesan dan kuncinya
  print(f"<---------------------------------->\nHasil program enkripsi\nData pesan\t: {pesan}\nKunci A & B\t:{key}\nDekripsi pesan\t: {hasil2}") 


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