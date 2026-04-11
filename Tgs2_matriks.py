while True:
    print("\n=== MENU LIST ===")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    pilihan = input("Masukkan pilihan: ")

    if pilihan == "0":
        print("Program selesai")
        break

    baris = int(input("Masukkan jumlah baris: "))
    kolom = int(input("Masukkan jumlah kolom: "))

    print("\nInput Matriks A")
    A = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            nilai = int(input(f"A[{i}][{j}] = "))
            baris_data.append(nilai)
        A.append(baris_data)

    print("\nInput Matriks B")
    B = []
    for i in range(baris):
        baris_data = []
        for j in range(kolom):
            nilai = int(input(f"B[{i}][{j}] = "))
            baris_data.append(nilai)
        B.append(baris_data)

    
    if pilihan == "1":
        hasil = []
        for i in range(baris):
            baris_hasil = []
            for j in range(kolom):
                baris_hasil.append(A[i][j] + B[i][j])
            hasil.append(baris_hasil)

        print("\nHasil Penjumlahan:")
        for h in hasil:
            print(h)

    elif pilihan == "2":
        hasil = []
        for i in range(baris):
            baris_hasil = []
            for j in range(kolom):
                baris_hasil.append(A[i][j] - B[i][j])
            hasil.append(baris_hasil)

        print("\nHasil Pengurangan:")
        for h in hasil:
            print(h)

    elif pilihan == "3":
        hasil = []
        for i in range(baris):
            baris_hasil = []
            for j in range(kolom):
                total = 0
                for k in range(kolom):
                    total += A[i][k] * B[k][j]
                baris_hasil.append(total)
            hasil.append(baris_hasil)

        print("\nHasil Perkalian:")
        for h in hasil:
            print(h)

    else:
        print("Pilihan tidak valid!")