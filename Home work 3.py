# 1.	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# from random import randint
# N = int(input('Введите количество элементов в списке: '))
# newList = [randint(0, 9) for _ in range(N)]
# print(f'Сгенерированный список: {newList}')
# sum = 0
# for i in range(1, len(newList), 2):
#     sum += newList[i]
# print(f'Сумма элементов списка, стоящих на нечётной позиции: {sum}')

# 2.	Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from random import randint
# N = int(input('Введите количество элементов в списке: '))
# newList = [randint(0, 9) for _ in range(N)]
# middleIndex = (len(newList))/2
# print(f'Сгенерированный список: {newList}')
# resultList = []

# if (float(middleIndex) == int(middleIndex)):
#     for i in range(int(middleIndex)):
#         result = newList[i]*newList[N-1-i]
#         resultList.append(result)
# else:
#     for i in range(int(middleIndex)):
#         result = newList[i]*newList[N-1-i]
#         resultList.append(result)
#     resultList.append(newList[int(middleIndex)])

# print(f'Произведение пар чисел списка: {resultList}')


# 3.	Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 //неправильный пример т.к. минимальное значение дробной части в примере 0, а максимальное 2

# someList = [1.1, 1.2, 3.1, 5, 10.01]
# print(f'Задан массив: {someList}')
# newList = []
# for i in range(len(someList)):
#     newElement = round((someList[i] % 1), 2)
#     newList.append(newElement)

# maxNumber = max(newList)
# minNumber = min(newList)
# print(
#     f'Разница между максимальным и минимальным значением дробной части: {maxNumber-minNumber}')

# 4.	Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input('Введите число: '))


# def Binarization(number, result='', residueNumber=0):
#     if number < 2:
#         result = (result+str(number))[::-1]
#         print(result)
#     else:
#         residueNumber = number % 2
#         number = number//2
#         result = result+str(residueNumber)
#         Binarization(number, result)


# Binarization(number)
