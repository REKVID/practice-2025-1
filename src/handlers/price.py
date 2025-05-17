from telegram import Update
from telegram.ext import ContextTypes
import logging

from ..services.moex import get_stock_price, check_ticker_exists

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def price_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not context.args or len(context.args) < 1:
        await update.message.reply_text(
            "Пожалуйста, укажите тикер акции после команды.\nНапример: /price SBER"
        )
        return

    ticker = context.args[0].upper()
    logger.info(f"Запрошена цена акции {ticker}")

    if not check_ticker_exists(ticker):
        await update.message.reply_text(
            f"❌ Акция с тикером {ticker} не найдена на Мосбирже.\n"
            "Введите /list для просмотра доступных акций."
        )
        return

    price = get_stock_price(ticker)

    if price is not None:
        await update.message.reply_text(f"💰 Текущая цена акции {ticker}: {price} RUB")
    else:
        await update.message.reply_text(
            f"❌ Не удалось получить цену акции {ticker}.\n"
            "Пожалуйста, попробуйте позже."
        )
