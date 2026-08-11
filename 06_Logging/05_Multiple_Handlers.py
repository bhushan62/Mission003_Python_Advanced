import logging
from pathlib import Path

# -----------------------------
# Create logs folder path
# -----------------------------
BASE_DIR = Path(__file__).parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "klyn_app.log"

# -----------------------------
# Create logger
# -----------------------------
logger = logging.getLogger("klyn")
logger.setLevel(logging.DEBUG)

# Prevent duplicate handlers if script is run repeatedly
if not logger.handlers:

    # -----------------------------
    # Console handler
    # -----------------------------
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # -----------------------------
    # File handler
    # -----------------------------
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # -----------------------------
    # Formatter
    # -----------------------------
    formatter = logging.Formatter(
        "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # -----------------------------
    # Attach handlers
    # -----------------------------
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

# -----------------------------
# Test logs
# -----------------------------
logger.debug("Connecting to KLYN database")
logger.info("KLYN automation started")
logger.warning("Customer phone number missing")
logger.error("Invoice generation failed")