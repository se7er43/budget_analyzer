# 💼 Personal Budget Analyzer

Небольшой pet-проект для демонстрации базовых навыков Python, pandas и matplotlib.

---

## 🎯 Цель проекта
Программа анализирует CSV-файл с личными расходами и выводит:
- общую сумму трат;
- средний расход;
- сводку по категориям;
- визуализацию в виде графика.

---

## 📦 Используемые технологии
- Python 3.10+
- pandas
- matplotlib

---

## 🧩 Структура проекта

budget-analyzer/
│
├── data/
│   └── expenses.csv
│
├── output/
│   └── report.csv
│
├── budget_analyzer.py
│
└── README.md

---

## 🚀 Как запустить
1. Установить зависимости:
   ```bash
   pip install pandas matplotlib

2. Запустить анализ:
   ```bash
   python budget_analyzer.py
 
3. Результаты: 
   На экране появится статистика и график. Отчёт сохранится в output/report.csv.
