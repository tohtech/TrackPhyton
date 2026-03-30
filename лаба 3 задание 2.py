def find_common_participants(group1, group2, separator=","):
    """
    Функция для поиска общих участников в двух группах
    """
    # Разделяем строки на списки и преобразуем в множества
    set1 = set(group1.split(separator))
    set2 = set(group2.split(separator))

    # Находим пересечение множеств (общих участников)
    common = set1.intersection(set2)

    # Возвращаем отсортированный список
    return sorted(list(common))