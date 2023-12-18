def encrypt_ecb(plaintext_hex, key_binary):
    plaintext_binary = bin(int(plaintext_hex, 16))[2:]
    blocks = [plaintext_binary[i:i+4] for i in range(0, len(plaintext_binary), 4)]
    encrypted_blocks = []
    for block in blocks:
        xor_result = ''.join(str(int(b) ^ int(k)) for b, k in zip(block, key_binary))
        shifted_result = xor_result[1:] + xor_result[0]
        encrypted_blocks.append(str(int(shifted_result, 2)))
    return encrypted_blocks

def main():
    plaintext_hex = input("Masukkan Plainteks : ")
    key_binary = input("Masukkan Kunci : ")
    encrypted_result = encrypt_ecb(plaintext_hex, key_binary)
    print("Hasil Enkripsi ECB:", encrypted_result)
if __name__ == "__main__":
    main()
