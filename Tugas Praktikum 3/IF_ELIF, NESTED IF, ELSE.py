#IF ELSE, ELIF, NESTED IF
#STUDI KASUS: PROGRAM PENGECEKAN BANDWIDTH INTERNET DAN WAKTU PENGUNDUHAN FILE
# NIM: 1124102188


def cek_bandwidth():
    # Input
    bandwidth = float(input("Masukkan bandwidth yang Anda miliki (dalam Mbps): "))
    print("1. Menonton video")
    print("2. Mengunduh file")
    kebutuhan = input("Apa yang ingin Anda lakukan? Pilih angka 1 atau 2: ")

    #IF ELSE & ELIF
    if kebutuhan == "1":
        bandwidth_dibutuhkan1 = 5  
        bandwidth_dibutuhkan2 = 10 
        bandwidth_dibutuhkan3 = 40 
        bandwidth_dibutuhkan4 = 100
        if bandwidth >= bandwidth_dibutuhkan1:
            print("Bandwidth Anda cukup untuk menonton video HD.")
        elif bandwidth >= bandwidth_dibutuhkan2:
            print("Bandwidth Anda cukup untuk menonton video Full HD.")
        elif bandwidth >= bandwidth_dibutuhkan3:
            print("Bandwidth Anda cukup untuk menonton video 4K.")
        elif bandwidth >= bandwidth_dibutuhkan4:
            print("Bandwidth Anda cukup untuk menonton video 8K.")
        else:
            print("Bandwidth Anda tidak cukup untuk menonton video HD.")

    elif kebutuhan == "2":
        ukuran_file = float(input("Masukkan ukuran file yang ingin diunduh (dalam GB): "))
        bandwidth_dibutuhkan = 10  

        # NESTED IF
        if bandwidth >= bandwidth_dibutuhkan:
            print("Bandwidth Anda cukup untuk mengunduh file dengan cepat.")
            waktu_unduh = (ukuran_file * 8000) / bandwidth 
            print(f"Estimasi waktu unduh: {waktu_unduh / 60:.2f} menit.")
        else:
            print("Bandwidth Anda tidak cukup untuk mengunduh file dengan cepat.")
            waktu_unduh = (ukuran_file * 8000) / bandwidth
            print(f"Estimasi waktu unduh: {waktu_unduh / 60:.2f} menit.")
    else:
        print("Pilihan tidak valid. Silakan pilih 'video_hd' atau 'unduh_file'.")

cek_bandwidth()
