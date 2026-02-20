import os
import json

# Путь к файлу с администраторами
ADMINS_FILE = "data/admins.json"


def load_admin_ids():
    """Загружает список администраторов из JSON-файла"""
    if not os.path.exists(ADMINS_FILE):
        return set()
    try:
        with open(ADMINS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return set(map(int, data))
    except (json.JSONDecodeError, ValueError) as e:
        print(f"❌ Ошибка чтения {ADMINS_FILE}: {e}")
        return set()
