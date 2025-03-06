#Studi Kasus: Membuat operasi hitungan & perkalian dengan menggunakan VARIABLE yang tertera dan hanya memasukan input untuk angka yang akan dikalikan dan dibagikan.

#Variable
angka_1 = 6
angka_2 = 7
angka_3 = 8

print("Masukan Angka yang akan dibagi dan dikali oleh angka di bawah:")
print(angka_1, angka_2, angka_3)
print(50 *"-")

#Input
angkaX = int(input("Masukan Angka yg anda mau (JANGAN ANGKA NOL): "))

#Proses
def kali(angka):
    return angka_1 * angka, angka_2 * angka, angka_3 * angka

def bagi(angka):
    if angka == 0:
        return "Itu angka 0 yaa... gabisa di bagi yang ada hasilnya error"
    return angka_1 / angka, angka_2 / angka, angka_3 / angka

#Output
print(50 * "-")
print("Hasil perkalian adalah:", kali(angkaX))
print("Hasil pembagian adalah:", bagi(angkaX))
