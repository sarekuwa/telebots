import telebot
import random
from telebot import types
import logging
import os

os.chmod('.api_token', 0o600)
logging.basicConfig(level=logging.DEBUG)

def token_init():
    try:
        with open('.api_token', 'r', encoding='UTF-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("Файл .api_token не найден!")
        return None

def load_data(filename):
    """Безопасная загрузка данных из файла"""
    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        return lines
    except Exception as e:
        logging.error(f"Ошибка загрузки {filename}: {e}")
        return []

api_token = token_init()
bot = telebot.TeleBot(api_token)

# Загружаем данные с проверкой
facts = load_data('data/facts.txt')
quotes = load_data('data/quotes.txt')

# Отладочная информация
print(f"Загружено фактов: {len(facts)}")
print(f"Загружено поговорок: {len(quotes)}")
print("Пример факта:", facts[0] if facts else "НЕТ ДАННЫХ")
print("Пример поговорки:", quotes[0] if quotes else "НЕТ ДАННЫХ")

@bot.message_handler(commands=["start"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Поговорка")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, 
                    'Нажми: \nФакт для получения интересного факта \nПоговорка - для получения мудрой поговорки',
                    reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    answer = None
    
    if message.text.strip() == 'Факт':
        if facts:
            answer = random.choice(facts)
        else:
            answer = "Факты временно недоступны"
            
    elif message.text.strip() == 'Поговорка':
        if quotes:
            answer = random.choice(quotes)
        else:
            answer = "Поговорки временно недоступны"
    else:
        answer = "Используйте кнопки 'Факт' или 'Поговорка'"
    
    # Проверка перед отправкой
    if answer and answer.strip():
        bot.send_message(message.chat.id, answer)
    else:
        logging.error("Попытка отправить пустое сообщение")
        bot.send_message(message.chat.id, "Произошла ошибка при формировании ответа")

if __name__ == '__main__':
    print("Бот запускается...")
    try:
        bot.polling(none_stop=True, interval=0, timeout=60)
    except Exception as e:
        print(f"Ошибка: {e}")
