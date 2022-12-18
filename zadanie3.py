#!/usr/bin/python3
#XOR шифрование/расшифрование. На входе файл с текстом и ключ шифрования (строка), на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле.

key = 67

def inxor(text, t_key):
    t_text = ''
    for i in text:
        t_text += chr(ord(i) ^ t_key)
    return t_text

with open('xor_original.txt', 'r') as file:
    with open('xor_encrypted.txt', 'w') as file2:
        file2.write(inxor(file.read(), key))

with open('xor_encrypted.txt', 'r') as file:
    print(inxor(file.read(), key))