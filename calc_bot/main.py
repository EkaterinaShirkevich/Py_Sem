
from telegram.ext import CommandHandler, ApplicationBuilder
from commands import *
from info import *

from calc_bot.commands import compl_sub_command, compl_sum_command, help_command, int_sub_command, int_sum_command

up = ApplicationBuilder().token(token).build()

up.add_handler(CommandHandler("hello", start))
up.add_handler(CommandHandler("int_sum", int_sum_command))
up.add_handler(CommandHandler("int_sub", int_sub_command))
up.add_handler(CommandHandler("compl_sum", compl_sum_command))
up.add_handler(CommandHandler("compl_sum", compl_sub_command))
up.add_handler(CommandHandler("help", help_command))

print('server starts')

up.run_polling()
