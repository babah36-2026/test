#Mod_4_Total_salary
def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.split(",")
                salary = int(salary)
                total += salary
                count += 1

        if count == 0:
            return 0, 0
        average = total / count

    except FileNotFoundError:
        print("Файл не знайдено")
        return 0, 0

    except ValueError:
        print("Неправильний формат даних у файлі")
        return 0, 0

    return total, average
total, average = total_salary(r"C:\Python\test\Module_4\tabulegram.txt")

print(f"Загальна сума заробітної плати: {total}")
print(f"Середня заробітна плата: {average}")