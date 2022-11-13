import telebot
from telebot import types # для указание типов

bot = telebot.TeleBot('5718359629:AAFWLgJ6E9O23sjIQVRL_fnE7vKoq5lWlxg')
user_num1 = ''
user_num2 = ''
user_proc = ''
user_result = ''

@bot.message_handler(commands= ['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    msg = bot.send_message(message.chat.id, "Привет " + message.from_user.first_name + ", я бот калькулятор\nВведите число", reply_markup=markup)
    bot.register_next_step_handler(msg, proces_num1_step)

def proces_num1_step(message, user_result = None):
    try:
        global user_num1
        if user_result == None:
            user_num1 = str(message.text)
        else:
            user_num1 = str(user_result)
        murkup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        op1 = types.KeyboardButton('+')
        op2 = types.KeyboardButton('-')
        op3 = types.KeyboardButton('*')
        op4 = types.KeyboardButton('/')
        murkup.add(op1,op2,op3,op4)
        msg = bot.send_message(message.chat.id, 'Выберите опперацию', reply_markup=murkup)
        bot.register_next_step_handler(msg, operations)
    except Exception as e:
        bot.reply_to(message, "Error")

def operations(message):
    try:
        global user_proc
        user_proc = message.text
        markup = types.ReplyKeyboardRemove(selective=False)
        msg = bot.send_message(message.chat.id, 'Введите число', reply_markup=markup)
        bot.register_next_step_handler(msg, proces_num2_step)
    except:
        bot.reply_to(message, 'Error')

def proces_num2_step(message):
    try:
        global user_num2
        user_num2 = str(message.text)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        butt1 = types.KeyboardButton('Результат')
        butt2 = types.KeyboardButton('Продолжить вычисления')
        markup.add(butt1, butt2)
        msg = bot.send_message(message.chat.id, 'Показать результат или продолжить оперцию?', reply_markup=markup)
        bot.register_next_step_handler(msg, alternative)
    except Exception as e:
        bot.reply_to(message, 'Error')



def alternative(message):
    try:
        calc()
        markup = types.ReplyKeyboardRemove(selective=False)
        if message.text == "Результат":
           bot.send_message(message.chat.id, calcRes(), reply_markup=markup)
           send_welcome(message)
        elif message.text == 'Продолжить вычисления':
             proces_num1_step(message, user_result)
    except Exception as e:
         bot.reply_to(message, "Error")



def calcRes():
    global user_num1,user_num2,user_proc, user_result
    return 'Результат ' + str(user_num1) + ' ' + user_proc + ' ' + str(user_num2) +  " =  " + str(user_result)

def calc():
    global user_num1,user_num2,user_proc, user_result
    try: 
        user_result = eval(str(user_num1) + user_proc + str(user_num2))
        return user_result
    except:
        user_result = eval(complex(user_num1) + user_proc + complex(user_num2))
        return user_result


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers
bot.polling(non_stop=True)


