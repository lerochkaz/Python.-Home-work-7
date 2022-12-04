# 1.	Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# import math
# pi = math.pi
# d = (list(map(int, ((input('Введите точность d: ').split('.'))[1]))))
# characterCounter = 0

# for _ in d:
#     characterCounter += 1
# print(characterCounter)

# 2.Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# N = int(input("Введите число N: "))
# dividers = []
# for i in range(1, N):
#     if (N % i == 0):
#         dividers.append(i)
# print(f'Делители числа N: {dividers}')

# resultList = []
# counter = 0

# for i in range(0, len(dividers)):
#     for j in range(1, dividers[i]+1):
#         if (dividers[i] % j == 0):
#             counter += 1
#     if counter <= 2:
#         resultList.append(dividers[i])
#     counter = 0

# print(f'Простые множители числа N: {resultList}')

# 3.	Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# someList = list(map(int, (input('Введите числа через пробел: ').split(' '))))
# resultList = []
# if len(someList) == len(set(someList)):
#     print('Все элементы уникальны')
# else:
#     for i in range(0, len(someList)):
#         if someList.count(someList[i]) == 1:
#             resultList.append(someList[i])
#     print(
#         f'Список неповторяющихся элементов исходной последовательности: {resultList}')
