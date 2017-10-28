import binascii


def encrypt(key, plainTextBytes):
    key = [ord(letter) for letter in key]
    cipherText = []
    for i in range(len(plainTextBytes)):
        cipherText.append((plainTextBytes[i] + key[(i // 2) % len(key)]) % 256)
    return bytes(cipherText)


byte = []
key = 'anime'

with open("original.jpg", "rb") as f:
    b = f.read()
    b = binascii.hexlify(b).decode()
    for i in range(0, len(b), 2):
        byte.append(int(b[i:i + 2], 16))

encrypted = encrypt(key, byte)
with open("encrypted.jpg", "wb") as f:
    f.write(encrypted)
