# Studi kasus: Membuat demonstrasi casting antar tipe data string, integer, dan float. lalu hasil akhir akan diubah kembali ke bentuk string

# Input awal berupa string
angka_string = input("Masukkan angka: ")

# Sebelumnya berupa string akan dicasting ke integer dan float
angka_int = int(angka_string)
angka_float = float(angka_string)

# Casting kembali lagi string dari hasil perhitungan sederhana
hasil_penjumlahan = angka_int + angka_float 
hasil_string = str(hasil_penjumlahan)

# Menampilkan hasil dengan tipe datanya
print("Angka dalam bentuk string:", angka_string)
print("Angka dalam bentuk integer:", angka_int)
print("Angka dalam bentuk float:", angka_float)

print("Angka Float dan Angka Interger akan dijumlahkan lalu akan di ubah kembali ke bentuk string")
print("Hasil penjumlahan antar angka float dan integer:", hasil_string)
