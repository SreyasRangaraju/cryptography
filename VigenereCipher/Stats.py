import binascii
import statistics as st


def freq(byteList):
    freqs = [0] * 256
    for b in byteList:
        freqs[b] += 1
    print('Mode: ' + str(max(freqs)))
    print('Mean: ' + str(st.mean(freqs)))
    print('Median: ' + str(st.median(freqs)))
    print('Standard Deviation: ' + str(st.pstdev(freqs)))
    print('Mode Index: ' + str(freqs.index(max(freqs))))
    print(freqs)


byte = []
with open("original.jpg", "rb") as f:
    b = f.read()
    b = binascii.hexlify(b).decode()
    for i in range(0, len(b), 2):
        byte.append(int(b[i:i + 2], 16))
freq(byte)
