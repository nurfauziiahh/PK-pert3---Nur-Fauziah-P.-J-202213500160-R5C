hari_per_bulan = {
    1: 31, #Januari
    2: 29, #Februari - tahun 2020 bukan tahun kabisat
    3: 31, #Maret
    4: 30, #April
    5: 31, #Mei
    6: 30, #Juni
    7: 31, #Juli
    8: 31, #Agustus
    9: 30, #September
    10: 31, #Oktober
    11: 30, #November
    12: 31 #Desember
}

def tampilkan_jumlah_hari():
    while True:
        try:
            bulan = int(input("Masukkan bulan (1-12): "))
            if bulan < 1 or bulan > 12:
                print("Bulan yang diinputkan tidak valid. Silakan coba lagi.")
            else:
                break
        except ValueError:
            print("Input tidak valid. Silakan masukkan angka.")

    jumlah_hari = hari_per_bulan[bulan]
    print(f" Jumlah hari: {jumlah_hari} hari")

tampilkan_jumlah_hari()