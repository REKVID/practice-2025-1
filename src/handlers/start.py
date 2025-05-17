from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [KeyboardButton("💰 Цена акции"), KeyboardButton("📋 Список акций")],
        [KeyboardButton("📅 Экономические события"), KeyboardButton("ℹ️ Помощь")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    message = (
        "👋 *Добро пожаловать в бот Московской Биржи!*\n\n"
        "Я помогу вам быстро получить информацию о ценах акций на Мосбирже "
        "и узнать о предстоящих экономических событиях.\n\n"
        "*Доступные команды:*\n"
        "🔸 `/price <тикер>` - текущая цена акции (например, /price SBER)\n"
        "🔸 `/list` - список популярных акций на Мосбирже\n"
        "🔸 `/events` - предстоящие экономические события\n\n"
        "Вы также можете использовать кнопки ниже для быстрого доступа к функциям.\n"
        "Если вам нужна помощь, просто нажмите кнопку 'ℹ️ Помощь'."
    )

    await update.message.reply_text(
        message, reply_markup=reply_markup, parse_mode="Markdown"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (
        "ℹ️ *Справка по командам:*\n\n"
        "🔸 `/price <тикер>` - получить текущую цену акции\n"
        "  Пример: `/price SBER` - цена акции Сбербанка\n\n"
        "🔸 `/list` - получить список топ-50 акций на Мосбирже\n\n"
        "🔸 `/events` - получить список предстоящих экономических событий\n\n"
        "🔸 `/help` - показать эту справку\n\n"
        "Чтобы узнать цену акции, введите команду `/price` и тикер акции через пробел."
    )

    await update.message.reply_text(message, parse_mode="Markdown")
