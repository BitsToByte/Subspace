"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count

def game_core_v3(number: int = 50) -> int:
    """Идея метода - выбираем предполагаемое число посередине, и в зависимости от того больше или меньше уменьшаем диапазон сверху или снизу соответственно,
       и уже в уменьшеном диапазоне опять берем середину и сравниваем.
    Args:
        number (int, optional): Загаданное число. Defaults to 50.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    predict_range = [1, 100] # Инициализируем предполагаемый диапазон (список из 2 значений - нижняя и верхняя границы)
    predict = 50
    count = 1 # Число попыток выставляем 1 т.к. мы уже первое предположение сделали что predict = 50
    while number != predict: # Если мы инициализирующим предположением угадали, то мы в цикл и не войдем
        count += 1
        if number > predict:
            predict_range[0] = predict + 1 # выставляем нижнюю границу диапазона не включая предполагаемое число (т.е. на 1 выше)
        elif number < predict:
            predict_range[1] = predict - 1 # выставляем верхнюю границу диапазона не включая предполагаемое число (т.е. на 1 ниже)
        predict = int((predict_range[1] - predict_range[0]) / 2) + predict_range[0] # Вычисляем середину от уменьшеного диапазона
    # Ваш код заканчивается здесь

    return count

def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    score_game(game_core_v2)
    score_game(game_core_v3)