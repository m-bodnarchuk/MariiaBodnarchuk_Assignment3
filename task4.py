employees = [
{"name": "Олена", "department": "Marketing", "salary":
25000},
{"name": "Ігор", "department": "IT", "salary": 55000},
{"name": "Наталія", "department": "Marketing", "salary":
28000},
{"name": "Олег", "department": "HR", "salary": 22000},
{"name": "Андрій", "department": "IT", "salary": 48000},
{"name": "Марія", "department": "IT", "salary": 52000},
]

# 1. Напишіть функцію get_department_stats(employee_list, target_dept), яка
# приймає два аргументи: список співробітників та назву відділу (рядок).
# 2. Функція повинна:
# ● Відфільтрувати співробітників, які належать до target_dept.
# ● Обчислити середню зарплату в цьому відділі.
# ● Знайти співробітника з найвищою зарплатою в цьому відділі.
# 3. Функція має повертати (return) словник такого вигляду:
# {
# "department": "IT",
# "average_salary": 51666.67,
# "top_earner": "Ігор",
# "count": 3
# }
# 4. Викличте функцію для відділів "IT" та "Marketing" і виведіть результат.
def get_department_stats(employee_list, target_dept) -> dict:
    department_stats = {}
    top_earner = ""
    count = 0
    salaries = []
    dep_emploees = []
    max_salary =0

    for employee in employee_list:
        if employee["department"] == target_dept:
            dep_emploees.append(employee)
    for employee in dep_emploees:
        if employee["salary"] > max_salary:
            max_salary = employee["salary"]
            top_earner = employee["name"]
        count = count + 1
        salaries.append(employee["salary"])
    average_salary = round(sum(salaries) / count, 2)
    department_stats = {
        "department": target_dept,
        "average_salary": average_salary,
        "top_earner": top_earner,
        "count": count
        }
    return department_stats

print(get_department_stats(employees, "IT"))











