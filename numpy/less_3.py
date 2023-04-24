import numpy as np


def main() -> None:
    # 1. Создаем массив с произвольными значениями
    i_dont_care = np.empty(10)
    print(f'1. \n{i_dont_care}', end='\n\n')

    # 2. Создаем массив с главной диагональю единицы
    diagonal = np.eye(4)
    print(f'2. \n{diagonal}', end='\n\n')

    # 3. Создаем с диагонялью единицами и заданными размерностями
    diagonal_2 = np.eye(4, 2)
    print(f'3. \n{diagonal_2}', end='\n\n')

    # 4. Строго квадратная матрица состоящая из единиц
    straight_diagonal = np.identity(5)
    print(f'4. \n{straight_diagonal}', end='\n\n')

    # 5. Массов из одних нулей
    zero = np.zeros((2, 3, 4))
    print(f'5. \n{zero}', end='\n\n')

    # 6. Создаем массив из всех едениц
    ones = np.ones([4, 3], dtype='int8')
    print(f'6. \n{ones}', end='\n\n')

    # 7. Произвольные массивы состоящии из заданых значений
    full = np.full((3, 2), -1)
    print(f'7. \n{full}', end='\n\n')

    # 8. Создание матрицы из строки
    mat = np.mat("1 2 3 4")
    print(f'8. \n{mat}', end='\n\n')
        #Двумерная матрица из строки
    mat = np.mat("1, 2; 3, 4")
    print(f'8.1. \n{mat}', end='\n\n')

    # 9. Создание матрицы с главной диагональю с задаными значениями
    diag = np.diag([1, 2, 3])
    print(f'9. \n{diag}', end='\n\n')
        # Выделяем диагональные значения из переданной матрицы
    diag = np.diag([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    print(f'9.1 \n{diag}', end='\n\n')
        # Выведем диагональную матрицу с переданной матрицей
    diagflat = np.diagflat([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    print(f'9.1 \n{diagflat}', end='\n\n')

    # 10. Создаем триугольную матрицу
    tri = np.tri(4)
    print(f'10 \n{tri}', end='\n\n')

    # 11. Приведение существующего массива к треугольному виду
    a = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
    tril = np.tril(a)
    print(f'11.1 \n{tril}', end='\n\n')
    triu = np.triu(a)
    print(f'11.2 \n{triu}', end='\n\n')

    # 12. Формируем матрицу Вандермонда
    vander = np.vander([1, 2, 3])
    print(f'12. \n{vander}', end='\n\n')

# ФУНКЦИИ ФОРМИРОВАНИЯ ЧИСЛОВЫХ ДИАПАЗОНОВ

    # 13. Возвращает одномерный массив с равномерно разнесенными числами указанного диапазона
    arange = np.arange(5)
    print(f'13.1 \n{arange}', end='\n\n')
    arange = np.arange(1, 5)
    print(f'13.2 \n{arange}', end='\n\n')
    arange = np.arange(1, 5, 0.5)
    print(f'13.3 \n{arange}', end='\n\n')
    arange = np.arange(0, np.pi, 0.1)
    print(f'13.4 \n{arange}', end='\n\n')
    arange = np.cos(np.arange(0, np.pi, 0.1))
    print(f'13.5 \n{arange}', end='\n\n')

    # 14. Возвращает одномерный массив с равномерно разнесенными числами, используя значения только начала и конца интервала
    linspace = np.linspace(0, np.pi, 0)
    print(f'14.1 \n{linspace}', end='\n\n')
    linspace = np.linspace(0, np.pi, 1)
    print(f'14.2 \n{linspace}', end='\n\n')
    linspace = np.linspace(0, np.pi, 2)
    print(f'14.3 \n{linspace}', end='\n\n')
    linspace = np.linspace(0, np.pi, 3)
    print(f'14.4 \n{linspace}', end='\n\n')

    # 15. Возвращает одномерный массив с числами, равномерно распределенных по логарифмической шкале
    logspace = np.logspace(0, 1, 3)
    print(f'15. \n{logspace}', end='\n\n')



    # 16. Формирование чисел по геометрической прогрессии
    geomspace = np.geomspace(1, 4, 3)
    print(f'16.1 \n{geomspace}', end='\n\n')
    geomspace = np.geomspace(1, 16, 5)
    print(f'16.2 \n{geomspace}', end='\n\n')


    #  Формирование графиков
    # # 17. xl, ..., xn - одномерные последовательности или массивы, используемые для фоормирования координатной сетки по кадой из осей
    # meshgrid = np.meshgrid()


    # # 18. Возвращает массив плотных координатных сеток
    # mgrid = mgrid[]


    # # 19. Возвращает открытую сетку значений
    # ogrid = ogrid[]

    



if __name__ == "__main__":
    main()
