# budget_analyzer.py
# -------------------
# Простая программа для анализа личных расходов.
# Использует pandas для анализа CSV-файла и matplotlib для визуализации.

import pandas as pd
import matplotlib.pyplot as plt
import os

# === 1. Загрузка данных ===
data_path = os.path.join("data", "expenses.csv")
df = pd.read_csv(data_path)

print("✅ Данные успешно загружены!")
print(df.head(), "\n")

# === 2. Преобразуем колонку 'date' в формат даты ===
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# === 3. Основная аналитика ===
print("=== Общая статистика ===")
total = df["amount"].sum()
mean = df["amount"].mean()

print(f"💰 Всего потрачено: {total:.2f} руб.")
print(f"📊 Средний расход: {mean:.2f} руб.\n")

# === 4. Анализ по категориям ===
category_summary = df.groupby("category")["amount"].sum().sort_values(ascending=False)
print("=== Траты по категориям ===")
print(category_summary, "\n")

# === 5. Сохраняем отчёт в CSV ===
os.makedirs("output", exist_ok=True)
category_summary.to_csv("output/report.csv", header=["total_spent"])
print("📁 Отчёт сохранён в output/report.csv\n")

# === 6. Строим график ===
plt.figure(figsize=(8, 5))
category_summary.plot(kind="bar", color="mediumseagreen")
plt.title("Расходы по категориям", fontsize=14)
plt.xlabel("Категория")
plt.ylabel("Сумма расходов (руб.)")
plt.tight_layout()
plt.show()
