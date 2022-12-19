#!/usr/bin/python3
'''
Формула молекулы спирта - C2H5(OH). Из неё видно, что молекула состоит из двух атомов углерода (С), 6 атомов водорода (Н) и одного атома кислорода (О).
В Input.txt содержится 3 натуральных числа: C, H, O – количество атомов углерода, водорода и кислорода соответственно.
В файл Output.txt вывести максимально возможное число молекул спирта, которые могут получиться из атомов, представленных во входных данных.
'''

def inputwrite(c, h, o):
    """Функция, принимающая значения C H O и записывающая их в файл Input.txt
    """
    with open('Input.txt', 'w') as file:
        file.write(f'{c} {h} {o}')

def inputread():
    """Функция, считывающая значения C H O из файла Input.txt и возвращающая их в виде списка
    """
    with open('Input.txt', 'r') as file:
        return(list(int(i) for i in file.read().split()))

def outputwrite(maxmol):
    """Функция, записывающая максимально возможное число молекул спирта в файл Output.txt
    """
    with open('Output.txt', 'w') as file:
        file.write(str(maxmol))

def outputread():
    """Функция, считывающая максимально возможное число молекул спирта из файла Output.txt
    """
    with open('Output.txt', 'r') as file:
        return int(file.read())

#список с кличеством C H O для одной молекулы
spirt = [2, 6, 1]

while True:
    try:
        c, h, o = map(lambda n: int(n), input('Введите 3 натуральных числа C, H, O через пробел. Они будут сохранены в Input.txt и потом прочитаны оттуда. Стоп-слово для выхода \"стоп\": ').split())
    except ValueError as e:
        if str(e).find('стоп') == -1:
            print('Должны быть введены 3 натуральных числа')
        else:
            break
    else:
        if c < 0 or h < 0 or o < 0:
            print('Должны быть введены 3 натуральных числа')
            continue
        #записал список полученных чисел в Input.txt
        inputwrite(c, h, o)
        #беру список чисел из Input.txt в переменную
        cho = inputread()
        #посчитал максимально возможное число молекул и сложил это число в файл Output.txt
        outputwrite(min(cho[i] // spirt[i] for i in range(3)))
        #вывел максимально возможное число молекул, прочитанное из файла Output.txt
        print(f'Максимально возможное количество молекул спирта, которые могут быть получены из введенных данных: {outputread()}')