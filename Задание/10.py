while True:
    user_number = input("Введите число или 'стоп': ")

    if user_number.lower() == 'стоп':
        print("Программа завершена.")
        break

    try:
        number = float(user_number)
        print(f"Введенное число: {number}")
    except ValueError:
        print("Ошибка: введите число или 'стоп'.")