deposit_account = {
"client_id": "C1025",
"balance": 5000.0,
"currency": "UAH",
"interest_rate": 0.08, # 8% річних
"is_active": True
}
# 1. Обчисліть суму нарахованих відсотків за рік (сума = баланс *
# відсоткова_ставка).
# 2. Оновіть значення ключа "balance", додавши до нього нараховані
# відсотки.
# 3. Додайте до словника новий ключ "last_update_type" зі значенням
# "interest accrual".
# 4. Змініть значення ключа "is_active" на False, ніби клієнт закрив рахунок.
# 5. Виведіть на екран фінальний оновлений словник.
interest = deposit_account["balance"] * deposit_account["interest_rate"]
print(f"Сума нарахованих відсотків: {interest:.2f}")
deposit_account["balance"] += interest
deposit_account["last_update_type"] = "interest accrual"
deposit_account["is_active"] = False
print(deposit_account)
# розрахунок чистого прибутку після вирахування податку на дохід фізичних осіб
# (в Україні податок на доходи від депозитних відсотків становить
# 18% ПДФО + 1.5% військовий збір).
deposit_account["inter"] = 0.195
profit = interest * (1-deposit_account["inter"])
print(f"Чистиц прибуток: {profit}")