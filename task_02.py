import random
from typing import List


def quick_select(arr: List[int], k: int) -> int:
    """
    Знаходить k-й найменший елемент у масиві за допомогою алгоритму Quick Select.

    :param arr: Список чисел
    :param k: Позиція найменшого елемента (1 <= k <= len(arr))
    :return: k-й найменший елемент
    :raises ValueError: якщо k виходить за межі масиву
    """
    if k < 1 or k > len(arr):
        raise ValueError(f"Параметр k={k} виходить за межі допустимого діапазону (1-{len(arr)})")

    if len(arr) == 1:
        return arr[0]

    # Вибір опорного елемента (pivot) випадковим чином
    pivot = random.choice(arr)

    # Розподіл елементів навколо опорного
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    larger = [x for x in arr if x > pivot]

    # Визначаємо позицію k відносно розмірів підмасивів
    if k <= len(smaller):
        return quick_select(smaller, k)
    elif k <= len(smaller) + len(equal):
        return pivot
    else:
        return quick_select(larger, k - len(smaller) - len(equal))


# Приклад використання
try:
    arr = [1, 10, 4, 6, 17, 8, 20, 34]
    k = 4
    result = quick_select(arr, k)
    print(f"{k}-й найменший елемент: {result}")
except ValueError as e:
    print(f"Помилка: {e}")