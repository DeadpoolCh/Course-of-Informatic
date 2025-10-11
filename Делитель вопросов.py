# --- Настройки ---
start = 1
end = 37
exclude = {}  # номера вопросов, которые исключаются
output_file = "questions_distribution.txt"

# --- Основной цикл по количеству людей ---
for count_people in range(2, 10):  # например, от 3 до 9 человек
    number_question = [[] for _ in range(count_people)]

    # фильтруем и распределяем вопросы
    filtered_questions = [num for num in range(start, end + 1) if num not in exclude]

    for idx, num in enumerate(filtered_questions):
        person = idx % count_people
        number_question[person].append(num)

    # # вывод на экран
    # print(f"\nКоличество людей: {count_people}")
    # for i, q in enumerate(number_question, start=1):
    #     print(f"Человек {i}: {q}")

    # запись в файл
    with open(output_file, "a", encoding="utf-8") as f:
        f.write(f"\nКоличество людей: {count_people}\n")
        for i, q in enumerate(number_question, start=1):
            f.write(f"Человек {i}: {q}\n")
