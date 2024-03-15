
def total_salary(path):
    total = 0
    average = 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if ',' in line:
                name, salary = line.strip().split(',')
                salary = int(salary)
                total += salary
                average += 1
            else:
                print(f"Невірний формат даних у рядку: '{line.strip()}'. Пропускаємо.")

    if average > 0:
        average_salary = total / average
    else:
        average_salary = 0
    return total, average_salary
path_to_file = 'зарплати_розробників.txt'
total, average = total_salary(path_to_file)
if total is not None and average is not None:
    print(f"Загальна сума зарплат: {total}")
    print(f"Середня зарплата: {average}")