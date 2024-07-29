import timeit
import random

# Реалізація алгоритму сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Реалізація алгоритму сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для вимірювання часу виконання
def measure_time(sort_func, arr):
    start_time = timeit.default_timer()
    sort_func(arr)
    end_time = timeit.default_timer()
    return end_time - start_time

# Генерація тестових даних
sizes = [100, 1000, 10000]
datasets = {size: [random.randint(0, 10000) for _ in range(size)] for size in sizes}

# Вимірювання часу виконання алгоритмів
results = {}
for size, data in datasets.items():
    data_copy1 = data[:]
    data_copy2 = data[:]
    data_copy3 = data[:]

    results[size] = {
        'merge_sort': measure_time(merge_sort, data_copy1),
        'insertion_sort': measure_time(insertion_sort, data_copy2),
        'timsort': measure_time(sorted, data_copy3)
    }

import pandas as pd
results_df = pd.DataFrame(results)
print(results_df)
