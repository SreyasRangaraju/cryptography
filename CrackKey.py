import binascii


def nthLargest(n, freqs):
    return freqs.index(sorted(freqs, reverse=True)[n])


def ioc(byteList):
    iocCount = [0] * 256
    for b in byteList:
        iocCount[b] += 1
    # print(iocCount)
    # print(nthLargest(0, iocCount))
    for i in range(len(iocCount)):
        iocCount[i] **= 2
    return sum(iocCount) / len(byteList) ** 2


def vigSep(m, byteList):
    byteLists = []
    iocs = []
    for i in range(m):
        byteLists.append([])
    for i in range(len(byteList)):
        byteLists[i % m].append(byteList[i])
    for b in byteLists:
        iocs.append(ioc(b))
    print(sum(iocs) / m)


byte = []
with open("encrypted.jpg", "rb") as f:
    b = f.read()
    b = binascii.hexlify(b).decode()
    for i in range(0, len(b), 2):
        byte.append(int(b[i:i + 2], 16))

keyLengthMax = 11
keyLength = 5
for i in range(1, keyLengthMax):
    vigSep(i, byte)
# vigSep(keyLength, byte)
