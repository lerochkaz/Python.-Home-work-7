# 1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# numberWeek = int(input('Введите цифру дня недели:'))
# if numberWeek >= 1 and numberWeek <= 5:
#     print('Это рабочий день недели!')
# elif numberWeek >= 6 and numberWeek <= 7:
#     print('Это выходной день!')
# else:
#     print('Под таким номером нет ни одного дня недели!')

# 2.	Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# for X in range(0, 2):
#     for Y in range(0, 2):
#         for Z in range(0, 2):
#             print((not (X or Y or Z)) == ((not X) and (not Y) and (not Z)))

# 3.	Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# X = int(input('Введите значение координаты X точки:'))
# Y = int(input('Введите значение координаты Y точки:'))

# if X == 0 and Y == 0:
#     print('Введены некорректные значения X и Y')
# else:
#     if X > 0 and X != 0:
#         if Y > 0 and Y != 0:
#             print('Точка находится в 1 четверти')
#         elif Y < 0 and Y != 0:
#             print('Точка находится в 4 четверти')
#         else:
#             print('Точка лежит на оси Y')
#     elif X < 0 and X != 0:
#         if Y > 0 and Y != 0:
#             print('Точка находится во 2 четверти')
#         elif Y < 0 and Y != 0:
#             print('Точка находится в 3 четверти')
#         else:
#             print('Точка лежит на оси Y')
#     else:
#         print('Точка лежит на оси X')

# 4.	Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# numberFourth = int(input('Введите номер четверти: '))
# if numberFourth == 1:
#     print('Возможные координаты точки: X > 0, Y > 0')
# elif numberFourth == 2:
#     print('Возможные координаты точки: X<0, Y>0')
# elif numberFourth == 3:
#     print('Возможные координаты точки: X<0, Y<0')
# elif numberFourth == 4:
#     print('Возможные координаты точки: X>0, Y<0')
# else:
#     print('Четверти с таким номером нет!')

# 5.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# import math
# AX, AY = map(int, input(
#     'Введите координаты точки A через запятую: ').split(','))
# BX, BY = map(int, input(
#     'Введите координаты точки B через запятую: ').split(','))
# result = round(math.sqrt(((BX-AX)**2)+((BY-AY)**2)), 2)
# print(f'Расстояние между двумя точками {result}')
