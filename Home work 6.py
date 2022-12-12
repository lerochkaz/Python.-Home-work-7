# Задача 1.
# S=Pi*a*b #Формула площади эллипса
# Написать функцию find_farthest_orbit(list_of_orbits)
# Ответ в примере неверный, максимальная орбита =113.112 (ответ: (6,6))
# import math
# Pi = round(math.pi, 3)
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# list_of_orbits = list(map(lambda x: str(x).replace(')', ''), orbits))
# list_of_orbits = list(map(lambda x: str(x).replace('(', ''), list_of_orbits))


# def calculation_orbits(orbits_copy):
#     for i in range(len(orbits_copy)):
#         orbits_copy[i] = str(orbits_copy[i]).split(', ')
#         orbits_copy[i] = Pi*float(orbits_copy[i][0])*float(orbits_copy[i][1])


# def find_farthest_orbit(list_of_orbits, orbits):
#     max_number = max(list_of_orbits)
#     index_max_orbit = list_of_orbits.index(max_number)
#     print(orbits[index_max_orbit])


# calculation_orbits(list_of_orbits)
# find_farthest_orbit(list_of_orbits, orbits)

# Задача 3.
# def filling_in_table(table, symbol, num_rows=9, num_columns=9):
#     for j in range(1, num_rows+1):
#         for i in range(1, num_columns+1):
#             match symbol:
#                 case '*':
#                     result = i*j
#                 case '+':
#                     result = (i-1)+(j-1)
#             table.append(result)


# def print_operation_table(table):
#     for index in range(1, len(table)):
#         if index % 9 == 0:
#             print(table[index], end='\n')
#         else:
#             print(table[index], end='\t')


# multiplication_table = [(None for _ in range(10))]
# filling_in_table(multiplication_table, '*')
# print_operation_table(multiplication_table)

# print()

# sum_table = [(None for _ in range(10))]
# filling_in_table(sum_table, '+')
# print_operation_table(sum_table)


# Задача 5.(Из базы тестовых заданий)

# def sort_list(some_list):
#     some_list = sorted(some_list)
#     result_list = ''
#     start_el = some_list[0]
#     stop_el = some_list[0]
#     for i in range(len(some_list)):
#         if i == len(some_list)-1:
#             stop_el = some_list[i]
#             if some_list[i] != some_list[i-1] and len(result_list) < 1:
#                 result_list += (f'{start_el}-{stop_el}')
#             elif some_list[i] != some_list[i-1]:
#                 result_list += (f'{stop_el}')
#             else:
#                 result_list += (f'{start_el}-{stop_el}')
#             return result_list
#         elif (some_list[i])+1 != some_list[i+1]:
#             stop_el = some_list[i]
#             if start_el == stop_el:
#                 result_list += (f'{stop_el}, ')
#             else:
#                 result_list += (f'{start_el}-{stop_el}, ')
#                 start_el = some_list[i+1]


# print(sort_list([1, 4, 5, 2, 3, 9, 8, 11, 0]))
# print(sort_list([1, 4, 3, 2]))
# print(sort_list([1, 4]))
