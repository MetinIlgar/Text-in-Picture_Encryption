import encryption
import cv2 as cv
import sys
import argparse

# Project Information
parser = argparse.ArgumentParser(prog = "Text-in-picture encryption.",
                                 description = "This application is for encryption and decryption on the picture.",
                                 epilog = "This software was created by Metin Ilgar Mutlu.")
#------------------------------------ Commands for Version 0.1 ------------------------------------
# Encryption version 0.1
parser.add_argument("--encode", "-enc",
                    help = """Indicates that it wants to encrypt the text into the image.\n
                    Example: python run.py -enc -img picture.png -txt 'sample text'""",
                    action="store_true")
# Decryption version 0.1
parser.add_argument("--decode", "-dec",
                    help = """Indicates that you want to decrypt the image.\n
                    Example: python run.py -dec -img picture.png -len 100""",
                    action="store_true")
#------------------------------------ Commands for Version 0.2 ------------------------------------
# Encryption version 0.2
parser.add_argument("--encode2", "-enc2",
                    help = """Indicates that it wants to encrypt the text into the image.\n
                     Example: python run.py -enc2 -img picture.png -txt 'sample text'""",
                    action="store_true")
# Decryption version 0.2
parser.add_argument("--decode2", "-dec2", help = """Indicates that you want to decrypt the image.\n
                                               Example: python run.py -dec2 -img picture.png""",
                    action="store_true")
parser.add_argument("--image", "-img" , help = "Specifies the file path of the image.", type=str, required=True)
parser.add_argument("--text", "-txt", help = "Specifies the text you want to encrypt.", type=str)
parser.add_argument("--length", "-len", help = "Estimated length of encrypted text.", type=int)
data = parser.parse_args()

img = cv.imread(data.image)
if img is None:
    sys.exit("Could not read the image.")


if data.decode == False and data.encode == True and data.decode2 == False and data.encode2 == False:
    encryption.encryptImg(data.text,img)
    cv.imwrite("EncryptionImage.png", img)
elif data.decode == True and data.encode == False and data.decode2 == False and data.encode2 == False:
    text = encryption.decodingImg(img,data.length)
    output = open("output.txt", "w")
    output.write(text)
    output.close()
    print(text)
elif data.decode == False and data.encode == False and data.decode2 == True and data.encode2 == False:
    text = encryption.decodingImg2(img)
    output = open("output.txt", "w")
    output.write(text)
    output.close()
    print(text)
elif data.decode == False and data.encode == False and data.decode2 == False and data.encode2 == True:
    encryption.encryptImg2(data.text, img)
    cv.imwrite("EncryptionImage.png", img)
else:
    print("Wrong use.")

