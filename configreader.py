from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    BOT_TOKEN: str = getenv('BOT_TOKEN', 'Invalid value!')
    ADMIN_ID: int = int(getenv('ADMIN_ID', 'Invalid value!'))


config = Config()
