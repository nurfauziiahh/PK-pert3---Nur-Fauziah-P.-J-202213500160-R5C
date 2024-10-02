def cek_sisi(sisi1, sisi2, sisi3):
    # Memeriksa apakah semua sisi sama
    if sisi1 == sisi2 == sisi3:
        print("3 sisi sama")
    # Memeriksa apakah dua sisi yang sama
    elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
        print("2 sisi sama")
    # Jika tidak ada yang sama
    else:
        print("Tidak ada yang sama")

# Meminta input dari pengguna dengan penanganan kesalahan
try:
    sisi1 = int(input("Masukkan sisi 1: "))
    sisi2 = int(input("Masukkan sisi 2: "))
    sisi3 = int(input("Masukkan sisi 3: "))

    # Memeriksa apakah nilai sisi positif
    if sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0:
        print("Input tidak valid. Semua sisi harus bernilai positif.")
    else:
        cek_sisi(sisi1, sisi2, sisi3)
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")