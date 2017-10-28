import binascii
import statistics as st


key = [1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1,
       0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1]


def bit2byte(bits):
    byteSum = 0
    for i in range(1, len(bits) + 1):
        byteSum += bits[-i] << (i - 1)
    return byteSum


def lfsr(r17, r25, numBytes):
    keystream = []
    carry = 0
    for i in range(numBytes):
        for j in range(8):
            r17.insert(0, r17[-17] ^ r17[-3])
            r17.pop()
            r25.insert(0, r25[-25] ^ r25[-8] ^ r25[-6] ^ r25[-2])
            r25.pop()
        nextByte = bit2byte(r17[:8]) + bit2byte(r25[:8]) + carry
        keystream.append(nextByte % 256)
        carry = nextByte // 256
    return keystream


def encrypt(plainText, keystream):
    cipherText = []
    for i in range(len(plainText)):
        cipherText.append(plainText[i] ^ keystream[i])
    return bytes(cipherText)


def decrypt(cipherText, keystream):
    plainText = []
    for i in range(len(cipherText)):
        plainText.append(cipherText[i] ^ keystream[i])
    return bytes(plainText)


def freq(byteList):
    freqs = [0] * 256
    for b in byteList:
        freqs[b] += 1
    print('Mode: ' + str(max(freqs)))
    print('Mean: ' + str(st.mean(freqs)))
    print('Median: ' + str(st.median(freqs)))
    print('Standard Deviation: ' + str(st.pstdev(freqs)))


obyte = []
with open("original.jpg", "rb") as f:
    b = f.read()
    b = binascii.hexlify(b).decode()
    for i in range(0, len(b), 2):
        obyte.append(int(b[i:i + 2], 16))
with open('encrypted.jpg', 'wb') as f:
    r17 = key[:16]
    r17.append(1)
    r25 = key[16:]
    r25.append(1)
    x = encrypt(obyte, lfsr(r17, r25, len(obyte)))
    f.write(x)

cbyte = []
with open("encrypted.jpg", "rb") as f:
    b = f.read()
    b = binascii.hexlify(b).decode()
    for i in range(0, len(b), 2):
        cbyte.append(int(b[i:i + 2], 16))
with open('decrypted.jpg', 'wb') as f:
    r17 = key[:16]
    r17.append(1)
    r25 = key[16:]
    r25.append(1)
    x = decrypt(cbyte, lfsr(r17, r25, len(cbyte)))
    f.write(x)

freq(obyte)
print()
freq(cbyte)
