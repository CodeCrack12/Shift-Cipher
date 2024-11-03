print("WELCOME TO SHIFT CIPHER")
print("DO YOU WANT TO ENCRYPT OR DECRYPT?")
print("1.Encrypt.\n2.Decrypt.")
while True:
    try:
        option = int(input("Enter 1 or 2: "))
        if option == 1 or option == 2:
            if option == 1:
                key = int(input("Enter the key: "))
                plain_text = input("Enter the plain text: ")
                for i in plain_text:
                    plain_text = ord(i)
                    x = plain_text + key
                    print(chr(x), end="")
                break
            elif option == 2:
                key = int(input("Enter the key: "))
                cipher_text = input("Enter the cipher text: ")
                for i in cipher_text:
                    cipher_text = ord(i)
                    y = cipher_text - key
                    print(chr(y), end="")
                break
        else:
            print("Select the right option.")
    except:
        print("Enter the right option: ")