while True:
    print("Menu Pilihan")
    print("1. Barisan Fibonacci")
    print("2. M kali N")
    print("0. Keluar")

    pilih = int(input("Pilih Menu: "))

    if pilih == 1:
        n = int(input("Masukkan jumlah suku: "))

        a, b = 0, 1
        print("Barisan Fibonacci:")
        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b

        input("\n\nTekan Enter untuk kembali ke menu...")

    elif pilih == 2:
        m = int(input("Masukkan nilai M: "))
        n = int(input("Masukkan nilai N: "))

        print("Hasil M kali N:")
        for i in range(1, n+1):
            print(f"{m} x {i} = {m*i}")

        input("\n\nTekan Enter untuk kembali ke menu...")

    elif pilih == 0:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter...")