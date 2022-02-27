import numpy as np


def text2binary(text):
    return ''.join(format(i, '08b') for i in bytearray(text, encoding='utf-8'))

def binary2text(binaryCode):
    if len(binaryCode) == 8:
        return str(bytes([int(binaryCode, 2)]).decode('utf-8'))
    elif len(binaryCode) != 8 and len(binaryCode) % 8 == 0:
        a = 0
        word = ""
        while len(binaryCode) > a:
            i = binaryCode[a:a+8]
            print(i)
            word = word + str(bytes([int(i, 2)]).decode('utf-8'))
            a = a + 8
        return word
    else:
        return ""

# Encryption
def encryptImg(text, Image):
    l1= []
    l2= []
    height = Image.shape[0]
    width = Image.shape[1]

    text = text + "ThisIsTheEndOfTheMessage."

    res = text2binary(text)

    if (len(res) % 3 == 0):
        pass
    else:
        for x in range(0, (3 - (len(res) % 3))):
            res = res + "0"

    for h in range(0,height,2):
        for w in range(0,width):
            l1.append(Image[h,w])

            if len(res) <= len(l1)*3:
                break
        if len(res) <= len(l1)*3:
           break

    k = 0
    for a1,a2,a3 in l1:
        l2.append(np.array([a1+int(res[k]), a2+int(res[k+1]), a3+int(res[k+2])], dtype=np.uint8))
        k = k + 3

    for h in range(1,height,2):
        for w in range(0,width):
            Image[h,w] = l2[w]

            if len(l2)-1 == w:
                break
        if len(l2) - 1 == w:
            break
    return Image

# Decryption
def decodingImg(Image):
    height = Image.shape[0]
    width = Image.shape[1]
    binary = ""
    wl = ""
    key = "ThisIsTheEndOfTheMessage"

    for h in range(0, height, 2):
        for w in range(0, width):
            a = (Image[h+1, w] - Image[h, w])
            for i in a:
                binary = binary + str(i)
                if len(binary) % 8 == 0:
                    wl = wl + binary2text(binary)
                    binary = ""


            if key in wl:
                break
        if key in wl:
            break

    return wl[:-len(key)]

