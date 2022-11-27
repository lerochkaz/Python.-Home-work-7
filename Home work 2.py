# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# def CheckList(inputNumber):
#     newList = []
#     length = len(inputNumber)
#     for i in range(0, length):
#         if inputNumber[i] != ',' and inputNumber[i] != '.' and inputNumber[i] != '-':
#             newList.append(inputNumber[i])
#     return newList


# def ChangeList(newList):
#     length = len(newList)
#     for i in range(0, length):
#         newList[i] = int(newList[i])
#     return newList


# def SumOfNumbers(newList, sum=0, count=0):
#     lengthList = len(newList)
#     if count == lengthList:
#         print(f'Сумма цифр числа = {sum}')
#     else:
#         sum += (newList[count])
#         count += 1
#         SumOfNumbers(newList, sum, count)


# inputNumber = list(input('Введите число: '))
# newList = CheckList(inputNumber)
# ChangeList(newList)
# SumOfNumbers(newList)

# 2.Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def ProductOfNumbers(N, list, i=0):
#     if i+1 == N:
#         list[i] = list[i-1]*N
#     elif i == 0:
#         list[i] = 1
#         i += 1
#         ProductOfNumbers(N, list, i)
#     else:
#         list[i] = list[i-1]*(i+1)
#         i += 1
#         ProductOfNumbers(N, list, i)


# N = int(input('Введите число N: '))
# list = [None for _ in range(N)]
# ProductOfNumbers(N, list)
# print(list)

# 3.Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# n = int(input('Введите число: '))
# result = {n: round((1+(1/n))**n, 2) for n in range(1, n+1)}
# print(result)

# 4.Реализуйте алгоритм перемешивания списка.

# import random
# N = int(input('Введите число N: '))
# list = [random.randint(0, 9) for _ in range(N)]
# print(f'Список до перемешивания: {list}')
# random.shuffle(list)
# print(f'Список после перемешивания: {list}')
