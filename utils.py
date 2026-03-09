import json
import csv
from datetime import datetime

FILE = "expenses.json"


def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"income": 0, "goal": 0, "expenses": []}


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def update_income():
    data = load_data()

    income = float(input("Enter monthly income: "))
    goal = float(input("Enter savings goal: "))

    data["income"] = income
    data["goal"] = goal

    save_data(data)

    print("Income and goal updated.")


def add_expense():
    data = load_data()

    amount = float(input("Amount: "))
    category = input("Category: ")
    desc = input("Description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    data["expenses"].append({
        "amount": amount,
        "category": category,
        "description": desc,
        "date": date
    })

    save_data(data)

    print("Expense added.")


def delete_expense():
    data = load_data()

    for i, exp in enumerate(data["expenses"]):
        print(i, exp)

    index = int(input("Enter index to delete: "))

    if 0 <= index < len(data["expenses"]):
        data["expenses"].pop(index)
        save_data(data)
        print("Deleted")
    else:
        print("Invalid index")


def monthly_summary(month, year):
    data = load_data()

    total = 0

    for exp in data["expenses"]:
        date = datetime.strptime(exp["date"], "%Y-%m-%d")

        if date.month == int(month) and date.year == int(year):
            total += exp["amount"]

    print("\n===== Monthly Summary =====")
    print("Total expenses:", total)
    print("Income:", data["income"])
    print("Savings:", data["income"] - total)


def export_csv(start_m, start_y, end_m, end_y):
    data = load_data()

    start = datetime(int(start_y), int(start_m), 1)
    end = datetime(int(end_y), int(end_m), 31)

    rows = []

    for exp in data["expenses"]:
        date = datetime.strptime(exp["date"], "%Y-%m-%d")

        if start <= date <= end:
            rows.append(exp)

    with open("expenses_export.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["date", "amount", "category", "description"])
        writer.writeheader()
        writer.writerows(rows)

    print("Exported to expenses_export.csv")
