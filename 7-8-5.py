def encryptcaesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('А') + shift) % 33 + ord('А'))
            else:
                result += chr((ord(char) - ord('а') + shift) % 33 + ord('а'))
        else:
            result += char
    return result
def decryptcaesar(text, shift):
    return encryptcaesar(text, -shift)
plaintext = input("Введите текст: ")
shiftvalue = int(input("Введите значение сдвига: "))
encryptedtext = encryptcaesar(plaintext, shiftvalue)
print("Зашифрованный текст:", encryptedtext)