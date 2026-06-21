import logging

from utils.paths import LOG_DIR

LOG_FILE = LOG_DIR / "soc_platform.log"

logging.basicConfig(

    filename=LOG_FILE,

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)

logger = logging.getLogger("SOC")


def log_info(message):

    logger.info(message)


def log_error(message):

    logger.error(message)


def log_warning(message):

    logger.warning(message)
