from colorama import Fore, Style
from rich.console import Console
from rich.logging import RichHandler
import logging

console = Console()
logger = logging.getLogger("api_logger")
logger.setLevel(logging.DEBUG)

handler = RichHandler(console=console, rich_tracebacks=True, markup=True)
formatter = logging.Formatter("%(message)s", style="%")

handler.setFormatter(formatter)
logger.addHandler(handler)


# Цветной вывод статусов
def colorize_status(status_code: int) -> str:
    """Возвращает статус с цветом по коду"""
    if 200 <= status_code < 300:
        return f"{Fore.GREEN}{status_code}{Style.RESET_ALL}"
    elif 300 <= status_code < 400:
        return f"{Fore.BLUE}{status_code}{Style.RESET_ALL}"
    elif 400 <= status_code < 500:
        return f"{Fore.YELLOW}{status_code}{Style.RESET_ALL}"
    elif 500 <= status_code < 600:
        return f"{Fore.RED}{status_code}{Style.RESET_ALL}"
    else:
        return str(status_code)
