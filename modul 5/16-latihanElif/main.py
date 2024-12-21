def tentukan_nilai(nilai):
    # Memeriksa nilai dan mengembalikan huruf sesuai kriteria
    if nilai > 90:
        return 'A'  # Nilai di atas 90
    elif 81 <= nilai <= 90:
        return 'B'  # Nilai antara 81 sampai 90
    elif 75 <= nilai <= 80:
        return 'C'  # Nilai antara 75 sampai 80
    elif 70 <= nilai <= 74:
        return 'D'  # Nilai antara 70 sampai 74
    elif 65 <= nilai <= 69:
        return 'E'  # Nilai antara 65 sampai 69
    elif 55 <= nilai <= 64:
        return 'F'  # Nilai antara 55 sampai 64
    else:
        return 'G'  # Nilai di bawah 55

# Input nilai dari pengguna
