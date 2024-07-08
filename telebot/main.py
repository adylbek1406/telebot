import telebot


TOKEN = '6995667698:AAHxCPWO0DQtS4T9bAoXwHIY3-4Fob4dfJc'
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправка приветственного сообщения
    bot.reply_to(message, "Привет! Я бот.")

    # Отправка изображения
    with open('68179A10-0667-42FE-935B-4F8D969D0450_1_105_c.jpeg', 'rb') as img:
        bot.send_photo(message.chat.id, img, caption="Этот бот хочет чтобы ты старалься.")

@bot.message_handler(commands=['video'])
def send_welcome(message):
            # Отправка приветственного сообщения
            bot.reply_to(message, "Привет! вот тебе видео.")

            # Отправка видео
            with open('E2A02EF2-81A8-4A1F-BF3F-0C955BB1577D_1_102_o.jpeg', 'rb') as vid:
                bot.send_video(message.chat.id, vid, caption="Это видео.")

@bot.message_handler(commands=['help'])
def send_help(message):
    # Отправка сообщения со справкой
    bot.reply_to(message, "Это справочное сообщение. Введите /start для начала работы с ботом.")

@bot.message_handler(commands=['audio'])
def send_welcome(message):
    # Отправка приветственного сообщения
    bot.reply_to(message, "Привет! Я бот с аудиосообщением.")

    # Отправка аудиосообщения
    with open('audio_2024-07-01_14-59-44.ogg', 'rb') as audio:
        bot.send_voice(message.chat.id, audio)



# Обработчик для кнопок
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Создание клавиатуры с кнопками
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    button1 = telebot.types.KeyboardButton('Кнопка 1')
    button2 = telebot.types.KeyboardButton('Кнопка 2')
    keyboard.add(button1, button2)

    # Отправка сообщения с клавиатурой
    bot.reply_to(message, "Выберите кнопку:", reply_markup=keyboard)

# Запуск бота
bot.polling()