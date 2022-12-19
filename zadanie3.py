#!/usr/bin/python3
#XOR шифрование/расшифрование. На входе файл с текстом и ключ шифрования (строка), на выходе преобразованное (зашифрованное/расшифрованное) сообщение в файле.


#входные данные содержатся в файле 'xor_original.txt', размещенном в папке репозитория вместе с самим скриптом, и в переменной 'key', заданной в скрипте.
#на выходе файл с зашифрованным текстом 'xor_encrypted.txt' и файл 'xor_transcribed.txt' с расшифрованным текстом

#ключ шифрования (строка)
key = 'weqjfgjtyjtr'

def xorfunc(input_text, t_key):
    """Функция, шифрующая/расшифрующая текст по алгоритму XOR. Принимает в качестве первого аргумента текст для шифрования/расшифрования, в качестве второго аргумента принимает ключ шифрования (строка).
    """
    t_text = list()
    i = 0
    for j in (ord(k) for k in input_text):
        j ^= ord(t_key[i])
        t_text.append(j)
        i += 1
        if i >= len(t_key):
            i = 0
    return ''.join(chr(k) for k in t_text)

#чтение файла с исходным текстом 'xor_original.txt' и запись файла с зашифрованным текстом 'xor_encrypted.txt'
try:
    with open('xor_original.txt', 'r') as file:
        with open('xor_encrypted.txt', 'w') as file2:
            file2.write(xorfunc(file.read(), key))
except FileNotFoundError:
    print('файл xor_original.txt с исходным текстом не найден')
else:
#чтение файла с зашифрованным текстом 'xor_encrypted.txt' и запись файла с расшифрованным текстом 'xor_transcribed.txt'
    with open('xor_encrypted.txt', 'r') as file:
        with open('xor_transcribed.txt', 'w') as file2:
            file2.write(xorfunc(file.read(), key))