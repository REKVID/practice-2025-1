import requests
import apimoex
from typing import List, Dict, Optional
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def get_stock_price(ticker: str) -> Optional[float]:
    try:
        with requests.Session() as session:
            securities = apimoex.find_securities(
                session, ticker.upper(), columns=("secid",)
            )

            if not securities:
                logger.warning(f"Акция с тикером {ticker} не найдена")
                return None

            data = apimoex.get_board_securities(
                session, table="marketdata", board="TQBR", columns=("SECID", "LAST")
            )

            for item in data:
                if item.get("SECID") == ticker.upper() and item.get("LAST") is not None:
                    return item["LAST"]

            logger.warning(f"Для акции {ticker} нет данных о цене")
            return None

    except Exception as e:
        logger.error(f"Ошибка при получении цены акции {ticker}: {str(e)}")
        return None


def get_top_stocks(limit: int = 50) -> List[Dict[str, str]]:
    try:
        with requests.Session() as session:
            data = apimoex.get_board_securities(
                session,
                board="TQBR",
                columns=(
                    "SECID",
                    "SHORTNAME",
                    "MARKETVALUE",
                    "ISIN",
                    "ISSUESIZE",
                    "PREVLEGALCLOSEPRICE",
                ),
            )

            stocks_with_cap = []
            for item in data:
                if "SECID" in item and "SHORTNAME" in item:
                    market_value = item.get("MARKETVALUE")

                    if market_value is None or market_value == 0:
                        issue_size = item.get("ISSUESIZE")
                        price = item.get("PREVLEGALCLOSEPRICE")

                        if issue_size and price:
                            market_value = issue_size * price

                    stocks_with_cap.append(
                        {
                            "ticker": item["SECID"],
                            "name": item["SHORTNAME"],
                            "capitalization": market_value if market_value else 0,
                        }
                    )

            sorted_stocks = sorted(
                stocks_with_cap,
                key=lambda x: x["capitalization"] if x["capitalization"] else 0,
                reverse=True,
            )

            result = []
            for i, stock in enumerate(sorted_stocks[:limit]):
                result.append({"ticker": stock["ticker"], "name": stock["name"]})

            return result
    except Exception as e:
        logger.error(f"Ошибка при получении списка акций: {str(e)}")
        return []


def check_ticker_exists(ticker: str) -> bool:
    try:
        with requests.Session() as session:
            securities = apimoex.find_securities(
                session, ticker.upper(), columns=("secid",)
            )
            return len(securities) > 0
    except Exception as e:
        logger.error(f"Ошибка при проверке тикера {ticker}: {str(e)}")
        return False
