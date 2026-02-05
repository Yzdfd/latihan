paket_a = 150000
paket_b = 187000
paket_c = 145000
paket_d = 210000
paket_e = 192000
es_teh_manis = 8000
milo = 12000
matcha = 32000
amerikano = 22000
total = 0
menu = []
nama_menu = []
jumlah_barang = []

# Catatan : setiap pembelian diatas Rp 300.000,- akan mendapatkan diskon 5%, jika diatas Rp 500.000,- akan mendapat 10% diskon dari total belanja

def show_menu():
    print("==============Menu==============")
    print("1. Paket A          Rp 150.000,-")
    print("2. Paket B          Rp 187.000,-")
    print("3. Paket C          Rp 145.000,-")
    print("4. Paket D          Rp 210.000,-")
    print("5. Paket E          Rp 192.000,-")
    print("=============Minumm=============")
    print("6. Es Teh Manis     Rp   8.000,-")
    print("7. Milo             Rp  12.000,-")
    print("8. Matcha           Rp  32.000,-")
    print("9. Amerikano        Rp  22.000,-")
    print("================================")

def struk_belanja():
    print("\n=========== STRUK BELANJA ==========")
    print("No  Nama Menu        Qty     Subtotal")

    total = 0
    for i in range(len(menu)):
        print(f"{i+1}.  {nama_menu[i]:17} {jumlah_barang[i]}   Rp {menu[i]:,}")
        total += menu[i]

    print("------------------------------------")
    print(f"Total Belanja : Rp {total:,}")

    # Hitung diskon
    diskon = 0
    if total > 500000:
        diskon = total * 0.10
    elif total > 300000:
        diskon = total * 0.05

    if diskon > 0:
        print(f"Diskon        : Rp {int(diskon):,}")
        total -= diskon

    print("------------------------------------")
    print(f"Total Bayar   : Rp {int(total):,}")
    print("====================================")
    print("Terima kasih sudah berbelanja 🙏")
   
while True :
    show_menu()
    barang = input("Masukan Nomor barang : ")
    if barang == "1":
        jumlah = int(input("Masukan Jumlah barang : ")) 
        jumlah_barang.append(jumlah)
        menu.append(paket_a * jumlah)
        nama_menu.append("Paket A")
        print("Barang Telah ditambahkan !")
    elif barang == "2":
        jumlah = int(input("Masukan Jumlah barang : ")) 
        jumlah_barang.append(jumlah)
        menu.append(paket_b * jumlah)
        nama_menu.append("Paket B")
        print("Barang Telah ditambahkan !")
    elif barang == "3":
        jumlah = int(input("Masukan Jumlah barang : ")) 
        jumlah_barang.append(jumlah)
        menu.append(paket_c * jumlah)
        nama_menu.append("Paket C")
        print("Barang Telah ditambahkan !")
    elif barang == "4" :
        jumlah = float(input("Masukan Jumlah barang : "))
        jumlah_barang.append(jumlah)
        menu.append(paket_d * jumlah)
        nama_menu.append("Paket D")
        print("Barang Telah ditambahkan !")
    elif barang == "5":
        jumlah = float(input("Masukan Jumlah bara ng : "))
        jumlah_barang.append(jumlah)
        menu.append(paket_e * jumlah)
        nama_menu.append("Paket E")
        print("Barang Telah ditambahkan !")
    elif barang == "6":
        jumlah = float(input("Masukan Jumlah bara ng : "))
        jumlah_barang.append(jumlah)
        menu.append(es_teh_manis * jumlah)
        nama_menu.append("Es Teh Manis")
        print("Barang Telah ditambahkan !")
    elif barang == "7":
        jumlah = float(input("Masukan Jumlah bara ng : "))
        jumlah_barang.append(jumlah)
        menu.append(milo * jumlah)
        nama_menu.append("Milo")
        print("Barang Telah ditambahkan !")
    elif barang == "8":
        jumlah = float(input("Masukan Jumlah bara ng : "))
        jumlah_barang.append(jumlah)
        menu.append(matcha * jumlah)
        nama_menu.append("Matcha")
        print("Barang Telah ditambahkan !")
    elif barang == "9":
        jumlah = float(input("Masukan Jumlah bara ng : "))
        jumlah_barang.append(jumlah)
        menu.append(amerikano * jumlah)
        nama_menu.append("Amerikano")
        print("Barang Telah ditambahkan !")
    elif barang == "p" or "P" & jumlah == "":
        struk_belanja()
        break