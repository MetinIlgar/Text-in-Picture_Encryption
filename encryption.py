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