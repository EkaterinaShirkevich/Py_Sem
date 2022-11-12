from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Приветствую, {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hello\n/int_sum\n/int_sub\n/compl_sum\ncompl_sub\n/help\n')

async def int_sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # будет 3 эл-та в списке items: сама команда /sum, первая и вторая порция данных для суммы
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')    

async def int_sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # будет 3 эл-та в списке items: сама команда /sum, первая и вторая порция данных для суммы
    x = int(items[1])
    y = int(items[2])    
    await update.message.reply_text(f'{x} - {y} = {x - y}')     

async def compl_sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # будет 3 эл-та в списке items: сама команда /sum, первая и вторая порция данных для суммы
    a = int(items[1])
    b = int(items[2])  
    c = int(items[3])
    d = int(items[4])
    x = complex(a, b)  
    y = complex(c, d)
    await update.message.reply_text(f'{x} + {y} = {x + y}')    

async def compl_sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    print(msg)
    items = msg.split() # будет 3 эл-та в списке items: сама команда /sum, первая и вторая порция данных для суммы
    a = int(items[1])
    b = int(items[2])  
    c = int(items[3])
    d = int(items[4])
    x = complex(a, b)  
    y = complex(c, d)
    await update.message.reply_text(f'{x} - {y} = {x - y}')        
