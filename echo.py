import telebot
import logging
import os

#logging.basicConfig(level=logging.DEBUG)
os.chmod('.api_token', 0o600)

def token_init():
    try:
        with open('.api_token', 'r', encoding='UTF-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Файл .api_token не найден!")
        return None

api_token = token_init()
bot = telebot.TeleBot(api_token)

try:
    bot_info = bot.get_me()
    print(f"Бот @{bot_info.username} успешно инициализирован")
except Exception as e:
    print(f"Ошибка токена: {e}")

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message( message.chat.id,'Я Online. Напиши мне что-нибудь')

# Получение сообщений от пользователя
@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(f"Получено сообщение: {message.text}")  # для отладки
    bot.send_message(message.chat.id,f'Вы написали: {message.text}')

# Обработчик ошибок
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Не понимаю команду")

if __name__ == '__main__':
    print("Бот запускается...")
    try:
        bot.polling(none_stop=True, interval=0, timeout=600)
    except Exception as e:
        print(f"Ошибка: {e}")
