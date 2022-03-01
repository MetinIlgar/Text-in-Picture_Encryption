def text2binary(text):
    return ''.join(format(i, '08b') for i in bytearray(text, encoding='utf-8'))

def binary2text(binaryCode):
    if len(binaryCode) == 8:
        return str(bytes([int(binaryCode, 2)]).decode('utf-8', "ignore"))
    elif len(binaryCode) != 8 and len(binaryCode) % 8 == 0:
        a = 0
        word = ""
        while len(binaryCode) > a:
            i = binaryCode[a:a+8]
            word = word + str(bytes([int(i, 2)]).decode('utf-8', "ignore"))
            a = a + 8
        return word
    else:
        return ""

# Encryption
def encryptImg(text, Image):
    width, height = Image.size
    pixel_map = Image.load()

    text = text + "3NdOf_Text."

    res = text2binary(text)

    if (len(res) % 3 == 0):
        pass
    else:
        for x in range(0, (3 - (len(res) % 3))):
            res = res + "0"

    k = 0
    for h in range(0, height, 2):
        for w in range(width):
            r2, g2, b2 = Image.getpixel((w, h + 1))

            try:
                r = r2 + int(res[k])
                k = k + 1
                g = g2 + int(res[k])
                k = k + 1
                b = b2 + int(res[k])
                k = k + 1
                pixel_map[w, h] = (r, g, b)
            except:
                return Image

# Decryption
def decodingImg(Image):
    binary = ""
    wl = ""
    key = "3NdOf_Text"
    width, height = Image.size

    for h in range(0, height, 2):
        for w in range(0, width):
            r,g,b = Image.getpixel((w,h))
            r2,g2,b2 = Image.getpixel((w,h+1))
            x1 = r-r2
            x2 = g-g2
            x3 = b-b2

            if x1 == 1 or x1 == 0:
                binary = binary + str(x1)
                if len(binary) % 8 == 0:
                    wl = wl + binary2text(binary)
                    binary = ""

            if x2 == 1 or x2 == 0:
                binary = binary + str(x2)
                if len(binary) % 8 == 0:
                    wl = wl + binary2text(binary)
                    binary = ""

            if x3 == 1 or x3 == 0:
                binary = binary + str(x3)
                if len(binary) % 8 == 0:
                    wl = wl + binary2text(binary)
                    binary = ""

            if key in wl:
                break
        if key in wl:
            break

    return wl[:-len(key)]