## ⚙️ Установка и настройка

### Создание виртуального окружения
```bash
python -m venv telebots
source venv/bin/activate  # Linux/MacOS
# или
venv\Scripts\activate     # Windows
```

### Установка зависимостей 
```bash
pip install pytelegrambotapi wikipedia
```

Настройка токена бота
bash

# Создайте файл .api_token и добавьте токен
echo "ВАШ_ТОКЕН_ОТ_BOTFATHER" > .api_token

# Установите безопасные права доступа
chmod 600 .api_token

. Подготовка данных

Убедитесь, что в папке data/ находятся файлы:

    facts.txt - по одному факту на строку
    quotes.txt - по одной поговорке на строку
    boltun.txt - вопросы и ответы в формате:
    text
    
u: вопрос
ответ
u: следующий вопрос
ответ

🚀 Запуск ботов
Эхо-бот
bash

python echo.py

Функции: возвращает ваши сообщения
Бот с фактами и поговорками
```bash
python factsandquotes.py
```
Функции:

    Кнопка "Факт" - случайный факт о вселенной

    Кнопка "Поговорка" - случайная поговорка

Wikipedia-бот
bash

python wikisearch.py

Функции: поиск статей в Wikipedia по ключевым словам
🛡️ Безопасность
Файл .gitignore
gitignore

# Токены и секреты
.api_token
.env
*.key

# Виртуальное окружение
venv/
.env/

Важные меры безопасности:

    Токен хранится в отдельном файле
    Файл с токеном имеет права 600
    Все зависимости фиксируются
    Обработка ошибок в каждом боте

### Отладка
Включите debug-режим установкой переменной окружения:
```bash
export DEBUG=True  # Linux/MacOS
set DEBUG=True     # Windows
```

Или измените уровень логирования в коде:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```
📝 Зависимости

Основные библиотеки:
    pyTelegramBotAPI - работа с Telegram API
    wikipedia - поиск в Wikipedia

🔧 Возможные проблемы и решения

Ошибка: "Token file not found"

    Проверьте наличие файла .api_token
    Убедитесь что файл в корне проекта

Ошибка: "Bad Request: unsupported parse_mode"
    Проверьте что передаётся только текст в send_message()

Ошибка: "message text is empty"
    Проверьте что файлы в data/ не пустые
    Убедитесь в правильной кодировке UTF-8

📄 Лицензия

MIT License - свободное использование с указанием авторства.
🤝 Вклад в проект

    Форкните репозиторий
    Создайте ветку для фичи (git checkout -b feature/amazing-feature)
    Закоммитьте изменения (git commit -m 'Add amazing feature')
    Запушьте в ветку (git push origin feature/amazing-feature)
    Откройте Pull Request
⚠️ ВАЖНО: Никогда не коммитьте файл .api_token в Git!



