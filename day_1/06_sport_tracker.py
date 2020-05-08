"""
Пример программы для работы с циклами
"""

cal = 5000
step = 340
step_count = 0

while cal > 3600:
    cal = cal - step
    step_count = step_count + 1

    print(f"Шаг {step_count}, каллории {cal}")
else:
    print(f"Шагов сделано -  {step_count}")