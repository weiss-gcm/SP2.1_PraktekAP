def tabel_perkalian():
    # Penggunaan While Looping
    while True:
        angka = int(input("Masukan sebuaha angka untuk menunjukan tabel perkalian (Untuk Keluar ketik '-1'): "))
        if angka == -1:
            print("Program berhenti")
            break
        # Penggunaan For Looping
        print(f"\nTabel perkalian untuk {angka}:")
        for i in range(1, 11):
            print(f"{angka} x {i} = {angka * i}")
        
        print()

tabel_perkalian()
