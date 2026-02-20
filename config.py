import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("TOKEN")
    ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(","))) if os.getenv("ADMIN_IDS") else []
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# Удобный доступ
config = Config()