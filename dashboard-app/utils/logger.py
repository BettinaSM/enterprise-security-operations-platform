import logging
import sys

from utils.paths import LOG_DIR

LOG_FILE = LOG_DIR / "soc_platform.log"

# --------------------------------
# LOGGER
# --------------------------------

logger = logging.getLogger(
    "SOC"
)

logger.setLevel(
    logging.INFO
)

# evita duplicação
if not logger.handlers:

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

    )

    # arquivo

    file_handler = logging.FileHandler(
        LOG_FILE
    )

    file_handler.setFormatter(
        formatter
    )

    # console

    console_handler = logging.StreamHandler(
        sys.stdout
    )

    console_handler.setFormatter(
        formatter
    )

    logger.addHandler(
        file_handler
    )

    logger.addHandler(
        console_handler
    )


# --------------------------------
# HELPERS
# --------------------------------

def log_info(message):

    logger.info(message)


def log_warning(message):

    logger.warning(message)


def log_error(message):

    logger.error(message)


def log_exception(message):

    logger.exception(message)
