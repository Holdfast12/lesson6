#!/usr/bin/python3
#Написать функцию преобразующую список строк, в список байт кодов. Написать обратную функцию.

def strinbyte(spisok):
    """Функция, возвращающая преобразованный список строк в список байт кодов
    """
    t = []
    for i in range(len(spisok)):
        t.append(spisok[i].encode('utf-8'))
    return t

def byteinstr(spisok):
    """Функция, возвращающая преобразованный список байт кодов в список строк
    """
    t = []
    for i in range(len(spisok)):
        t.append(spisok[i].decode('utf-8'))
    return t

inputlist = input('\nВведите строки для создания из них списка и их дальнейшего преобразования, разделяя их пробелами: ').split()

print(f'Из строк в байт коды: {strinbyte(inputlist)}')
print(f'Из байт кодов в строки (через обратную функцию): {byteinstr(strinbyte(inputlist))}')