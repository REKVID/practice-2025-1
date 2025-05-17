import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

from .config import BOT_TOKEN

from .handlers import (
    start_command,
    price_command,
    list_command,
    events_command,
    help_command,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def handle_message(update, context):
    text = update.message.text

    if text == "💰 Цена акции":
        await update.message.reply_text(
            "Пожалуйста, введите команду в формате:\n/price <тикер>\n\nНапример: /price SBER"
        )
    elif text == "📋 Список акций":
        await list_command(update, context)
    elif text == "📅 Экономические события":
        await events_command(update, context)
    elif text == "ℹ️ Помощь":
        await help_command(update, context)
    else:
        await update.message.reply_text(
            "Я не понимаю эту команду. Используйте /help для получения списка доступных команд."
        )


def main() -> None:
    logger.info("Запуск бота...")

    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("price", price_command))
    application.add_handler(CommandHandler("list", list_command))
    application.add_handler(CommandHandler("events", events_command))
    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND & ~filters.Regex(r"^/start$"),
            handle_message,
        )
    )

    logger.info("Бот запущен")
    application.run_polling(allowed_updates=["message"])


if __name__ == "__main__":
    main()
