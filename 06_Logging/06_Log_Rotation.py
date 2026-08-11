import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "klyn_app.log"

logger = logging.getLogger("klyn")


file_handler = RotatingFileHandler(
    LOG_FILE,
    maxBytes=2000,
    backupCount=3,
    encoding="utf-8"
)

file_handler.setLevel(logging.INFO)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

for i in range(100):
    logger.info(f"Processing KLYN order number {i}")


