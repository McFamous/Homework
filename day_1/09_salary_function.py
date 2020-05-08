"""
Пример программы для работы с функциями (аналог файла 01_hours_salary)
"""

def salary(hour_cost, day_quantity):
    total = hour_cost * 8 * day_quantity
    final = total - (total * .13)

    return final

a = salary(600, 2)
b = salary(1200, 6)

print(a,b)