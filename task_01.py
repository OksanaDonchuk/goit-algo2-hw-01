from typing import List, Tuple

def find_min_max(arr: List[int]) -> Tuple[int, int]:
    """
    Знаходить мінімальний та максимальний елементи в масиві за допомогою методу "розділяй і володарюй".

    :param arr: Список цілих чисел
    :return: Кортеж (мінімум, максимум)
    """
    if len(arr) == 1:
        return arr[0], arr[0]

    if len(arr) == 2:
        return min(arr), max(arr)

    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    global_min = min(left_min, right_min)
    global_max = max(left_max, right_max)

    return global_min, global_max


# Приклад використання
arr = [12, 5, 2, 5, 86, 21, 7, 2, 65, 44]
result = find_min_max(arr)
print(f"Мінімум: {result[0]}, Максимум: {result[1]}")
