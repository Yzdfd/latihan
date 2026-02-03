mahasiswa = {}

def tampil_menu():
    print("\n====Menu====")
    print("1. Tambah Mahasiswa & Nilai")
    print("2. Tampilkan Data")
    print("3. Keluar")

def tambah_data():
    nama = input("Nama Mahasiswa : ")
    
    if nama not in mahasiswa:
        mahasiswa[nama] = []
    

    while True:
        nilai = input("Masukkan Nilai Mahasiswa (tekan q untuk keluar) : ")
        
        if nilai == 'q' :
            print("Data Tersimpan ><")
            break
        
        try:
            mahasiswa[nama].append(float(nilai))
        except ValueError:
            print("Masukkan angka yang valid!")
        
def rata_rata(nilai_list):
    return sum(nilai_list) / len(nilai_list)

def status_kelulusan(rata_rata):
    if rata_rata >= 80 :
        return "LULUS Dengan Predikat A"
    elif rata_rata >= 70 :
        return "LULUS Dengan Predikat B"
    elif rata_rata >= 50 :
        return "LULUS Dengan Predikat C"
    else :
        return "TIDAK LULUS Dengan Predikat D"

def tampilkan_data():
    if not mahasiswa :
        print("Tidak Ada Data !")
        return
    
    for nama, nilai in mahasiswa.items():
        rata = rata_rata(nilai)
        status = status_kelulusan(rata)
        
        print(f"\nNama : {nama}")
        print(f"Nilai: {nilai}")
        print(f"Rata - Rata: {rata}")
        print(f"Status Kelulusan : {status}")

while True :
    tampil_menu()
    pilih = input("Pilihan Menu 1/2/3 : ")
    
    if pilih == "1" :
        tambah_data()
    elif pilih == "2":
        tampilkan_data()
    elif pilih == "3":
        print("Program Selesai ><")
        break
    else :
        print("Mohon masukan nomor yang tertera ><")
        
    