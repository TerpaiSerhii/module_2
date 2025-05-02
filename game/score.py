import json
from datetime import datetime

RESULTS_FILE = "game_results.json"

def save_result(name, rounds, score):
    result = {
        "Дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Гравець": name,
        "Кількість рандів": rounds,
        "Ігровий рахунок": score
    }

    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = []

    data.append(result)

    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def get_results():
    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            print("\n--- Результати ігор ---")
            for entry in data:
                print(f"Дата: {entry['Дата']}")
                print(f"Ім'я гравця: {entry['Гравець']}")
                print(f"Кількість раундів: {entry['Кількість рандів']}")
                print(f"Підсумковий рахунок: {entry['Ігровий рахунок']}")
                print("-" * 30)
    except FileNotFoundError:
        print("Результати ще не збережені.")
