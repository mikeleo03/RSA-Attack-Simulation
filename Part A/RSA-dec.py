from sympy import factorint
from Crypto.Util.number import *
from mpmath import mp

# Pembangkitan kunci RSA tidak benar-benar acak, tetapi menggunakan sebuah bilangan prima yang diubah dengan nilai acak.
# Tidak aman dengan serangan faktorisasi
def decrypt_variant_a(ciphertext, n, e):
    factors = factorint(n)
    p, q = factors.keys()
    d = pow(e, -1, (p-1)*(q-1))
    plaintext_int = pow(ciphertext, d, n)
    plaintext_bytes = long_to_bytes(plaintext_int)
    return plaintext_bytes

# Nilai N = p^k dengan k adalah bilangan asli
# Jika N = p^k, maka Totient(N) = p^(k-1) * (p-1)
def decrypt_variant_b(ciphertext, n, e):
    mp.dps = 1000
    p = int(mp.sqrt(n))
    d = pow(e, -1, p*(p-1))
    plaintext_int = pow(ciphertext, d, n)
    plaintext_bytes = long_to_bytes(plaintext_int)
    return plaintext_bytes

# Mian program
if __name__ == "__main__":
    c = int(input("Enter the ciphertext (c): "))
    n = int(input("Enter the modulus (n): "))
    e = int(input("Enter the public exponent (e): "))
    
    # Ganti varian nya
    plaintext = decrypt_variant_b(c, n, e)
    print(plaintext)