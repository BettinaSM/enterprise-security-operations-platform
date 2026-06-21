import os

from dotenv import load_dotenv

load_dotenv()


def get_secret(name):

    return os.getenv(name)
