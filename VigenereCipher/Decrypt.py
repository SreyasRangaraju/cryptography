import binascii


def decrypt(key, cipherTextBytes):
    key = [ord(letter) for letter in key]
    plainText = []
    for i in range(len(cipherTextBytes)):
        plainText.append((cipherTextBytes[i] - key[(i // 2) % len(key)]) % 256)
    return bytes(plainText)


byte = []
key = 'anime'

with open("encrypted.jpg", "rb") as f:
    b = f.read()
    b = binascii.hexlify(b).decode()
    for i in range(0, len(b), 2):
        byte.append(int(b[i:i + 2], 16))

decrypted = decrypt(key, byte)
with open("decrypted.jpg", "wb") as f:
    f.write(decrypted)
