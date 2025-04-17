#Studi Kasus Pembuatan daftar barang sederhana dengan menggunakan Function, Parameter, dan Retrun 

def menu():  # FUNCTION - BLOCK KODE 1 (PRINT & INPUT - MENAMPILKAN MENU & MEMINTA OPSI KEPADA USER)
    print("Pilih nomor pada daftar: ")
    print("1. Tambah")
    print("2. Liat isi")
    print("3. Hapus")
    print("4. Keluar")
    opsi = input()
    return opsi  # RETURN

isi_daftar = []

def tambah(pengisian):  # FUNCTION - BLOCK KODE 2 (APPEND - MEMASUKAN BARANG KEDALAM DAFTAR)
    isi_daftar.append(pengisian)
    print("Telah Dimasukan", pengisian, "Kedalam daftar")

def liat_isi():  # FUNCTION - BLOCK KODE 3 (PRINT - MENAMPILKAN ISI DAFTAR)
    print(isi_daftar)

def hapus():  # FUNCTION - BLOCK KODE 4 (REMOVE - MENGHAPUS BARANG DARI DAFTAR)
    pengisian = input("Hapus nama barang kedalam daftar: ")
    if pengisian in isi_daftar:
        isi_daftar.remove(pengisian)
        print("Telah dihapus", pengisian, "dari daftar")
    else:
        print("Tidak ada barang", pengisian, "di dalam daftar")

def keluar():  # FUNCTION - BLOCK KODE 5 (PRINT - PROGRAM BERHENTI)
    print("Keluar")

melanjutkan = True
while melanjutkan:
    opsi = menu()
    if opsi == "1":
        pengisian = input("Isi Nama barang kedalam daftar: ")
        tambah(pengisian)
    elif opsi == "2":
        liat_isi()
    elif opsi == "3":
        hapus()
    elif opsi == "4":
        keluar()
        nro = False
