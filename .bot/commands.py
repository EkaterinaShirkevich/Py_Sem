from logs import logger
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler
from model_sum import *
from model_sub import *
from compl import *

# Определяем константы этапов разговора
GET_OPER, GET_NUM, RESULT = range(3)

a = ''
b = ''
user_oper = ''
user_type = ''
user_nums = ''
res = ''

# функция обратного вызова точки входа в разговор
def start(update, _):
    # Список кнопок для ответа
    reply_keyboard = [['рациональное', 'комплексное']]
    # Создаем простую клавиатуру для ответа
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Приветствую, мои маленькие программисты! Давайте посчитаем)'
        ' Команда /cancel, чтобы прекратить разговор.\n\n'
        'С какими числами работаем?',
        reply_markup=markup_key,)
    return GET_OPER

# Обрабатываем выбор пользователя
def get_oper(update, _):
    # global user_type
    # user_type = update.message.from_user
    reply_keyboard = [['+', '-']]
    markup_key = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(
        'Хорошо. Выберете операцию: введите + или _, или /cancel, чтобы прекратить разговор.\n\n.',
        reply_markup=markup_key,)
    return GET_NUM

def get_num(update, _):
    global user_oper
    user_oper = update.message.from_user
    if get_oper == 'комплексное':
        update.message.reply_text(
        'Введите число 1, число 2, число 3 и число 4 через пробел'
        ' для формирования комплексных чисел, или /cancel, чтобы прекратить разговор.\n\n.'
    )
    if get_oper == 'рациональное':
        update.message.reply_text(
        'Введите число 1 и число 2 через пробел,'
        ' или /cancel, чтобы прекратить разговор.\n\n.'
    )
    return RESULT

def result(update, _):
    global res 
    global user_nums
    global a
    global b
    user_nums = update.message.from_user
    (a, b) = update.message.nums
    if get_oper == 'комплексное' and get_num == '+':
        a = a.cal_compl
        b = b.cal_compl
        res = complex(a + b)
        update.message.reply_text(
        '{res}, /cancel, чтобы прекратить разговор.\n\n.'
    )
    if get_oper == 'комплексное' and get_num == '-':
        a = a.cal_compl
        b = b.cal_compl
        res = complex(a - b)
        update.message.reply_text(
        '{res}, /cancel, чтобы прекратить разговор.\n\n.'
    )

# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

# # Обрабатываем сообщение с рассказом/биографией пользователя
# def bio(update, _):
#     # определяем пользователя
#     user = update.message.from_user
#     # Пишем в журнал биографию или рассказ пользователя
#     logger.info("Пользователь %s рассказал: %s", user.first_name, update.message.text)
#     # Отвечаем на то что пользователь рассказал.
#     update.message.reply_text('Спасибо! Надеюсь, когда-нибудь снова сможем поговорить.')
#     # Заканчиваем разговор.
#     return ConversationHandler.END















# board = list(map(str, range(1, 10)))

# def draw_board():
#     print('-' * 20)
#     for i in range(3):
#         for k in range(3):
#             print(f"{board[k + i * 3]:^5}", end=" ")
#         print(f"\n{'-' * 20}")
#     print()


# def place_sign(token):
#     global board
#     while True:
#         answer = input(f"Enter a number from 1 to 9.\nSelect a position {token}? ")
#         if answer.isdigit() and int(answer) in range(1, 10):
#             answer = int(answer)
#             pos = board[answer - 1]
#             if pos not in (chr(10060), chr(11093)):
#                 board[answer - 1] = chr(10060) if token == "X" else chr(11093)
#                 break
#             else:
#                 print(f"This cell is already occupied{chr(9995)}{chr(129292)}")
#         else:
#             print(f"Incorrect input{chr(9940)}. Are you sure you entered a correct number?")


# def check_win():
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     n = [board[x[0]] for x in win_coord if board[x[0]] == board[x[1]] == board[x[2]]]
#     return n[0] if n else n


# def main():
#     counter = 0
#     draw_board()
#     while True:
#         place_sign("O") if counter % 2 else place_sign("X")
#         draw_board()

#         if counter > 3:
#             if check_win():
#                 print(f"{check_win()} - WIN{chr(127942)}{chr(127881)}!")
#                 break
#         if counter == 8:
#             print(f"Drawn game {chr(129318)}{chr(129309)}!")
#             break
#         counter += 1


# main()
