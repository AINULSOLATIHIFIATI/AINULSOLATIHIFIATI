# percabangan 
# percabangan 1 kondisi

# struktur percabangan 
"""
   1. if-nya
   2. kondisinya, statement yang harus di terpenuhi agar aksi dijalankan
   3. aksinya
"""

nama = input("masukkan nama anda !")

# percabangan inline
# if <kondisi> : <aksi>
if nama == "ainul" : print("selamat datang")
print("terima kasih") # bukan aksi

# percabangan dengan indensitas
if nama == "ainul" : # kondisi
    print("selamat datang") # aksi
    print("selamat belajar") # aksi
print("terima kasih") # bukan aksi


# percabangan dengan else statement
if nama == "ainul" :
    print("selamat datang")
else :
    print("anda bukan ainul")
print("program berakhir")