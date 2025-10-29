import telebot, wikipedia, re
import logging
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

wikipedia.set_lang("ru")

def getwiki(string):
    try:
        page = wikipedia.page(string)
        wikitext = page.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikireq = ''

        for x in wikimas:
            if not('==' in x):
                if(len( ( x.strip() ) ) > 3):
                    wikireq = wikireq + x + '.'
                else:
                    break
        
        wikireq = re.sub(r'\([^()]*\)', '', wikireq)
        wikireq = re.sub(r'\{[^\{\}]*\}', '', wikireq)
        return wikireq
    
    except Exception as e:
        logging.error(f"Wikipedia error: {e}")
        return 'В энциклопедии нет информации об этом'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    print(f"Получено сообщение: {message.text}")
    wiki_result = getwiki(message.text)
    response = f'Вы написали: {message.text}\n\nРезультат из Wikipedia:\n{wiki_result}'
    bot.send_message(message.chat.id, response)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
