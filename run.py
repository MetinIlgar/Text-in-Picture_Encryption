import encryption
import cv2 as cv
import sys, os
import argparse

# Project Information
parser = argparse.ArgumentParser(prog = "Text-in-picture encryption.",
                                 description = "This application is for encryption and decryption on the picture.",
                                 epilog = "This software was created by Metin Ilgar Mutlu.")

# Encryption
parser.add_argument("--encode", "-enc",
                    help = """Indicates that it wants to encrypt the text into the image.\n
                     Example: python run.py -enc -img picture.png -txt 'sample text'""",
                    action="store_true")
# Decryption
parser.add_argument("--decode", "-dec", help = """Indicates that you want to decrypt the image.\n
                                               Example: python run.py -dec -img picture.png""",
                    action="store_true")
parser.add_argument("--image", "-img" , help = "Specifies the file path of the image.", type=str)
parser.add_argument("--text", "-txt", help = "Specifies the text you want to encrypt.", type=str)

data = parser.parse_args()

def heading():
    head = """
████████╗███████╗██╗░░██╗████████╗░░░░░░██╗███╗░░██╗░░░░░░██████╗░██╗░█████╗░████████╗██╗░░░██╗██████╗░███████╗
╚══██╔══╝██╔════╝╚██╗██╔╝╚══██╔══╝░░░░░░██║████╗░██║░░░░░░██╔══██╗██║██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗██╔════╝
░░░██║░░░█████╗░░░╚███╔╝░░░░██║░░░█████╗██║██╔██╗██║█████╗██████╔╝██║██║░░╚═╝░░░██║░░░██║░░░██║██████╔╝█████╗░░
░░░██║░░░██╔══╝░░░██╔██╗░░░░██║░░░╚════╝██║██║╚████║╚════╝██╔═══╝░██║██║░░██╗░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░
░░░██║░░░███████╗██╔╝╚██╗░░░██║░░░░░░░░░██║██║░╚███║░░░░░░██║░░░░░██║╚█████╔╝░░░██║░░░╚██████╔╝██║░░██║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░░░░░░╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝

            ███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗
            ██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║
            █████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║
            ██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║
            ███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║
            ╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝        

                                                                                    𝑴𝒂𝒅𝒆 𝒃𝒚 𝑴𝒆𝒕𝒊𝒏 𝑰𝒍𝒈𝒂𝒓 𝑴𝒖𝒕𝒍𝒖
                                                                                    
                                                                                    
                    > Encrypt text to image.
                    > Version 2.0
                                                                                  
"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(head)
    print("\tEnter The Image Path: ")
    img = input("\t\t> ")
    img = cv.imread(img)
    if img is None:
        sys.exit("Could not read the image.")

    while True:
        print("\n\tSelect an action.\n\t[1] Image encryption\n\t[2] Image decryption")
        c = input("\t\t> ")
        if c == "1":
            print("\n\tText to be encrypted:")
            text = input("\t\t> ")
            encryption.encryptImg(text, img)
            cv.imwrite("EncryptionImage.png", img)
            break
        elif c == "2":
            text = encryption.decodingImg(img)
            output = open("output.txt", "w")
            output.write(text)
            output.close()
            print("\tText: " +text)
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Choose a valid action.")


if data.decode == False and data.encode == False :
    heading()

elif data.decode == False and data.encode == True:
    img = data.image
    text = data.text
    if text is None:
        print("\tText to be encrypted:")
        text = input("\t\t> ")
    if img is None:
        print("\n\tEnter the image path:")
        img = input("\t\t> ")

    img = cv.imread(img)
    if img is None:
        sys.exit("Could not read the image.")

    encryption.encryptImg(text, img)
    cv.imwrite("EncryptionImage.png", img)

elif data.decode == True and data.encode == False:
    img = data.image
    if img is None:
        print("\tEnter the image path:")
        img = input("\t\t> ")

    img = cv.imread(img)
    if img is None:
        sys.exit("Could not read the image.")
    text = encryption.decodingImg(img)
    output = open("output.txt", "w")
    output.write(text)
    output.close()
    print("\tText: "+text)