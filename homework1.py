# №1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# Решение:

# a = int(input('Введите день недели: '))
# while a > 7 or a < 1:
#     print('Вы ввели не день недели!')
#     a = int(input('Введите день недели: '))

# if a == 1:
#    print('Не выходной') 
# elif a == 2:
#    print('Не выходной')
# elif a == 3:
#    print('Не выходной') 
# elif a == 4:
#    print('Не выходной')       
# elif a == 5:
#    print('Не выходной') 
# elif a == 6:
#    print('Выходной') 
# elif a == 7:
#    print('Выходной')       


# №2.Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример: 
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# Решение:

# x = int(input('Введите координат х: '))
# y = int(input('Введите координат y: '))

# while x == 0 and y == 0:
#     print('В условии X ≠ 0 и Y ≠ 0, попробуйти сново!')
#     x = int(input('Введите координат х: '))
#     y = int(input('Введите координат y: '))

# if x > 0 and y > 0:
#     print('Ваша точка находится в 1 плоскости')
# elif x < 0 and y > 0:
#     print('Ваша точка находится в 2 плоскости')
# elif x < 0 and y < 0:
#     print('Ваша точка находится в 3 плоскости')
# elif x > 0 and y < 0:
#     print('Ваша точка находится в 4 плоскости')


# № 3 Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Решение:

# quarter = int(input('Введите номер четверти: '))

# while quarter < 1 or quarter > 4:
#     print('Вы ввели не номер четверти! Попробуйти сново.') 
#     quarter = int(input('Введите номер четверти: '))

# if   quarter == 1:
#     print('Возможные точки координат четверти 1: x > 0 & y > 0')   
# elif   quarter == 2:
#     print('Возможные точки координат четверти 2: x < 0 & y > 0')   
# elif   quarter == 3:
#     print('Возможные точки координат четверти 3: x < 0 & y < 0')   
# elif   quarter == 4:
#     print('Возможные точки координат четверти 4: x > 0 & y < 0')               