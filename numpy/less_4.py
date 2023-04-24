import numpy as np


a = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9])

a.dtype = np.int8()
print(a)
print(a.size)
# Узнать сколько байт занимает один елемент
print(a.itemsize)
# Кол-во осей в масиве
print(a.ndim)
# Число елементов по осям
print(a.shape)
# Изменение представления массива
# print(a.reshape(3, 2, 10))

a = np.array([1,2,3,4,5,6,7,8,9,10])
b = a
a.shape = 3, 3
b = a.view
print(b)