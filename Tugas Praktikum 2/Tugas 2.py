#STUDI KASUS: PROGRAM PEMBAYARAN DENGAN DISKON DAN LOYALTY POINT
#NIM: 1124102188

# Assignment
total_belanja = int(input("Masukkan total belanja: Rp "))
apa_member = input("Apakah pelanggan  merupakan member? (y/n): ").lower() == 'y'

# Assignment
diskon = 0
loyalty_points = 0

# Comparisson & logical
if total_belanja > 1000000:  # Comparison
    diskon = 0.15  # 15% diskon
elif total_belanja >= 500000 and apa_member:  # Comparisson + Logical AND
    diskon = 0.10  # 10% diskon
elif total_belanja >= 300000 or apa_member:  # Comparisson + Logical OR
    diskon = 0.05  # 5% diskon

# Aritmatika: Hitung total setelah diskon
total_setelah_diskon = total_belanja - (total_belanja * diskon)

# Assignment
if apa_member:
    loyalty_points += int(total_belanja // 10000)  # Aritmatika + Assignment

# Output
print(f"Total Belanja: Rp {total_belanja:,.2f}")
print(f"Diskon: {diskon*100:.0f}%")
print(f"Total setelah diskon: Rp {total_setelah_diskon:,.2f}")
print(f"Loyalty Points ditambahkan: {loyalty_points}")

# Operator Comparisson
if loyalty_points > 50 and total_setelah_diskon > 400000:  # Logical AND
    print("\nBonus! Anda mendapatkan potongan Rp 50.000!")
