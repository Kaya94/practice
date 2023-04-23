import numpy as np
from typing import List

# Создаем массив с элиментами и распечатываем тип элементов
def create_array(arr: List):
    a = np.array(arr)
    print(a.dtype)
    return a

def main(arr: List):
    a = create_array(arr)
    return a

if __name__ == "__main__":
    same_type = [1, 2, 3, 4]
    diff_types = [1, "arr", True]
    a = main(same_type)
    b = main(diff_types)

    # Выводим значения True и False
    print(a[True, False, True, False])

    # Решейпим в матрицу 3х3
    reshaped = a.reshape(2, 2)
    print(reshaped)