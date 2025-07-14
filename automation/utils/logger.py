import os
import logging
from datetime import datetime

def setup_logger(name="test_logger"):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"test_{datetime.now().strftime('%Y-%m-%d')}.log")
    logger = logging.getLogger(name)  # ✅ Use logger name, not file path
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers when called multiple times
    if not any(isinstance(h, logging.FileHandler) and h.baseFilename == os.path.abspath(log_file) for h in logger.handlers):
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger
