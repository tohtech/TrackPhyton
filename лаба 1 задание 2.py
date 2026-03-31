# TODO Найдите количество книг, которое можно разместить на дискете
disk_capacity_mb = 1.44
disk_capacity_kb = (disk_capacity_mb * 1024)   # объем дискеты в КБ
pages = 100               # количество страниц в книге
lines = 50       # строк на странице
chars = 25       # символов в строке
bytes = 4        # байт на символ

# Вычисляем размер книги
total_symbols = pages * lines * chars
book_size_bytes = total_symbols * bytes
book_size_kb = book_size_bytes / 1024  # переводим в КБ

# Считаем, сколько книг помещается на дискету
books_on_disk = int(disk_capacity_kb // book_size_kb)

print("Количество книг, помещающихся на дискету:", books_on_disk)
