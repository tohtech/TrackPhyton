def find_first_occurrence(items, target_item):
    """
    Функция для поиска индекса первого вхождения товара в списке

    Args:
        items: список товаров
        target_item: товар, который нужно найти

    Returns:
        Индекс первого вхождения товара или None, если товар не найден
    """
    for index, item in enumerate(items):
        if item == target_item:
            return index
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_first_occurrence(items_list, find_item)  # Вызываем функцию для получения индекса товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")