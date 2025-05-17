from telegram import Update
from telegram.ext import ContextTypes
import logging

from ..services.moex import get_top_stocks
from ..config import MOEX_TOP_STOCKS

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def list_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Запрошен список акций")

    status_message = await update.message.reply_text(
        "⏳ Загружаю список топ-50 акций по капитализации...\n"
        "Это может занять несколько секунд."
    )

    stocks = get_top_stocks(limit=MOEX_TOP_STOCKS)

    if not stocks:
        await status_message.edit_text(
            "❌ Не удалось получить список акций.\nПожалуйста, попробуйте позже."
        )
        return

    message = "📋 Топ-50 акций Мосбиржи по капитализации:\n\n"

    for i, stock in enumerate(stocks, 1):
        message += f"{i}. {stock['ticker']}: {stock['name']}\n"

    message += "\nДля получения цены используйте команду /price <тикер>"

    await status_message.edit_text(message)
