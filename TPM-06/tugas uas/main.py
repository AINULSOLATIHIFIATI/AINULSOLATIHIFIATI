def hitung_diskon(total_belanja, is_member):
    if is_member:  # Jika pelanggan memiliki kartu member
        if total_belanja > 500000:
            diskon_persen = 10
        elif total_belanja >= 100000:
            diskon_persen = 0  # Tidak ada diskon jika belanja antara 100.000 - 499.999
        else:
            diskon_persen = 3
    else:  # Jika pelanggan tidak memiliki kartu member
        if total_belanja > 100000:
            diskon_persen = 3
        else:
            diskon_persen = 3

    # Menghitung diskon dalam rupiah
    diskon_rupiah = total_belanja * diskon_persen / 100
    
    # Menghitung total belanja setelah diskon
    total_belanja_after = total_belanja - diskon_rupiah
    
    return diskon_persen, diskon_rupiah, total_belanja_after

def tampilkan_hasil(nama_pelanggan, is_member, total_belanja):
    # Mendapatkan diskon dan total belanja setelah potongan
    diskon_persen, diskon_rupiah, total_belanja_after = hitung_diskon(total_belanja, is_member)
    
    # Menampilkan hasil sesuai dengan format yang diminta
    print("Nama Pelanggan        :", nama_pelanggan)
    print("Status Kartu Member   :", "Member" if is_member else "Non-Member")
    print("Total Belanja Sebelum Potongan  :", total_belanja)
    print("Diskon (Dalam Persen)  :", diskon_persen, "%")
    print("Diskon (Dalam Rupiah)  :", diskon_rupiah)
    print("Total Belanja Setelah Potongan:", total_belanja_after)

# Input data pelanggan
nama_pelanggan = input("Masukkan Nama Pelanggan: ")
status_member = input("Apakah pelanggan memiliki kartu member (ya/tidak)? ").strip().lower()

# Menentukan apakah pelanggan member atau tidak
is_member = status_member == 'ya'

# Input total belanja
total_belanja = float(input("Masukkan Total Belanja: "))

# Tampilkan hasil
tampilkan_hasil(nama_pelanggan, is_member, total_belanja)