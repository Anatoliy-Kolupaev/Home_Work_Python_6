# Задача № 3
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.


result = []
m = list(map(int, input('Введите числа через пробел: ').split()))
list(map(lambda x: result.append(x) if x not in result else True, m))

print(result)
