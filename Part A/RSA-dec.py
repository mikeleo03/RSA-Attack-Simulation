from sympy import factorint
from Crypto.Util.number import *
from mpmath import mp
from fractions import Fraction

# Fungsi bantuan untuk menghitung pecahan lanjutan dari e/n
def continued_fraction(e, n):
    while n:
        a = e // n
        yield a
        e, n = n, e - a * n

# Fungsi bantuan untuk mengubah pecahan lanjutan menjadi konvergen
def convergents_of_cont_frac(fraction):
    convergents = []
    for i in fraction:
        if not convergents:
            convergents.append((i, 1))
        elif len(convergents) == 1:
            convergents.append((i*convergents[0][0]+1, i))
        else:
            convergents.append((i*convergents[-1][0] + convergents[-2][0], i*convergents[-1][1] + convergents[-2][1]))
    return convergents

# RSA Decryption 
# Pembangkitan kunci RSA tidak benar-benar acak, tetapi menggunakan sebuah bilangan prima yang diubah dengan nilai acak.
# Tidak aman dengan serangan faktorisasi
def decrypt_variant_a(ciphertext, n, e):
    factors = factorint(n)
    p, q = factors.keys()
    d = pow(e, -1, (p-1)*(q-1))
    plaintext_int = pow(ciphertext, d, n)
    plaintext_bytes = long_to_bytes(plaintext_int)
    print("Decryption successful with d =", d)
    return plaintext_bytes

# Nilai N = p^k dengan k adalah bilangan asli
# Jika N = p^k, maka Totient(N) = p^(k-1) * (p-1)
def decrypt_variant_b(ciphertext, n, e):
    mp.dps = 1000
    p = int(mp.sqrt(n))
    d = pow(e, -1, p*(p-1))
    plaintext_int = pow(ciphertext, d, n)
    plaintext_bytes = long_to_bytes(plaintext_int)
    print("Decryption successful with d =", d)
    return plaintext_bytes

# Nilai d yang sangat besar dan terbatas membuat konsekuensi nilai e kecil
# Tidak aman dengan Wiener's attack
def decrypt_variant_c(ciphertext, n, e):
    # Hasilkan representasi pecahan lanjutan dari e/n
    frac = continued_fraction(e, n)
    
    # Ubah pecahan lanjutan menjadi konvergen
    convergents = convergents_of_cont_frac(frac)
    
    # Mencoba untuk mendekripsi ciphertext menggunakan setiap konvergen sebagai eksponen privat
    for k, d in convergents:
        try:
            # Mencoba dekripsi
            plaintext_int = pow(ciphertext, d, n)
            plaintext_bytes = long_to_bytes(plaintext_int)
            
            # Jika hasil dekripsi mengikuti pola KRIPTOGRAFIITB{secret}, maka itu jawabannya
            if plaintext_bytes.startswith(b'KRIPTOGRAFIITB{'):
                print("Decryption successful with d =", d)
                return plaintext_bytes
            
        except Exception as e:
            print("Error with d =", d, "Error:", e)
            continue
    
    # Jika tidak ada yang valid, return None
    return None

# Why?
""" def decrypt_variant_d(ciphertext, n, e):
    # TODO
    
# Why?
def decrypt_variant_e(ciphertext, n, e):
    # TODO """

# Main program
if __name__ == "__main__":
    c = int(input("Enter the ciphertext (c): "))
    n = int(input("Enter the modulus (n): "))
    e = int(input("Enter the public exponent (e): "))
    
    # Ganti varian nya
    plaintext = decrypt_variant_c(c, n, e)
    print(plaintext)