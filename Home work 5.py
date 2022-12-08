# 1.	Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_text = 'абв вуакукаы чфчкпу абвпар авб цщцву здзюж'

# my_text_list = list(filter(
#     lambda i: 'а' not in i and 'б' not in i and 'в' not in i, my_text.split()))

# print(my_text)
# print(my_text_list)


# 2.	Создайте программу для игры в ""Крестики-нолики"".

# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print("-" * 13)


# def move_X(board):
#     nX = int(input('Куда поставить X? (необходимо ввести номер ячейки): '))
#     board[nX-1] = 'X'
#     return board


# def move_0(board):
#     n0 = int(input('Куда поставить 0? (необходимо ввести номер ячейки): '))
#     board[n0-1] = '0'
#     return board


# def check_win(board):
#     if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
#         draw_board(board)
#         print('Игра окончена, есть победитель!')
#         return True
#     else:
#         return False


# def play_game(i=0):
#     board = list(range(1, 10))
#     while check_win(board) == False:
#         if i < 4:
#             draw_board(board)
#             move_X(board)
#             if check_win(board) == True:
#                 break
#             move_0(board)
#             if check_win(board) == True:
#                 break
#             i += 1
#         else:
#             draw_board(board)
#             print('Ходов больше нет! Начните игру заново')
#             break


# play_game()


# 3.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def compress(path):
#     txt = ''
#     count = 1
#     for i in range(1, len(path)):
#         if i == len(path)-1:
#             if path[i-1] == path[i]:
#                 txt += str(count)+path[i-1]
#             else:
#                 txt += str(count)+path[i-1]+'1'+path[i]
#         elif path[i-1] == path[i]:
#             count += 1
#         else:
#             txt += str(count)+path[i-1]
#             count = 1
#     return txt


# def recovery(string):
#     txt_result = ''
#     for i in range(0, len(string), 2):
#         if i == len(string):
#             txt_result += (n*string[i])
#         else:
#             n = int(string[i])
#             txt_result += (n*string[i+1])
#     return txt_result


# with open('HW5-1.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
#     print(f'Текст из файла: {text}')
#     text_after_compression = compress(text)


# with open('HW5-2.txt', 'w', encoding='utf-8') as f:
#     f.write(text_after_compression)
#     print(f'Текст после сжатия: {text_after_compression}')


# with open('HW5-2.txt', 'r', encoding='utf-8') as f:
#     find_text = f.read()
#     print(f'Текст из файла: {find_text}')
#     text_after_recovery = recovery(find_text)


# with open('HW5-1.txt', 'a+', encoding='utf-8') as file:
#     file.write("\n" + text_after_recovery)
#     print(f'Текст после восстановления: {text_after_recovery}')
