import json
import os

DATA_FILE = "data/karvands.json"


def create_data_file():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_FILE):
        data = {
            "bootcamp": {
                "name": "Karvand Bootcamp"
            },
            "karvands": []
        }

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


create_data_file()