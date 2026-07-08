sales_data = [
{"product": "Смартфон", "category": "Електроніка",
"quantity": 1, "price": 15000},
{"product": "Книга 'Python для всіх'", "category":
"Книги", "quantity": 2, "price": 700},
{"product": "Навушники", "category": "Електроніка",
"quantity": 2, "price": 2500},
{"product": "Чайник", "category": "Побутова техніка",
"quantity": 1, "price": 1200},
{"product": "Книга 'Алгоритми'", "category": "Книги",
"quantity": 1, "price": 900},
{"product": "Ноутбук", "category": "Електроніка",
"quantity": 1, "price": 32000}
]
# 1. Створіть новий порожній словник під назвою category_report.
# 2. Напишіть цикл, що проходить по списку sales_data. Для кожного
# продажу:
# ○ Визначте його категорію.
# ○ Якщо такої категорії ще немає в category_report, створіть для неї
# новий ключ. Значенням для цього ключа має бути словник з
# початковими даними, наприклад: {'total_revenue': 0,
# 'total_items_sold': 0}.
# ○ Оновіть дані для цієї категорії:
# ■ Збільште загальний дохід (total_revenue) на вартість цієї
# транзакції (quantity * price).
# ■ Збільште загальну кількість проданих одиниць
# (total_items_sold) на кількість товарів у цій транзакції
# (quantity).
# 3. Виведіть фінальний словник category_report у зручному для читання
# форматі.
# 4. порахувати всередині звіту ще й середній чек
# для кожної категорії (тобто total_revenue / total_items_sold)

category_report = {}
for item in sales_data:
    category = item["category"]
    revenue = item["quantity"]*item["price"]
    if category not in category_report:
        category_report[category] = {"total_revenue": 0,
                                    "total_items_sold": 0}
    category_report[category]["total_revenue"] += revenue
    category_report[category]["total_items_sold"] += item["quantity"]
for category, data in category_report.items():
    data["average_check"] = round(data["total_revenue"]/data["total_items_sold"], 2)

import pprint
pprint.pprint(category_report)