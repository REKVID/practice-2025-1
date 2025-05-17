from telegram import Update
from telegram.ext import ContextTypes
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


async def events_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info("Запрошены экономические события")

    await update.message.reply_text(
        "📊 *Актуальные экономические события*\n\n"
        "Актуальная информация об экономических событиях доступна по ссылке:\n"
        "https://www.rbc.ru/economics/",
        parse_mode="Markdown",
    )
