<a href="https://codeclimate.com/github/mogul03/smd-lab2/maintainability"><img src="https://api.codeclimate.com/v1/badges/14c2ab1677e79ec9a45e/maintainability" /></a>

**Выполнил: Гуляев М.О. (БИВТ-21-1)**

***Обзор функциональности***
**Создание функции приветствия**
    Я создал функцию welcome_user() в файле src/cli.py, которая приветствует пользователя и запрашивает его имя. Функция использует input(), чтобы получить имя пользователя, а затем отображает приветственное сообщение. Это служит первым шагом к предоставлению интерактивного приветствия для игроков.

def welcome_user():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

**Реализация игрового движка**
Я реализовал функцию play_game(game_function) для управления игровым процессом. Эта функция принимает другую функцию (например, lcm_game или geometric_progression_game) в качестве аргумента и запускает её несколько раз (3 раунда, как определено константой ROUNDS). Эта структура упрощает добавление новых игр, просто создавая новые функции, которые следуют аналогичной логике.

ROUNDS = 3

def play_game(game_function):
    for _ in range(ROUNDS):
        game_function()

**Настройка линтера (Flake8)**
Я настроил Flake8 для проверки стиля кода, добавив файл конфигурации .flake8. Это помогает поддерживать высокое качество кода, соблюдая принципы PEP8. Я выбрал игнорировать некоторые специфические предупреждения, которые не критичны для моего проекта (например, E203, E266, W503).

[flake8]
max-line-length = 79
ignore = E203, E266, W503
exclude = __pycache__, venv, .git

**Исправленные ошибки**
Файл brain-games.py

Ошибка: F401 'engine.play_game' imported but unused (импортирован, но не используется).

Исправление: Удалил неиспользуемый импорт.

Ошибка: W293 blank line contains whitespace (пустая строка содержит пробелы).

Исправление: Удалил лишние пробелы в пустых строках.

Ошибка: E302 expected 2 blank lines, found 1 (ожидается 2 пустые строки, но найдено 1).

Исправление: Добавил необходимые пустые строки.

Ошибка: E305 expected 2 blank lines after class or function definition, found 1 (ожидается 2 пустые строки после определения класса или функции, найдено 1).

Исправление: Добавил пустые строки после определений функций.

Ошибка: W391 blank line at end of file (пустая строка в конце файла).

Исправление: Удалил лишнюю пустую строку.

Файл geometric_progression.py

Ошибка: W293 blank line contains whitespace (пустая строка содержит пробелы).

Исправление: Удалил лишние пробелы в пустых строках.

Файл lcm_game.py

Ошибка: E501 line too long (81 > 79 characters) (строка слишком длинная).

Исправление: Разбил длинные строки на более короткие.

Ошибка: W391 blank line at end of file (пустая строка в конце файла).

Исправление: Убедился, что в конце файла нет лишних пустых строк.

**Вывод**
Я исправил все ошибки в коде и убедился, что он соответствует стандартам PEP 8. Теперь код более читабелен и поддерживаем. 
