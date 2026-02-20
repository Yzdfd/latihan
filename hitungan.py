import math
from statistics import mean, median, mode

# Fungsi untuk menghitung volume bangun ruang
def volume_bangun_ruang():
    print("Pilih Bangun Ruang:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Bola")
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == '1':
        sisi = float(input("Masukkan panjang sisi kubus: "))
        volume = sisi ** 3
        print(f"Volume Kubus: {volume}")
    elif pilihan == '2':
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        volume = panjang * lebar * tinggi
        print(f"Volume Balok: {volume}")
    elif pilihan == '3':
        jari_jari = float(input("Masukkan jari-jari bola: "))
        volume = (4/3) * math.pi * jari_jari ** 3
        print(f"Volume Bola: {volume}")
    else:
        print("Pilihan tidak valid!")

# Fungsi untuk menghitung bangun datar
def bangun_datar():
    print("Pilih Bangun Datar:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Belah Ketupat")
    print("6. Jajar Genjang")
    print("7. Trapesium")
    print("8. Layang-Layang")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1':  # Persegi
        sisi = float(input("Masukkan panjang sisi: "))
        luas = sisi ** 2
        keliling = 4 * sisi
        print(f"Luas Persegi: {luas}")
        print(f"Keliling Persegi: {keliling}")
    elif pilihan == '2':  # Persegi Panjang
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        print(f"Luas Persegi Panjang: {luas}")
        print(f"Keliling Persegi Panjang: {keliling}")
    elif pilihan == '3':  # Segitiga
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi_a = float(input("Masukkan panjang sisi a: "))
        sisi_b = float(input("Masukkan panjang sisi b: "))
        sisi_c = float(input("Masukkan panjang sisi c: "))
        luas = 0.5 * alas * tinggi
        keliling = sisi_a + sisi_b + sisi_c
        print(f"Luas Segitiga: {luas}")
        print(f"Keliling Segitiga: {keliling}")
    elif pilihan == '4':  # Lingkaran
        jari_jari = float(input("Masukkan jari-jari: "))
        luas = math.pi * jari_jari ** 2
        keliling = 2 * math.pi * jari_jari
        print(f"Luas Lingkaran: {luas}")
        print(f"Keliling Lingkaran: {keliling}")
    elif pilihan == '5':  # Belah Ketupat
        diagonal1 = float(input("Masukkan diagonal 1: "))
        diagonal2 = float(input("Masukkan diagonal 2: "))
        sisi = float(input("Masukkan panjang sisi: "))
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 4 * sisi
        print(f"Luas Belah Ketupat: {luas}")
        print(f"Keliling Belah Ketupat: {keliling}")
    elif pilihan == '6':  # Jajar Genjang
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi = float(input("Masukkan panjang sisi miring: "))
        luas = alas * tinggi
        keliling = 2 * (alas + sisi)
        print(f"Luas Jajar Genjang: {luas}")
        print(f"Keliling Jajar Genjang: {keliling}")
    elif pilihan == '7':  # Trapesium
        sisi_a = float(input("Masukkan panjang sisi atas: "))
        sisi_b = float(input("Masukkan panjang sisi bawah: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi_c = float(input("Masukkan panjang sisi miring kiri: "))
        sisi_d = float(input("Masukkan panjang sisi miring kanan: "))
        luas = 0.5 * (sisi_a + sisi_b) * tinggi
        keliling = sisi_a + sisi_b + sisi_c + sisi_d
        print(f"Luas Trapesium: {luas}")
        print(f"Keliling Trapesium: {keliling}")
    elif pilihan == '8':  # Layang-Layang
        diagonal1 = float(input("Masukkan diagonal 1: "))
        diagonal2 = float(input("Masukkan diagonal 2: "))
        sisi_a = float(input("Masukkan panjang sisi a: "))
        sisi_b = float(input("Masukkan panjang sisi b: "))
        luas = 0.5 * diagonal1 * diagonal2
        keliling = 2 * (sisi_a + sisi_b)
        print(f"Luas Layang-Layang: {luas}")
        print(f"Keliling Layang-Layang: {keliling}")
    else:
        print("Pilihan tidak valid!")

# Fungsi untuk menghitung mean, median, modus
def hitung_statistika():
    data = list(map(float, input("Masukkan data (pisahkan dengan spasi): ").split()))
    print(f"Mean: {mean(data)}")
    print(f"Median: {median(data)}")
    try:
        print(f"Modus: {mode(data)}")
    except:
        print("Tidak ada modus yang unik.")

# Menu utama
def menu():
    print("Pilih perhitungan yang ingin dilakukan:")
    print("1. Bangun Ruang")
    print("2. Bangun Datar")
    print("3. Mean, Median, Modus")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == '1':
        volume_bangun_ruang()
    elif pilihan == '2':
        bangun_datar()
    elif pilihan == '3':
        hitung_statistika()
    else:
        print("Pilihan tidak valid!")

if _name_ == "_main_":
    while True:
        menu()
        ulang = input("Apakah ingin menghitung lagi? (y/n): ")
        if ulang.lower() != 'y':
            print("Terima kasih telah menggunakan program ini!")
            break