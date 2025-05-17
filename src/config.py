import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

# Токен Telegram-бота из переменных окружения
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Настройки Мосбиржи
MOEX_TOP_STOCKS = 50  # количество акций для отображения


