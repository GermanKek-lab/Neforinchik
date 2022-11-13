import sqlite3
import telebot

from telebot import types

from config import Config

bot = telebot.TeleBot(Config['token'])
db = sqlite3.connect("anketa.db")
sql = db.cursor()
sql.execute(
    """CREATE TABLE IF NOT EXISTS users(
        user_id    TEXT,
        name       TEXT,
        years      INTEGER,
        desc       TEXT,
        foto       TEXT,
        social   TEXT
        )
    """
)
db.commit()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('НЕфор'), types.KeyboardButton('девушка'))
    bot.send_message(
        message.chat.id,
        f'Привет, {message.from_user.first_name}! '
        f'Добро пожаловать в нефорские знакомства!\n'
        f'ТЫ кто такой по жизни??',
        reply_markup=markup
    )


@bot.message_handler(content_types=['text'])
def bot_message(message):
    main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_markup.add(
        types.KeyboardButton('Создать анкету'),
        types.KeyboardButton('СМотреть анкеты'),
        types.KeyboardButton('Редактировать анкету'),
        types.KeyboardButton('Смотреть мемы с нефорами'),
        types.KeyboardButton('Контакты форов'),
        types.KeyboardButton('Контакты рефоров'))
    if message.text == 'НЕфор':
        bot.send_message(message.chat.id, 'НЕфор - самый главный да'),
    elif message.text == 'девушка':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton('ДА!'), types.KeyboardButton('нет'))
        bot.send_message(message.chat.id, 'Вас зовут Наташа?', reply_markup=markup)
    elif message.text == 'нет':
        bot.send_message(message.chat.id, 'ливай')
    elif message.text == 'ДА!':
        bot.send_message(message.chat.id, 'Добро пожаловать! (скинь инсту)')
    bot.send_message(message.chat.id, 'Выберите', reply_markup=main_markup)
    if message.text == 'Создать анкету':
        create_anketa(message)


@bot.message_handler(commands=['Создать анкету'])
def create_anketa(message):
    person_list = []

    text = ''
    while text:
        bot.send_message(message.chat.id, 'Введите ваше имя')
        text = message.text

    bot.send_message(message.chat.id, 'Введите ваше имя')
    person_list.append(message.text)

    bot.send_message(message.chat.id, 'Введите ваше имя')
    person_list.append(message.text)

    bot.send_message(message.chat.id, 'Введите ваше имя')
    person_list.append(message.text)

    bot.send_message(message.chat.id, 'Введите ваше имя')
    person_list.append(message.text)
    # ID = [str(message.chat.id)]
    # sql.execute("INSERT INTO users VALUES (?,?,?,?,?,?)",
    #             (ID[0], get_name, 0, "0", "0", "0"))
    # db.commit()
    # sql.execute(f"UPDATE users SET act = 'get_name' WHERE iserId = {ID}")
    # db.commit()


bot.polling(none_stop=True, interval=0)
