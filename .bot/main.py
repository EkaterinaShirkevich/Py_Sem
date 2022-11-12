from commands import *
from info import token
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Определяем константы этапов разговора
GET_OPER, GET_NUM, RESULT = range(3)

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(token)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GET_OPER, GET_NUM, RESULT и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        #этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            GET_OPER: [MessageHandler(Filters.regex('^(Рациональное|Комплексное)$'), get_oper)],
            GET_NUM: [MessageHandler(Filters.regex('^( + | - )$'), get_num)],
            RESULT: [MessageHandler(a, b), result]
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()