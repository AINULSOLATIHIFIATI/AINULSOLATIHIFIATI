# meminta input total belanja dari pengguna
total_belanja = float(input("masukkan total belanja anda(dalam Rp):"))

# menentukan hadiah berdasarkan total belanja
if total_belanja >= 500000:
    hadiah = "mouse dan keybord"
else:
    hadiah = "gantungan kunci"

# menampilkan hasil
print(f"anda mendapatkan hadiah: {hadiah}")