numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
# список без пропуска
numbers_no_none = [x for x in numbers if x is not None]

# вычисляем среднее: сумма без None / количество всех элементов
average = sum(numbers_no_none) / len(numbers)

# подставляем найденное значение на место None
missing_index = numbers.index(None)
numbers[missing_index] = round(average, 2)


print("Измененный список:", numbers)
