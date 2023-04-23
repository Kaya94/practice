import numpy as np
from typing import List
import pprint


def main(arr: List, num) -> None:
    # Создаем масив
    a = np.array(arr)
    print(a)

    # Показываем поддерживаемы виды масива
    print(np.sctypeDict)

    #Преобразование типа в комплексное число
    complex_num = np.complex64(num)
    print(complex_num)

    # Создаем массив из кортежа
    corteg = np.array((1, 2, 3))
    print(corteg)

    # Создаем массив из строки
    line = np.array("Hello World")
    print(line)

    #Создание двухмерного массива
    dim_2_array = np.array([[1, 2], [3, 4], [5, 6]])
    print(dim_2_array)

    # Создание трехмерного массива
    dim_3_array = np.array(
        [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
        [[9, 10], [11,12]]
        ]
    )
    print(dim_3_array)

if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    num = 10
    main(arr, num)