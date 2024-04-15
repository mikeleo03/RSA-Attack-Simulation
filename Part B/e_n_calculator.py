def main():
    # Hanya bekerja untuk e ganjil
    # Nilai -1^e % n
    neg_one_res = int(input("Masukkan keluaran dari masukan -1: "))

    # Nilai n didapat dari hasil penjumlahan 1 dengan neg_one_res
    n = neg_one_res + 1

    # Menghitung nilai e berdasarkan sepasang plaintext dan ciphertext
    plain = int(input("Masukkan angka plaintext: "))
    cipher = int(input("Masukkan hasil enkripsi dari plaintext: "))
    
    # Mencari nilai e dengan brute force
    e = 2**15
    while pow(plain, e, n) != cipher:
        e += 1
    
    print(f"Nilai e adalah {e}")

    # Menghitung hasil enkripsi nomor arsip admin
    nomor_arsip_admin = int(input("Masukkan nomor arsip admin: "))
    cipher_nomor_arsip_admin = pow(nomor_arsip_admin, e, n)
    print(f"Token akses nomor arsip admin: {cipher_nomor_arsip_admin}")


if __name__ == "__main__":
    main()
