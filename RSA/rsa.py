import statistics as st
import math
import random


def genRandLet(num):
    randLets = []
    for i in range(num):
        rl = []
        for j in range(4):
            rl.extend(chr(random.randint(97, 122)))
        randLets.append(rl)
    return randLets


def strToInt(text):
    num = 0
    for i in range(len(text)):
        num += (26 ** i) * (ord(text[len(text) - 1 - i]) % 97)
    return num


def intToStr(num):
    text = []
    for i in range(max(int(math.log(num, 26)), 3), -1, -1):
        text.append(chr((num // (26 ** i)) + 97))
        num = num % (26**i)
    return text


def encrypt(plainText):
    cipherText = []
    for pt in plainText:
        cipherText.append(intToStr(((strToInt(pt)**key[1]) % key[2])))
    return cipherText


def decrypt(cipherText):
    plainText = []
    for ct in cipherText:
        plainText.append(intToStr(((strToInt(ct)**key[0]) % key[2])))
    return plainText


def freq(text):
    freqs = [0] * 26
    for w in text:
        for l in w:
            freqs[ord(l) % 97] += 1
    print('Mode: ' + str(max(freqs)))
    print('Mean: ' + str(st.mean(freqs)))
    print('Median: ' + str(st.median(freqs)))
    print('Standard Deviation: ' + str(st.pstdev(freqs)))
    print()


key = [259, 2719, 705917]
x = encrypt(genRandLet(250))
y = decrypt(x)
freq(x)
freq(y)
print("".join(letters for words in x for letters in words))
print()
print("".join(letters for words in y for letters in words))
