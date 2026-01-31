import json

INPUT_FILENAME = "input.json"

def task() -> float:
    with open(INPUT_FILENAME, encoding="utf-8") as f:
        data = json.load(f)

    total = sum(item["score"] * item["weight"] for item in data)
    return round(total, 3)


print(task())
