import numpy as np

def ascii2hex(ascii_val):
    return ascii_val.encode().hex()

def hex2rgb(hex_val):
    lv = len(hex_val)
    return tuple(int(hex_val[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb2hex(r,g,b):
    if (r <= 255 and r >= 0) and (g <= 255 and g >= 0) and (b <= 255 and b >= 0):
        return '%02x%02x%02x' % (r, g, b)
    else:
        return False

def hex2ascii(hex_val):
    try:
        byte_array = bytearray.fromhex(hex_val)
        return byte_array.decode()
    except:
        return False

def encryptImg(text, Image):
    encrypt_word_list = []
    i=0
    while i<len(text):
        hex = ascii2hex(text[i: i + 3])
        if len(hex) == 6:
            encrypt_word_list.append(hex2rgb(hex))
        else:
            zero = 6-len(hex)
            for a in range(0,zero):
                hex = hex+"0"
            encrypt_word_list.append(hex2rgb(hex))
        i += 3

    height = Image.shape[0]
    width = Image.shape[1]
    y = 0
    x = 0
    z = 0
    while True:
        Image[y,x] = encrypt_word_list[z][0],encrypt_word_list[z][1],encrypt_word_list[z][2]
        x = x+1
        z = z+1
        if x == width:
            y = y+1
            x = 0
        elif len(encrypt_word_list) == z:
            break
    return Image

def decodingImg(Image,long):
    height = Image.shape[0]
    width = Image.shape[1]
    y = 0
    x = 0
    z = 0
    decode_list = []
    while True:
        b,g,r = Image[y, x]
        a = rgb2hex(b, g, r)
        b = hex2ascii(a)
        if b == False:
          break
        decode_list.append(b)
        x = x + 1
        z = z + 1
        if x == width:
            y = y + 1
            x = 0
        elif long == z:
            break
    return "".join(decode_list)

def encryptImg2(text, Image):
    l1= []
    l2= []
    height = Image.shape[0]
    width = Image.shape[1]

    res = ''.join(format(i, '08b') for i in bytearray(text, encoding='utf-8'))
    if len(res) % 3 == 0:
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

def decodingImg2(Image):
    height = Image.shape[0]
    width = Image.shape[1]
    binary = ""
    count = 0
    count2 = 0
    for h in range(0, height, 2):
        for w in range(0, width):
            a = (Image[h+1, w] - Image[h, w])
            for i in a:
                binary = binary + str(i)
                if i == 0:
                    count2 = count2 + 1

                    if count2 == 3:
                        count = count + 1

            count2 = 0

            if count == 100:
                break
        if count == 100:
            break
    b = ""
    bl = []
    for x in binary:
        b = b+x
        if len(b) % 8 == 0:
            if int(b) == 0:
                b = ""
                continue
            bl.append(b)
            b=""

    return str(bytes([int(x,2) for x in bl]).decode('utf-8'))





