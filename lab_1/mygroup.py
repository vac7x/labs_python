groupmates = [
    {
        "name": "Леонид",
        "surname": "Мадиков",
        "exams": ["История", "Английский", "Русский"],
        "marks": [3, 5, 5]
    },
    {
        "name": "Петр",
        "surname": "Петров",
        "exams": ["История", "Физика", "Химия"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Афанасий",
        "surname": "Сергеев",
        "exams": ["Философия", "Информатика", "Алгебра"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Мария",
        "surname": "Фонарева",
        "exams": ["Математика", "Физика", "Физкультура"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Игорь",
        "surname": "Гагунов",
        "exams": ["Вышмат", "Химия", "Литература"],
        "marks": [5, 4, 5]
    }
]

# Функция для вычисления среднего балла студента
def calculate_average(mark_list):
    return sum(mark_list) / len(mark_list) if mark_list else 0

# Функция для фильтрации студентов по среднему баллу
def filter_students_by_average(students_list, threshold):
    filtered_students = []
    for student in students_list:
        average_mark = calculate_average(student["marks"])
        if average_mark > threshold:
            filtered_students.append(student)
    return filtered_students

# Функция для вывода списка студентов в виде таблицы
def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(15), u"Экзамены".ljust(40), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), 
              student["surname"].ljust(15), 
              str(student["exams"]).ljust(40), 
              str(student["marks"]).ljust(20))

# Основная часть программы
if __name__ == "__main__":
    try:
        threshold = float(input("Введите средний балл для фильтрации: "))
        filtered_students = filter_students_by_average(groupmates, threshold)
        print(f"\nСтуденты со средним баллом выше {threshold}:")
        if filtered_students:
            print_students(filtered_students)
        else:
            print("Нет студентов с таким средним баллом.")
    except ValueError:
        print("Ошибка: введите числовое значение для среднего балла.")